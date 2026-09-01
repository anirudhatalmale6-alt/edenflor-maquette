# -*- coding: utf-8 -*-
"""
EdenFlor — illustrations generees.

POURQUOI DES ILLUSTRATIONS ET PAS DES PHOTOS.

Un site de fleuriste se vend a la photo, et c'est justement le probleme : je
n'ai aucune photo dont EdenFlor detienne les droits. Prendre des images de
banque ou, pire, celles d'un concurrent, mettrait sur son domaine des visuels
qu'il n'a pas le droit d'exploiter — et personne ne s'en apercevrait avant la
mise en demeure. Le meme raisonnement que sur Amarimmo : on illustre, on ne
maquille pas.

Ces bouquets sont donc des compositions vectorielles, generees ici, libres de
tout droit. Ils tiennent la maquette debout et se remplacent par ses vraies
photos quand il les envoie — c'est un changement de fichier, pas de gabarit.

Graines fixes : deux executions produisent des fichiers identiques, donc
regenerer ne bouscule jamais un visuel deja valide.
"""
import math
import os
import random

W, H = 900, 675
_ICI = os.path.dirname(os.path.abspath(__file__))
# Dans le dossier de travail les scripts sont a cote des pages ; dans le paquet
# livre ils sont dans source/, un cran plus bas. Sans ce reglage, « cd source &&
# python3 gen_visuals.py » ecrirait dans source/assets/ et les pages livrees
# continueraient d'afficher les anciens visuels sans que rien ne le signale.
RACINE = os.path.dirname(_ICI) if os.path.basename(_ICI) == "source" else _ICI
OUT = os.path.join(RACINE, "assets")
os.makedirs(OUT, exist_ok=True)


class Palette:
    def __init__(self, fond, papier, tige, feuille, fleurs, coeur):
        self.fond, self.papier, self.tige = fond, papier, tige
        self.feuille, self.fleurs, self.coeur = feuille, fleurs, coeur


PALETTES = {
    # Un fleuriste change de gamme avec la saison et avec l'occasion. Cinq
    # gammes, pas une seule declinee : deux bouquets cote a cote doivent se
    # distinguer au premier coup d'oeil dans une grille de catalogue.
    "poudre":   Palette("#F6EFEA", "#E7D7CB", "#5C7A5E", "#4E6B50",
                        ["#E3A9A2", "#EFC7C1", "#D98C86", "#F3DCD6"], "#C97F62"),
    "champs":   Palette("#F4F2E7", "#DCD4BE", "#65784C", "#54663F",
                        ["#E8C55B", "#F2DE9A", "#D9A93F", "#FBF0CE"], "#A8752B"),
    "nuit":     Palette("#EEEFF2", "#CFD3DA", "#4A6152", "#3C5144",
                        ["#7E6C9B", "#A491BE", "#5D4E78", "#C9BEDA"], "#3F3457"),
    "blanc":    Palette("#F3F4F1", "#DDDED8", "#5B7358", "#4A6047",
                        ["#FFFFFF", "#F1F3EC", "#E6E9DE", "#FAFBF6"], "#D6C68A"),
    "corail":   Palette("#FBF0E8", "#E8CFB8", "#5E7A57", "#4C6547",
                        ["#E8724C", "#F19A72", "#CF5636", "#F7C4A6"], "#8E3B22"),
}


def _grain(uid):
    return (f'<filter id="g{uid}"><feTurbulence type="fractalNoise" baseFrequency="0.85" '
            f'numOctaves="3" seed="{uid}"/>'
            f'<feColorMatrix type="saturate" values="0"/>'
            f'<feComponentTransfer><feFuncA type="linear" slope="0.055"/></feComponentTransfer>'
            f'</filter>')


def _fleur(rnd, cx, cy, r, pal, penche):
    """Une fleur = une couronne de petales + un coeur. Pas de degrade : a cette
    taille il devient une tache grise a l'impression comme a l'ecran."""
    s = []
    n = rnd.choice([5, 5, 6, 8])
    teinte = rnd.choice(pal.fleurs)
    depart = rnd.uniform(0, math.tau)
    for i in range(n):
        a = depart + i * math.tau / n
        px = cx + math.cos(a) * r * 0.56
        py = cy + math.sin(a) * r * 0.56
        rot = math.degrees(a) + penche
        s.append(f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="{r*0.54:.1f}" ry="{r*0.34:.1f}" '
                 f'fill="{teinte}" transform="rotate({rot:.1f} {px:.1f} {py:.1f})" opacity=".95"/>')
    s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r*0.29:.1f}" fill="{pal.coeur}"/>')
    return "".join(s)


def _bouton(rnd, cx, cy, r, pal):
    teinte = rnd.choice(pal.fleurs)
    return (f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{r*0.42:.1f}" ry="{r*0.62:.1f}" '
            f'fill="{teinte}" opacity=".92"/>')


