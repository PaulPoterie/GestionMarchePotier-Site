# Gestion Marché Potier — site statique

Site vitrine français du plugin **Poterie Navarraise Pottery Market Manager 0.19.3**, par Poterie Navarraise. Présentation, captures réelles, installation, FAQ et téléchargement depuis la release officielle du plugin. Le plugin est en cours de révision sur WordPress.org, sans approbation annoncée.

## Modifier le site

- `site/accueil.html` : textes, sections, liens et FAQ, en HTML simple.
- `site/style.css` : présentation et adaptation mobile.
- `site/assets/` : captures réelles du plugin et de l’éditeur WordPress.
- `tools/build-static.py` : assemblage de la page, de la navigation et du pied de page.

Aucune dépendance Python externe, aucun serveur PHP, aucune base de données, aucun JavaScript requis dans le navigateur. Le site utilise les polices système et ne charge aucun outil de suivi.

## Prévisualisation locale

Avec Python 3 installé :

```powershell
python tools/build-static.py
python -m http.server 4173 --bind 127.0.0.1 --directory public
```

Ouvrir http://127.0.0.1:4173/. Après une modification des sources, relancer la construction et actualiser le navigateur. Arrêter le serveur avec Ctrl+C.

## Publication automatique

Le dépôt GitHub public est `PaulPoterie/GestionMarchePotier-Site`. Le workflow `.github/workflows/pages.yml` construit et publie uniquement le dossier `public/` à chaque push sur `main`. Dans Settings → Pages, la source est **GitHub Actions**.

```powershell
git add site tools/build-static.py README.md docs .github .gitignore
git commit -m "Mettre à jour le site"
git push origin main
```

L’onglet Actions donne le résultat du déploiement. Une ancienne version peut être rétablie avec `git revert`, puis un push. Les images et liens relatifs fonctionnent avec l’adresse GitHub Pages et le sous-domaine personnalisé.

Voir [la procédure de domaine et de publication](docs/TRANSFERT.md).

## Origine et conservation

La présentation a d’abord été validée dans WordPress puis convertie en site statique le 1er octobre 2026. Les classes CSS héritées du thème ne nécessitent pas WordPress.

Les fichiers de la version WordPress, ses exports et l’installation Local sont conservés sur le poste, exclus de Git. Ils ne sont ni téléversés ni déployés. L’éditeur WordPress ne modifie plus cette nouvelle version statique.

Les captures d’accueil et d’historique proviennent des tests du 30 septembre 2026 ; les légendes signalent les anciennes versions et données de test. Les trois captures d’insertion de blocs ont été réalisées avec le plugin 0.19.3 le 1er octobre 2026. Le code du plugin et les autres installations WordPress n’ont pas été modifiés.

Contact : paul@poterie-navarraise.info.
