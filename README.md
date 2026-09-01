# EdenFlor — maquette statique, cinq pages

Fleuriste. Boutique en ligne, parcours de deuil distinct, page de livraison.

Cinq pages HTML, une feuille de style, quatorze illustrations SVG. Aucune
dépendance externe, aucun script tiers, aucune requête vers un CDN : on dépose
le dossier tel quel sur l'hébergement et ça marche.

## Contenu

```
index.html        accueil
boutique.html     catalogue, filtres par occasion (ils fonctionnent)
bouquet.html      une fiche produit complète
deuil.html        parcours distinct pour les obsèques
livraison.html    zones, délais, absence, fraîcheur
assets/           site.css + 14 illustrations SVG
source/           les scripts qui régénèrent le tout
```

## Régénérer

```
cd source
python3 gen_visuals.py     # écrit les 14 SVG dans ../assets — graines fixes,
                           # deux exécutions donnent des fichiers identiques
python3 build.py           # écrit les 5 pages HTML
```

Le gabarit (en-tête, panier, pied de page, bandeau) est écrit **une seule
fois** dans `build.py`. Si la feuille de style change, incrémenter
`VERSION_CSS` — sinon le navigateur ressert l'ancien fichier et on teste dans
le vide.

## Ce qui n'était pas dans le brief

Le brief tenait en une ligne : *EdenFlor, spécialisé dans la fleur,
edenflor.com*, plus un lien vers un thème ThemeForest de boutique de fleurs.

Le thème est une **boutique** — panier, fiche, paiement. C'est donc une
boutique qui est construite ici. J'en prends la **structure**, pas le thème :
je ne redistribue pas un thème acheté.

**Question posée et toujours ouverte :** EdenFlor *vend* des fleurs, ou *met en
relation* des fleuristes ? « Spécialisé dans la fleur » peut vouloir dire les
deux, et ce n'est pas le même produit. Cette maquette répond à la première
hypothèse. Si c'est la seconde, ce qui change est le catalogue et le panier ;
l'ossature, la charte et les pages de contenu restent.

## Les trois décisions de fond

**1. Le bouquet livré n'est jamais exactement celui de la photo.**
C'est vrai chez tous les fleuristes : la fleur est saisonnière, l'arrivage
varie, on remplace par une tige équivalente. La plupart des sites rangent cette
phrase dans les CGV et récoltent des litiges le jour d'un anniversaire. Ici
elle est **sur la fiche produit, au-dessus du bouton d'achat** — et la suite de
vérification le prouve par la géométrie, pas en lisant le HTML.

Garanti : la gamme de couleurs, la taille, la valeur.
Non garanti : la liste exacte des variétés.

**2. Le deuil a son propre parcours.**
Une commande de deuil ne se livre pas « dans la journée à une personne » : elle
doit arriver **avant une heure précise**, dans un lieu qui a ses horaires
d'accès, et elle n'est pas rattrapable le lendemain. Le formulaire demande donc
la date *et l'heure* de la cérémonie, le lieu, le nom du défunt et le texte du
ruban. Une commande que le délai ne permet pas d'honorer est refusée avant,
pas remboursée après.

**3. Ce que je ne sais pas de son commerce reste visiblement vide.**
Zones desservies, heure limite, frais, délais, durée de la garantie de
fraîcheur : ce sont ses décisions, et je n'ai même pas son pays. Huit lignes de
la page Livraison portent donc la mention **« à définir »**.

Attention à ne pas la confondre avec le « à vérifier » du site Amarimmo :

| mention | site | ce que ça veut dire |
|---|---|---|
| `à vérifier` | Amarimmo | une autorité publie la valeur, personne ne l'a encore lue à une date précise |
| `à définir` | EdenFlor | **il n'existe aucun barème à consulter** — c'est une décision commerciale à prendre |

La nuance est écrite sur la page elle-même. Marquer « à vérifier » des frais de
livraison enverrait quelqu'un chercher un barème que personne n'a jamais écrit.

## Les illustrations

Générées ici, vectorielles, libres de tout droit. Un site de fleuriste se vend
à la photo — et c'est justement le problème : je n'ai aucune photo dont EdenFlor
détienne les droits. Une image de banque ou, pire, celle d'un concurrent, ne se
remarque pas avant la mise en demeure.

Elles se remplacent par ses vraies photos quand il les envoie : c'est un
changement de fichier, pas de gabarit. Deux formats — vignette 4:3 pour le
catalogue, bannière 1800×780 pour les en-têtes, avec la composition décalée à
droite pour laisser la gauche au texte.

## Ce qui reste à faire

- Les valeurs de la page Livraison (les huit lignes « à définir »).
- Le pays et la ville : toute la logique de livraison en dépend.
- Les vraies photos, les vrais prix, les vrais noms de bouquets.
- Les coordonnées (le pied de page dit « à compléter »).
- Mentions légales, CGV, politique de confidentialité.
- Les formulaires n'ont pas d'adresse de réception : ils sont interceptés en
  JavaScript pour ne pas recharger la page et avoir l'air cassés.
- Le panier n'est pas connecté : c'est une démonstration d'interface.