def _feuille(cx, cy, longueur, angle, couleur):
    a = math.radians(angle)
    x2 = cx + math.cos(a) * longueur
    y2 = cy + math.sin(a) * longueur
    mx = cx + math.cos(a) * longueur * 0.5
    my = cy + math.sin(a) * longueur * 0.5
    d = longueur * 0.24
    px, py = mx - math.sin(a) * d, my + math.cos(a) * d
    qx, qy = mx + math.sin(a) * d, my - math.cos(a) * d
    return (f'<path d="M{cx:.1f},{cy:.1f} Q{px:.1f},{py:.1f} {x2:.1f},{y2:.1f} '
            f'Q{qx:.1f},{qy:.1f} {cx:.1f},{cy:.1f}Z" fill="{couleur}" opacity=".9"/>')


def scene(nom, gamme, forme, graine, alt, format_="carte"):
    """forme  : 'bouquet' (papier kraft), 'vase', 'couronne' (deuil), 'plante'.
    format_ : 'carte' (4:3, vignette de catalogue) ou 'banniere'.

    Le format 'banniere' n'est pas la vignette etiree. Sur une banniere, le
    texte occupe la gauche : une composition centree se retrouve DERRIERE le
    titre, et il faut alors assombrir l'image au point d'effacer les fleurs.
    Constate sur la premiere capture de l'accueil. La banniere decale donc le
    bouquet vers la droite et laisse la gauche libre pour le texte.
    """
    rnd = random.Random(graine)
    pal = PALETTES[gamme]
    uid = graine
    w, h = (1800, 780) if format_ == "banniere" else (W, H)
    ancre = 0.685 if format_ == "banniere" else 0.5
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
         f'width="{w}" height="{h}" role="img" aria-label="{alt}">',
         f'<defs>{_grain(uid)}</defs>',
         f'<rect width="{w}" height="{h}" fill="{pal.fond}"/>']

    W_, H_ = w, h

    # halo : centre optique de la composition
    s.append(f'<circle cx="{w*ancre:.0f}" cy="{h*0.44:.0f}" r="{h*0.42:.0f}" '
             f'fill="#FFFFFF" opacity=".45"/>')

    cx, base = w * ancre, h * 0.80

    if forme == "couronne":
        # Couronne de deuil : anneau de feuillage et de fleurs, pas de papier.
        # Une couronne n'est pas un bouquet retourne, et la confondre sur une
        # page de deuil serait la faute la plus visible du site.
        R = h * 0.29
        s.append(f'<circle cx="{cx:.0f}" cy="{H*0.46:.0f}" r="{R:.0f}" fill="none" '
                 f'stroke="{pal.feuille}" stroke-width="{R*0.30:.0f}" opacity=".55"/>')
        # Le feuillage de la couronne doit se DETACHER de l'anneau, sinon
        # l'anneau se lit comme un simple trait vert : premiere version faite,
        # premiere version jetee apres l'avoir regardee a l'ecran.
        for i in range(40):
            a = i * math.tau / 40 + rnd.uniform(-0.06, 0.06)
            rr = R + rnd.uniform(-R * 0.13, R * 0.13)
            fx = cx + math.cos(a) * rr
            fy = h * 0.46 + math.sin(a) * rr
            s.append(_feuille(fx, fy, R * (0.30 + rnd.random() * 0.22),
                              math.degrees(a) + rnd.choice([76, 104]), pal.feuille))
        for i in range(13):
            a = i * math.tau / 13 + 0.3
            fx = cx + math.cos(a) * R
            fy = h * 0.46 + math.sin(a) * R
            s.append(_fleur(rnd, fx, fy, rnd.uniform(23, 32), pal, rnd.uniform(-20, 20)))
        s.append(f'<rect width="{w}" height="{h}" filter="url(#g{uid})" opacity=".55"/>')
        s.append("</svg>")
        chemin = os.path.join(OUT, nom + ".svg")
        open(chemin, "w", encoding="utf-8").write("".join(s))
        return chemin

    if forme == "vase":
        s.append(f'<path d="M{cx-62:.0f},{base-8:.0f} L{cx-46:.0f},{base+118:.0f} '
                 f'L{cx+46:.0f},{base+118:.0f} L{cx+62:.0f},{base-8:.0f}Z" '
                 f'fill="{pal.papier}" opacity=".92"/>')
        s.append(f'<rect x="{cx-62:.0f}" y="{base-14:.0f}" width="124" height="12" rx="4" '
                 f'fill="{pal.papier}"/>')
    elif forme == "plante":
        s.append(f'<path d="M{cx-70:.0f},{base+6:.0f} L{cx-54:.0f},{base+126:.0f} '
                 f'L{cx+54:.0f},{base+126:.0f} L{cx+70:.0f},{base+6:.0f}Z" '
                 f'fill="{pal.coeur}" opacity=".55"/>')
        s.append(f'<rect x="{cx-78:.0f}" y="{base-12:.0f}" width="156" height="22" rx="5" '
                 f'fill="{pal.coeur}" opacity=".7"/>')
    else:
        # cone de papier
        s.append(f'<path d="M{cx-150:.0f},{base-96:.0f} L{cx:.0f},{base+128:.0f} '
                 f'L{cx+150:.0f},{base-96:.0f} Z" fill="{pal.papier}" opacity=".95"/>')
        s.append(f'<path d="M{cx-150:.0f},{base-96:.0f} L{cx:.0f},{base+128:.0f} '
                 f'L{cx-16:.0f},{base-96:.0f} Z" fill="#000000" opacity=".07"/>')
        s.append(f'<rect x="{cx-58:.0f}" y="{base+22:.0f}" width="116" height="13" rx="6" '
                 f'fill="{pal.tige}" opacity=".8"/>')

    # tiges + feuillage, puis fleurs par-dessus
    n = rnd.randint(13, 17)
    tetes = []
    for i in range(n):
        etale = (i / max(1, n - 1) - 0.5) * 2
        tx = cx + etale * rnd.uniform(120, 210)
        ty = h * 0.31 + abs(etale) * rnd.uniform(28, 74) + rnd.uniform(-18, 18)
        ctrl = cx + etale * 50
        s.append(f'<path d="M{cx:.0f},{base:.0f} Q{ctrl:.0f},{(base+ty)/2:.0f} {tx:.1f},{ty:.1f}" '
                 f'fill="none" stroke="{pal.tige}" stroke-width="3.4" stroke-linecap="round" '
                 f'opacity=".85"/>')
        tetes.append((tx, ty, etale))

    # Le feuillage etait trop petit et trop clair : sur la premiere planche il
    # disparaissait derriere les tiges et le bouquet paraissait maigre. On le
    # rend plus grand, plus nombreux, et on le pose AVANT les fleurs pour qu'il
    # remplisse les vides sans passer devant.
    for i in range(rnd.randint(14, 19)):
        etale = rnd.uniform(-1, 1)
        fx = cx + etale * rnd.uniform(60, 185)
        fy = h * 0.41 + rnd.uniform(-45, 100)
        s.append(_feuille(fx, fy, rnd.uniform(74, 132),
                          rnd.uniform(-175, -5), pal.feuille))

    for tx, ty, etale in tetes:
        r = rnd.uniform(26, 44) * (1 - abs(etale) * 0.22)
        if rnd.random() < 0.24:
            s.append(_bouton(rnd, tx, ty, r, pal))
        else:
            s.append(_fleur(rnd, tx, ty, r, pal, rnd.uniform(-25, 25)))

    s.append(f'<rect width="{w}" height="{h}" filter="url(#g{uid})" opacity=".55"/>')
    s.append("</svg>")

    chemin = os.path.join(OUT, nom + ".svg")
    open(chemin, "w", encoding="utf-8").write("".join(s))
    return chemin


