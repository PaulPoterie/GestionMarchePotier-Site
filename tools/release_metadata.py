"""Resolve only the official installable ZIP from the latest stable release."""
import json
import os
import re
from urllib.request import Request, urlopen

REPO = 'https://github.com/PaulPoterie/MarchePotier'

def validate(data):
    version = data.get('VERSION', '')
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        raise ValueError('Unsupported stable version')
    expected = {
        'VERSION': version,
        'RELEASE_URL': f'{REPO}/releases/tag/v{version}',
        'DOWNLOAD_URL': f'{REPO}/releases/download/v{version}/poterie-navarraise-market-manager-{version}.zip',
    }
    if data != expected:
        raise ValueError('Unexpected release URL or asset')

def fetch_latest():
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'GestionMarchePotier-Site'}
    if os.environ.get('GITHUB_TOKEN'):
        headers['Authorization'] = 'Bearer ' + os.environ['GITHUB_TOKEN']
    request = Request('https://api.github.com/repos/PaulPoterie/MarchePotier/releases/latest', headers=headers)
    with urlopen(request, timeout=30) as response:
        release = json.load(response)
    if release.get('draft') or release.get('prerelease'):
        raise ValueError('Only published stable releases are allowed')
    version = release['tag_name'].removeprefix('v')
    name = f'poterie-navarraise-market-manager-{version}.zip'
    assets = [a for a in release.get('assets', []) if a['name'] == name and a.get('state') == 'uploaded' and a.get('size', 0) > 0]
    if len(assets) != 1:
        raise ValueError('Expected installable ZIP missing; current deployment is preserved')
    data = {'VERSION': version, 'DOWNLOAD_URL': assets[0]['browser_download_url'], 'RELEASE_URL': release['html_url']}
    validate(data)
    return data
