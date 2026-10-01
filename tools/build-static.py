"""Build the static showcase with Python's standard library only."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'site'
OUTPUT = ROOT / 'public'
OUTPUT.mkdir(exist_ok=True)
content = (SOURCE / 'accueil.html').read_text(encoding='utf-8')
navigation = ''.join(f'<a href="#{anchor}">{label}</a>' for label, anchor in [
    ('Fonctionnalités', 'fonctionnalites'), ('Captures', 'captures'),
    ('Installation', 'installation'), ('FAQ', 'faq'), ('Télécharger', 'telechargement')])
header = f'<header class="site-header"><p class="brand"><a href="./">Gestion Marché Potier<span class="brand-subtitle">par Poterie Navarraise</span></a></p><nav class="site-nav" aria-label="Navigation principale">{navigation}</nav></header>'
footer = '<footer class="site-footer"><p class="signature">fait par Poterie Navarraise</p><p><a href="mailto:paul@poterie-navarraise.info">Contact</a> · <a href="#telechargement">Téléchargement</a> · <a href="#installation">Installation</a></p></footer>'
page = f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Gestion Marché Potier — par Poterie Navarraise</title>
<meta name="description" content="Organisez vos marchés potiers avec WordPress : éditions, candidatures, jury, historiques et galerie. Découvrez et téléchargez le plugin gratuit 0.19.3.">
<meta name="theme-color" content="#93462f">
<link rel="stylesheet" href="style.css">
</head>
<body><a class="skip-link" href="#contenu">Aller au contenu</a>
{header}<main id="contenu">{content}</main>{footer}
</body></html>
'''
assert '<?php' not in page and 'gestion-marche-potier.local' not in page
assert 'Avant de collecter des dossiers' not in page
assert 'Les justificatifs sont-ils protégés' not in page
(OUTPUT / 'index.html').write_text(page, encoding='utf-8')
(OUTPUT / '.nojekyll').touch()
shutil.copy2(SOURCE / 'style.css', OUTPUT / 'style.css')
shutil.copytree(SOURCE / 'assets', OUTPUT / 'assets', dirs_exist_ok=True)
print(f'Site statique généré : {OUTPUT}')