SCENES = [
    ("hero",            "poudre",  "bouquet",   1001, "Bouquet EdenFlor", "banniere"),
    ("hero-boutique",   "champs",  "bouquet",   1002, "Selection de bouquets EdenFlor", "banniere"),
    ("b-tendresse",     "poudre",  "bouquet",   1011, "Bouquet aux tons poudres"),
    ("b-soleil",        "champs",  "bouquet",   1012, "Bouquet aux tons jaunes"),
    ("b-crepuscule",    "nuit",    "bouquet",   1013, "Bouquet aux tons violets"),
    ("b-neige",         "blanc",   "bouquet",   1014, "Bouquet blanc"),
    ("b-brasier",       "corail",  "bouquet",   1015, "Bouquet aux tons corail"),
    ("b-jardin",        "champs",  "vase",      1016, "Composition en vase"),
    ("b-atelier",       "poudre",  "vase",      1017, "Composition en vase, tons poudres"),
    ("b-verdure",       "blanc",   "plante",    1018, "Plante en pot"),
    ("d-couronne",      "blanc",   "couronne",  1021, "Couronne de deuil"),
    ("d-gerbe",         "nuit",    "bouquet",   1022, "Gerbe de deuil"),
    ("abo-1",           "champs",  "vase",      1031, "Abonnement fleurs, gamme de saison"),
    ("evt-1",           "blanc",   "bouquet",   1041, "Composition evenementielle"),
]

if __name__ == "__main__":
    for a in SCENES:
        p = scene(*a)
        print("  ", os.path.basename(p), f"{os.path.getsize(p)//1024} KB")
    print(f"{len(SCENES)} visuels -> {OUT}")
