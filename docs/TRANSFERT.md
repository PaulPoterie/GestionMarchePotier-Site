# Publication GitHub Pages et domaine personnalisé

## Publication automatique

Dépôt : https://github.com/PaulPoterie/GestionMarchePotier-Site

Adresse GitHub Pages initiale : https://paulpoterie.github.io/GestionMarchePotier-Site/

Chaque push sur `main` déclenche le workflow de construction et de déploiement. Seuls les fichiers statiques générés dans `public/` sont publiés. Aucun hébergement WordPress n’est nécessaire pour la vitrine ; les utilisateurs du plugin l’installent toujours sur leur propre WordPress.

## Relier le sous-domaine

Adresse souhaitée : https://gestion-marche-potier.poterie-navarraise.info

1. Retrouver le fournisseur qui gère la zone DNS de `poterie-navarraise.info`.
2. Vérifier le domaine dans les paramètres Pages du compte GitHub avec l’enregistrement TXT fourni par GitHub ; conserver cet enregistrement.
3. Dans le dépôt, ouvrir Settings → Pages → Custom domain, saisir `gestion-marche-potier.poterie-navarraise.info`, puis enregistrer.
4. Dans la zone DNS, créer un enregistrement **CNAME** :

   | Champ | Valeur |
   |---|---|
   | Nom / sous-domaine | `gestion-marche-potier` |
   | Cible | `paulpoterie.github.io` |
   | TTL | Valeur par défaut du fournisseur |

   La cible ne contient ni `https://` ni le nom du dépôt. S’il existe déjà un enregistrement pour ce sous-domaine, examiner sa destination avant de le remplacer. Ne pas modifier les enregistrements du domaine principal, du courrier ou des autres sous-domaines.
5. Attendre la validation DNS et l’émission du certificat par GitHub, puis activer **Enforce HTTPS** dès que disponible.
6. Contrôler l’accueil, les cinq images, la FAQ, les ancres, le lien de téléchargement GitHub et le lien email sur le domaine final.

Avec le workflow GitHub Actions utilisé ici, le domaine se configure dans les paramètres Pages ; aucun fichier CNAME n’est nécessaire dans les sources.

La liaison du domaine dépend du fournisseur DNS, encore à préciser. Ne configurer le domaine personnalisé GitHub que lorsque la modification DNS peut être réalisée, pour éviter une redirection vers un sous-domaine non prêt.

## Retour arrière

Pour le contenu, utiliser `git revert` sur le commit concerné et pousser sur `main` : le workflow republie l’état précédent. Pour abandonner Pages, retirer le CNAME DNS et le domaine personnalisé des paramètres GitHub ensemble afin de ne pas laisser de DNS pointant vers un site non attribué.

La version WordPress locale reste conservée comme archive. Elle ne doit pas être copiée dans le dépôt public.

## Documentation officielle

- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages
