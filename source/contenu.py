# -*- coding: utf-8 -*-
"""
EdenFlor — contenu de la maquette.

CE QUE J'AI COMME BRIEF, ET CE QUE JE N'AI PAS.

Reçu : « EdenFlor / spécialisé dans la fleur / edenflor.com » et un lien vers un
thème ThemeForest de boutique de fleurs, « inspired from this one ». Le thème
est une BOUTIQUE : panier, fiche produit, paiement. C'est donc une boutique que
je construis. Je prends la STRUCTURE d'une boutique de fleurs, pas le thème :
je ne redistribue pas un thème acheté, et je ne l'ai pas.

Reste ouverte la question que je lui ai posée et qui n'a pas de réponse :
EdenFlor VEND des fleurs, ou MET EN RELATION des fleuristes ? « Spécialisé dans
la fleur » peut vouloir dire les deux, et ce n'est pas le même produit. Cette
maquette répond à la première hypothèse. Si c'est la seconde, ce qui change est
le catalogue et le panier ; l'ossature, la charte et les pages de contenu
restent.

LES TROIS DÉCISIONS DE FOND DE CETTE MAQUETTE.

  1. LE BOUQUET LIVRÉ N'EST JAMAIS EXACTEMENT CELUI DE LA PHOTO.
     C'est vrai chez tous les fleuristes du monde : la fleur est saisonnière,
     l'arrivage varie, on remplace par une tige équivalente. La plupart des
     sites planquent cette phrase dans les CGV, et récoltent des litiges de
     clients furieux le jour d'un anniversaire. Ici elle est ÉCRITE SUR LA FICHE
     PRODUIT, avant le bouton d'achat. Ça se dit une fois, ça évite un
     remboursement, et ça se lit comme du sérieux plutôt que comme une clause.

  2. LE DEUIL N'EST PAS UNE OCCASION COMME LES AUTRES.
     Une commande de deuil se livre à une heure de cérémonie, dans un lieu, pas
     chez une personne, et elle n'est pas rattrapable le lendemain. Le même
     tunnel que pour un anniversaire ne convient pas : il lui faut sa date ET
     son heure, l'adresse du lieu, et le ruban. C'est une page à part.

  3. LES CHIFFRES QUE JE N'AI PAS RESTENT VISIBLEMENT VIDES.
     Zones de livraison, heure limite, frais, délais : ce sont des données de
     SON commerce et je ne les connais pas — je n'ai même pas son pays. Comme
     sur Amarimmo, une case vide et visible vaut mieux qu'un chiffre plausible.
     Mais la mention est différente et le dit : sur Amarimmo, « à vérifier »
     désigne une valeur réglementaire publiée par une autorité. Ici, « à
     définir » désigne une décision commerciale qui lui appartient. Confondre
     les deux laisserait croire qu'il y a quelque part un barème à consulter.

Les PRIX affichés sont des exemples, marqués comme tels sur chaque fiche et
dans le bandeau de démonstration.
"""

# --- gammes de bouquets -----------------------------------------------------
# (id, image, nom, gamme, occasions, description, prix d'exemple par taille)
BOUQUETS = [
    ("tendresse", "b-tendresse", "Tendresse", "Tons poudrés",
     ["Anniversaire", "Amour", "Naissance"],
     "Roses, renoncules et gypsophile dans une gamme rose pâle. Le bouquet qui ne se "
     "trompe jamais de destinataire : il convient à une déclaration comme à un merci.",
     [("Petit", "45"), ("Moyen", "65"), ("Grand", "95")]),
    ("plein-soleil", "b-soleil", "Plein Soleil", "Tons jaunes",
     ["Anniversaire", "Félicitations", "Remerciement"],
     "Tournesols, roses jaunes et feuillage clair. Une gamme franche, qui se voit "
     "d'un bout à l'autre d'une pièce — pour une nouvelle qu'on annonce fort.",
     [("Petit", "42"), ("Moyen", "62"), ("Grand", "89")]),
    ("crepuscule", "b-crepuscule", "Crépuscule", "Tons violets",
     ["Amour", "Remerciement", "Entreprise"],
     "Lisianthus, statice et eucalyptus. La gamme la plus sobre du catalogue, celle "
     "qui tient dans un bureau ou une entrée sans écraser ce qu'il y a autour.",
     [("Petit", "48"), ("Moyen", "70"), ("Grand", "99")]),
    ("neige", "b-neige", "Neige", "Blanc et vert",
     ["Naissance", "Mariage", "Deuil", "Entreprise"],
     "Roses blanches, freesias et verdure. Le blanc est la seule gamme qui traverse "
     "toutes les occasions — d'une naissance à un hommage, selon la façon de le lier.",
     [("Petit", "46"), ("Moyen", "68"), ("Grand", "98")]),
    ("brasier", "b-brasier", "Brasier", "Tons corail",
     ["Anniversaire", "Félicitations", "Amour"],
     "Renoncules corail, roses orangées et feuillage sombre. Une gamme chaude, pour "
     "quelqu'un dont on sait qu'il n'aime pas le pastel.",
     [("Petit", "44"), ("Moyen", "66"), ("Grand", "92")]),
    ("jardin", "b-jardin", "Jardin d'Hiver", "Composition en vase",
     ["Entreprise", "Remerciement", "Anniversaire"],
     "Composition montée dans son vase, prête à poser. Rien à couper, rien à "
     "arranger : c'est ce qu'il faut quand le destinataire est au travail.",
     [("Moyen", "78"), ("Grand", "112")]),
    ("atelier", "b-atelier", "Atelier", "Composition en vase",
     ["Amour", "Remerciement"],
     "Même principe, gamme poudrée. Le vase est compris et fait partie du prix.",
     [("Moyen", "74"), ("Grand", "106")]),
    ("verdure", "b-verdure", "Verdure", "Plante fleurie",
     ["Entreprise", "Remerciement", "Naissance"],
     "Une plante fleurie en pot plutôt qu'un bouquet coupé : elle tient des mois, "
     "et c'est souvent le meilleur choix pour un bureau.",
     [("Moyen", "52"), ("Grand", "76")]),
]

# --- deuil : catalogue séparé, tunnel séparé -------------------------------
DEUIL = [
    ("couronne", "d-couronne", "Couronne",
     "Couronne ronde montée sur mousse, feuillage et fleurs de saison. Se dépose "
     "au pied du cercueil ou à l'entrée. Ruban avec inscription compris.",
     [("Moyen", "à définir"), ("Grand", "à définir")]),
    ("gerbe", "d-gerbe", "Gerbe",
     "Gerbe à plat, présentée le long du cercueil. Gamme sobre, feuillage sombre. "
     "Ruban avec inscription compris.",
     [("Moyen", "à définir"), ("Grand", "à définir")]),
]

# --- occasions du menu ------------------------------------------------------
OCCASIONS = [
    ("Anniversaire", "Le plus demandé, et celui qui pardonne le moins un retard."),
    ("Amour", "Saint-Valentin comprise, avec ses contraintes de volume."),
    ("Naissance", "Livraison en maternité : horaires et service à vérifier."),
    ("Remerciement", "Souvent envoyé au bureau plutôt qu'au domicile."),
    ("Félicitations", "Diplôme, promotion, emménagement."),
    ("Mariage", "Sur devis : ce n'est pas une commande en ligne."),
    ("Deuil", "Tunnel distinct — date et heure de cérémonie, lieu, ruban."),
    ("Entreprise", "Réception, accueil, abonnement hebdomadaire."),
]

# --- ce que je ne connais pas de son commerce -------------------------------
# Ce ne sont PAS des valeurs réglementaires : ce sont ses décisions. La mention
# est donc « à définir » et pas « à vérifier ». La distinction est écrite sur
# la page, parce qu'elle est inutile si seul l'auteur la voit.
LIVRAISON = [
    ("Pays et villes desservis",
     "toute la logique du site en dépend — zones, délais, transporteur"),
    ("Heure limite pour une livraison le jour même",
     "l'heure de coupure au-delà de laquelle la commande bascule au lendemain"),
    ("Jours de livraison",
     "dimanche et jours fériés compris ou non, et à quel supplément"),
    ("Frais de livraison par zone",
     "au moins deux zones : la ville et sa périphérie"),
    ("Créneaux horaires proposés",
     "matin, après-midi, ou une heure précise pour le deuil"),
    ("Délai de commande pour le deuil",
     "combien d'heures avant la cérémonie la commande reste acceptable"),
    ("Politique en cas d'absence du destinataire",
     "voisin, gardien, dépôt, nouvelle présentation — et qui paie la seconde"),
    ("Durée de la garantie de fraîcheur",
     "le nombre de jours pendant lesquels un bouquet abîmé est remplacé"),
]

FAQ = [
    ("Le bouquet livré sera-t-il exactement celui de la photo ?",
     "<p><b>Non, et aucun fleuriste sérieux ne vous promettra le contraire.</b> La fleur "
     "est un produit vivant et saisonnier : ce qui arrive au marché le matin n'est pas ce "
     "qui arrivera dans trois semaines. Quand une variété manque, elle est remplacée par "
     "une tige de valeur et de tenue équivalentes, dans la même gamme de couleurs.</p>"
     "<p>Ce qui est garanti, c'est la gamme de couleurs, la taille, et la valeur. Ce qui "
     "ne l'est pas, c'est la liste exacte des variétés. Nous l'écrivons ici, sur la fiche "
     "produit, plutôt que dans les conditions générales — parce que c'est là qu'on le lit "
     "avant d'acheter, pas après.</p>"),

    ("Jusqu'à quelle heure puis-je commander pour une livraison aujourd'hui ?",
     "<p>Une heure limite existe et elle est affichée sur la page Livraison. Passé cette "
     "heure, la commande bascule automatiquement au jour suivant et vous le voyez avant "
     "de payer, pas après.</p>"
     "<p>Cette heure n'est pas encore renseignée sur cette maquette : elle dépend de "
     "l'organisation de l'atelier et des zones desservies.</p>"),

    ("Où livrez-vous ?",
     "<p>Les zones desservies et leurs frais figurent sur la page Livraison. Elles ne "
     "sont pas encore renseignées ici : ce sont des décisions commerciales, pas des "
     "données que je peux aller chercher.</p>"),

    ("Que se passe-t-il si personne n'est là à la livraison ?",
     "<p>C'est la question la plus fréquente et celle qui produit le plus de litiges. "
     "Trois solutions existent — remise à un voisin ou à un gardien, dépôt dans un lieu "
     "sûr, ou nouvelle présentation — et elles n'ont pas le même coût.</p>"
     "<p>La règle retenue sera écrite sur la page Livraison, en clair, avec la mention de "
     "qui paie une seconde présentation. Une règle floue sur ce point se paie en "
     "remboursements.</p>"),

    ("Combien de temps les fleurs tiennent-elles ?",
     "<p>Une semaine environ pour un bouquet coupé, à condition de recouper les tiges en "
     "biseau tous les deux jours, de changer l'eau aussi souvent, et de tenir le vase "
     "loin d'une source de chaleur et d'une corbeille de fruits — l'éthylène des fruits "
     "fait vieillir les fleurs plus vite.</p>"
     "<p>Une plante fleurie tient des mois. C'est pourquoi elle est souvent le meilleur "
     "choix pour un bureau.</p>"),

    ("Puis-je joindre un message ?",
     "<p>Oui. Une carte est comprise avec chaque commande, écrite à la main. Le texte se "
     "saisit à l'étape de commande, et il est relu tel quel — ponctuation et retours à la "
     "ligne compris.</p>"),

    ("Comment se passe une commande pour des obsèques ?",
     "<p>Par un parcours distinct, parce que la contrainte n'est pas la même. Il ne s'agit "
     "pas de livrer dans la journée à une personne, mais d'arriver <b>avant une heure "
     "précise</b>, dans un lieu — funérarium, lieu de culte, cimetière — qui a ses propres "
     "horaires d'accès.</p>"
     "<p>Le formulaire demande donc la date ET l'heure de la cérémonie, le lieu exact, le "
     "nom du défunt pour l'accueil, et le texte du ruban. Une commande de deuil n'est pas "
     "rattrapable le lendemain : le délai minimum est indiqué avant la validation.</p>"),

    ("Puis-je annuler ou modifier ma commande ?",
     "<p>Tant que le bouquet n'est pas monté, oui. Une fois composé, non : il est fait à "
     "la main pour un destinataire et ne se remet pas en vente.</p>"
     "<p>Le délai exact d'annulation dépend de l'heure limite retenue par l'atelier. Il "
     "sera affiché sur la page Livraison, et c'est une information à donner avant le "
     "paiement — pas dans un courriel de confirmation.</p>"),
]
