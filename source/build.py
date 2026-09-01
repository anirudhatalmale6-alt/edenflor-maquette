# -*- coding: utf-8 -*-
"""
EdenFlor — construit les cinq pages de la maquette.

Le gabarit (en-tête, pied de page, panier, bandeau) est écrit UNE SEULE FOIS
ici. C'est ce qui évite que cinq pages divergent à la première correction —
même règle que sur Amarimmo, et pour la même raison.

Pages :
  index.html      accueil
  boutique.html   catalogue, avec filtres par occasion
  bouquet.html    une fiche produit complète, avec l'avertissement de
                  substitution AU-DESSUS du bouton d'achat
  deuil.html      parcours distinct : date ET heure, lieu, ruban
  livraison.html  zones, délais, absence, fraîcheur — valeurs à définir
"""
import html
import os
import re

from contenu import BOUQUETS, DEUIL, OCCASIONS, LIVRAISON, FAQ

_ICI = os.path.dirname(os.path.abspath(__file__))
# Meme raison que dans gen_visuals.py : dans le paquet livre les scripts sont
# dans source/ et les pages un cran au-dessus.
HERE = os.path.dirname(_ICI) if os.path.basename(_ICI) == "source" else _ICI
VERSION_CSS = 4

MARK = ('<svg class="mk" viewBox="0 0 32 32" fill="none" aria-hidden="true">'
        '<path d="M16 29V15" stroke="#3E5C46" stroke-width="2.1" stroke-linecap="round"/>'
        '<path d="M16 15c0-4 3-7 7-7 0 4-3 7-7 7Z" fill="#3E5C46"/>'
        '<path d="M16 19c0-4-3-7-7-7 0 4 3 7 7 7Z" fill="#7E9A84"/>'
        '<circle cx="16" cy="9" r="4.2" fill="#C1746B"/>'
        '</svg>')

ARROW = ('<svg class="ar" width="15" height="15" viewBox="0 0 16 16" fill="none" aria-hidden="true">'
         '<path d="M2 8h11M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.7" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')

ICONS = {
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 2"/>',
    "truck": '<path d="M3 16V6h11v10"/><path d="M14 9h3.6L21 12.4V16h-7"/>'
             '<circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    "card":  '<rect x="3" y="6" width="18" height="13" rx="2"/><path d="M3 10h18M7 15h4"/>',
    "leaf":  '<path d="M20 4C10 4 5 9 5 16c0 2 .6 3.4.6 3.4S9 12 20 10"/><path d="M4 20 20 4"/>',
    "hand":  '<path d="M8 13V5.5a1.5 1.5 0 0 1 3 0V12"/><path d="M11 11.5V4.5a1.5 1.5 0 0 1 3 0V12"/>'
             '<path d="M14 11V6.5a1.5 1.5 0 0 1 3 0V14"/>'
             '<path d="M17 12.5a1.5 1.5 0 0 1 3 0V16a6 6 0 0 1-6 6h-2a6 6 0 0 1-6-6v-3l-1.6-2.1'
             'a1.5 1.5 0 0 1 2.4-1.8L8 13"/>',
    "shield":'<path d="M12 3 20 6v6c0 4.6-3.3 7.9-8 9-4.7-1.1-8-4.4-8-9V6Z"/><path d="m9 12 2 2 4-4"/>',
}


def icon(cle):
    return (f'<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{ICONS[cle]}</svg>')


PAGES = [("index.html", "Accueil"), ("boutique.html", "Boutique"),
         ("bouquet.html", "Une fiche"), ("deuil.html", "Deuil"),
         ("livraison.html", "Livraison")]


def nav(courante):
    liens = "".join(
        f'<a href="{f}"{" aria-current=\"page\"" if f == courante else ""}>{t}</a>'
        for f, t in PAGES)
    return f'''<header class="hdr">
  <div class="wrap">
    <a class="brand" href="index.html">{MARK}<span class="nm">Eden<em>Flor</em></span></a>
    <nav class="nav" id="nav">{liens}</nav>
    <div class="tools">
      <a class="icb" href="boutique.html" aria-label="Panier, 0 article"><svg class="pan" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 7h13l-1.4 8.2a2 2 0 0 1-2 1.8H9.4a2 2 0 0 1-2-1.7L6 4H3"/><circle cx="10" cy="20" r="1.2"/><circle cx="17" cy="20" r="1.2"/></svg><span class="lab">Panier</span><span class="n">0</span></a>
    </div>
    <button class="burger" aria-label="Menu" aria-expanded="false" id="burger"><span></span><span></span><span></span></button>
  </div>
</header>'''


DEMO = '''<div class="demo" id="demo">
  <span><b>Maquette de démonstration.</b> Les visuels sont des illustrations générées, pas des photos de bouquets réels. Les prix affichés sont des exemples. Zones de livraison, délais et coordonnées restent à définir.</span>
  <button onclick="document.getElementById('demo').remove()">Masquer</button>
</div>'''

FOOT = '''<footer class="ft-main">
  <div class="wrap">
    <div class="cols">
      <div>
        <div class="brand">''' + MARK + '''<span class="nm">Eden<em>Flor</em></span></div>
        <p class="bl">Fleuriste. Bouquets composés à la main, livrés le jour même dans les zones desservies.</p>
        <ul style="margin-top:18px">
          <li class="muted" style="color:#8FA391">Coordonnées à compléter</li>
          <li><a href="index.html#contact">Formulaire de contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Boutique</h4>
        <ul>
          <li><a href="boutique.html">Tous les bouquets</a></li>
          <li><a href="boutique.html#occasions">Par occasion</a></li>
          <li><a href="bouquet.html">Exemple de fiche</a></li>
          <li><a href="deuil.html">Deuil</a></li>
        </ul>
      </div>
      <div>
        <h4>Commander</h4>
        <ul>
          <li><a href="livraison.html">Zones et délais</a></li>
          <li><a href="livraison.html#absence">En cas d'absence</a></li>
          <li><a href="livraison.html#fraicheur">Garantie de fraîcheur</a></li>
          <li><a href="index.html#faq">Questions fréquentes</a></li>
        </ul>
      </div>
      <div>
        <h4>La maison</h4>
        <ul>
          <li><a href="index.html#methode">Comment on travaille</a></li>
          <li><a href="index.html#substitution">La règle de substitution</a></li>
          <li><a href="index.html#contact">Nous écrire</a></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="wrap">
    <div class="ft-bot">
      <span>© 2026 EdenFlor. Tous droits réservés.</span>
      <span>Mentions légales · CGV · Politique de confidentialité — à rédiger</span>
    </div>
  </div>
</footer>
<script>
(function(){
  var b=document.getElementById('burger'), n=document.getElementById('nav');
  if(b&&n) b.addEventListener('click',function(){
    var o=n.classList.toggle('open');
    b.setAttribute('aria-expanded', o?'true':'false');
  });
  // Les formulaires n'ont pas d'adresse de reception : on intercepte plutot
  // que de laisser un envoi recharger la page et avoir l'air casse.
  document.querySelectorAll('form[data-demo]').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var n=f.querySelector('[data-note]');
      if(n) n.textContent="Formulaire de démonstration — non connecté. Indiquez l'adresse de réception et je le branche.";
    });
  });
  // Choix de taille sur la fiche produit : purement visuel, pas de panier.
  document.querySelectorAll('[data-opts]').forEach(function(g){
    g.querySelectorAll('.opt').forEach(function(o){
      o.addEventListener('click',function(){
        g.querySelectorAll('.opt').forEach(function(x){x.classList.remove('on')});
        o.classList.add('on');
        var p=document.getElementById('prix-choisi');
        if(p) p.textContent=o.dataset.prix;
      });
    });
  });
  // Filtres de la boutique : ils filtrent pour de vrai, cote navigateur.
  var f=document.getElementById('filtres');
  if(f){
    var cartes=[].slice.call(document.querySelectorAll('#catalogue [data-oc]'));
    var vide=document.getElementById('vide');
    f.addEventListener('click',function(e){
      var b=e.target.closest('button'); if(!b) return;
      f.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed','false')});
      b.setAttribute('aria-pressed','true');
      var oc=b.dataset.oc, n=0;
      cartes.forEach(function(c){
        var ok = !oc || c.dataset.oc.split('|').indexOf(oc)>-1;
        c.style.display = ok?'':'none';
        if(ok) n++;
      });
      if(vide) vide.hidden = n>0;
    });
  }
})();
</script>'''


def typo_fr(h):
    """Espace insécable avant la ponctuation double, comme le veut le français.

    Sans elle le navigateur peut renvoyer le signe seul en début de ligne, ce
    qui se lit comme une faute de frappe. Deux précautions, parce qu'une
    substitution globale sur du HTML casse en silence :
      - on ne touche QUE le texte, jamais l'intérieur d'une balise ;
      - on saute <script> et <style>, où un « ; » collé à un insécable serait
        du code invalide.
    """
    morceaux = re.split(r'(<[^>]*>)', h)
    dans_code = False
    for i, m in enumerate(morceaux):
        if i % 2:
            b = m.lower()
            if b.startswith(('<script', '<style')):
                dans_code = True
            elif b.startswith(('</script', '</style')):
                dans_code = False
            continue
        if dans_code or not m:
            continue
        m = re.sub(r' ([;!?»])', ' \\1', m)
        m = re.sub(r' (:)', ' \\1', m)
        m = m.replace('« ', '« ')
        morceaux[i] = m
    return "".join(morceaux)


def page(titre, desc, corps, courante):
    return typo_fr(f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(titre)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(titre)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="assets/site.css?v={VERSION_CSS}">
</head>
<body>
{DEMO}
{nav(courante)}
{corps}
{FOOT}
</body>
</html>''')


def carte(b):
    _id, img, nom, gamme, occasions, desc, tailles = b
    oc = "".join(f"<li>{html.escape(o)}</li>" for o in occasions)
    px = tailles[0][1]
    depuis = (f'<span class="px">dès {px}&nbsp;€<span class="ex">exemple</span></span>'
              if px != "à définir" else '<span class="px"><span class="tbd">prix à définir</span></span>')
    return f'''<article class="pc" data-oc="{html.escape('|'.join(occasions))}">
  <div class="im"><img src="assets/{img}.svg" alt="Illustration — {html.escape(nom)}" loading="lazy"><span class="tag">Illustration</span></div>
  <div class="bd">
    <span class="gam">{html.escape(gamme)}</span>
    <h3>{html.escape(nom)}</h3>
    <p>{html.escape(desc)}</p>
    <ul class="oc">{oc}</ul>
    <div class="ft">{depuis}<a href="bouquet.html">Voir la fiche {ARROW}</a></div>
  </div>
</article>'''


def faq_bloc(items):
    d = "".join(f'<details><summary>{q}</summary><div class="a">{a}</div></details>'
                for q, a in items)
    return f'<div class="faq">{d}</div>'


SUBSTITUTION = '''<div class="subst">
  <h4>Ce que nous garantissons, et ce que nous ne garantissons pas</h4>
  <p>La fleur est un produit vivant et saisonnier. Quand une variété manque à l'arrivage, elle est remplacée par une tige de valeur et de tenue équivalentes, dans la même gamme de couleurs.</p>
  <p><b>Garanti :</b> la gamme de couleurs, la taille, la valeur. <b>Non garanti :</b> la liste exacte des variétés. Nous l'écrivons ici plutôt que dans les conditions générales, parce que c'est ici qu'on le lit avant d'acheter.</p>
</div>'''


# ============================ ACCUEIL =======================================
cartes_accueil = "".join(carte(b) for b in BOUQUETS[:4])
occ_liste = "".join(
    f'<div class="box"><h3>{html.escape(n)}</h3><p>{html.escape(d)}</p></div>'
    for n, d in OCCASIONS)

index_body = f'''
<div class="hero">
  <img src="assets/hero.svg" alt="Illustration d'un bouquet EdenFlor">
  <div class="wrap">
    <div class="eyebrow">Fleuriste</div>
    <h1>Des fleurs qui arrivent au bon moment.</h1>
    <p class="sub">Bouquets composés à la main, le jour de la commande. Nous disons aussi ce que la plupart des sites cachent : le bouquet livré ne sera pas exactement celui de la photo, et voilà pourquoi.</p>
    <div class="cta">
      <a class="btn btn-b" href="boutique.html">Voir les bouquets {ARROW}</a>
      <a class="btn btn-g" href="#substitution">Pourquoi pas exactement la photo</a>
    </div>
  </div>
</div>

<div class="strip">
  <div class="wrap">
    <div><div class="k">Composition</div><div class="v">À la main, le jour même</div></div>
    <div><div class="k">Livraison</div><div class="v"><span class="tbd">zones à définir</span></div></div>
    <div><div class="k">Carte</div><div class="v">Écrite à la main, comprise</div></div>
    <div><div class="k">Deuil</div><div class="v">Parcours distinct, à l'heure</div></div>
  </div>
</div>

<section id="selection">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">La sélection</div>
      <h2>Quatre gammes, et huit au catalogue.</h2>
      <p class="lede" style="margin-top:16px">Chaque gamme est une famille de couleurs, pas une liste figée de variétés. C'est ce qui permet de composer avec ce qui est beau le matin même plutôt qu'avec ce qui figurait sur une photo prise l'an dernier.</p>
    </div>
    <div class="grid g4">{cartes_accueil}</div>
    <p class="note">Illustrations générées, libres de droits, en attendant tes photos. Les prix sont des exemples.</p>
    <div style="margin-top:30px"><a class="btn btn-o" href="boutique.html">Tout le catalogue {ARROW}</a></div>
  </div>
</section>

<section class="cream" id="substitution">
  <div class="wrap">
    <div class="split" style="align-items:center">
      <div>
        <div class="eyebrow">La règle qu'on écrit en grand</div>
        <h2>Le bouquet livré n'est jamais exactement celui de la photo.</h2>
        <p class="lede" style="margin-top:16px">C'est vrai chez tous les fleuristes du monde, et la plupart des sites le rangent en petits caractères dans les conditions générales. Le résultat est connu : un client qui découvre la clause après coup, un jour d'anniversaire, et un litige que personne ne gagne.</p>
        <p class="lede" style="margin-top:14px">Nous le mettons <b>sur la fiche produit, au-dessus du bouton d'achat</b>. Dit une fois, avant le paiement, ça se lit comme du sérieux. Dit après, ça se lit comme une excuse.</p>
      </div>
      <div>
        <div class="fc" style="margin-bottom:16px">
          {icon("leaf")}
          <h3>Ce qui est garanti</h3>
          <p>La gamme de couleurs, la taille commandée, et la valeur du bouquet. Une tige remplacée l'est par une tige de valeur et de tenue équivalentes.</p>
        </div>
        <div class="fc">
          {icon("shield")}
          <h3>Ce qui ne l'est pas</h3>
          <p>La liste exacte des variétés. L'arrivage du jour décide, et c'est précisément ce qui fait la différence entre un bouquet de fleuriste et un bouquet de supermarché.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="occasions">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Les occasions</div>
      <h2>Huit occasions, et deux qui ne se traitent pas comme les autres.</h2>
      <p class="lede" style="margin-top:16px">Le mariage se fait sur devis, pas en ligne. Le deuil a son propre parcours : il ne s'agit pas de livrer dans la journée à une personne, mais d'arriver avant une heure précise, dans un lieu qui a ses horaires.</p>
    </div>
    <div class="grid g4">{occ_liste}</div>
  </div>
</section>

<section class="cream" id="methode">
  <div class="wrap">
    <div class="head"><div class="eyebrow">Comment on travaille</div><h2>Quatre points, et aucun n'est décoratif.</h2></div>
    <div class="grid g4">
      <div class="fc">{icon("clock")}<h3>Composé le jour de la livraison</h3><p>Pas la veille, pas en série. Un bouquet monté trop tôt perd deux jours de tenue chez le destinataire.</p></div>
      <div class="fc">{icon("truck")}<h3>Livré par nos soins</h3><p>Pas par un transporteur de colis. Une fleur ne voyage pas comme une paire de chaussures et ne passe pas la nuit dans un entrepôt.</p></div>
      <div class="fc">{icon("card")}<h3>La carte est écrite à la main</h3><p>Le texte est repris tel quel — ponctuation et retours à la ligne compris. C'est souvent ce qui compte le plus dans l'envoi.</p></div>
      <div class="fc">{icon("hand")}<h3>On dit non quand il le faut</h3><p>Si le délai ne permet pas d'arriver à l'heure pour des obsèques, on le dit avant la commande. Une commande de deuil ne se rattrape pas le lendemain.</p></div>
    </div>
  </div>
</section>

<section id="faq">
  <div class="wrap">
    <div class="head"><div class="eyebrow">Questions fréquentes</div><h2>Ce qu'on nous demande le plus.</h2></div>
    {faq_bloc(FAQ)}
  </div>
</section>

<section class="cream" id="contact">
  <div class="wrap">
    <div class="split">
      <div>
        <div class="eyebrow">Contact</div>
        <h2>Une demande particulière ?</h2>
        <p class="lede" style="margin-top:16px">Mariage, réception, abonnement hebdomadaire pour un bureau : ces demandes se traitent de vive voix, pas par un bouton d'achat. Dites-nous la date, le lieu et l'ambiance recherchée.</p>
        <p class="lede" style="margin-top:14px muted">Le formulaire n'a pas encore d'adresse de réception : indique-la et je le branche.</p>
      </div>
      <form class="form" data-demo>
        <div class="champ"><label>Nom</label><input type="text" autocomplete="name"></div>
        <div class="champ"><label>Téléphone</label><input type="tel" autocomplete="tel"></div>
        <div class="champ plein"><label>Type de demande</label>
          <select><option>Mariage</option><option>Réception ou entreprise</option><option>Abonnement</option><option>Deuil</option><option>Autre</option></select></div>
        <div class="champ plein"><label>Votre message</label><textarea></textarea></div>
        <div class="plein"><button class="btn btn-p wide" type="submit">Envoyer</button></div>
        <p class="note" data-note>Nous répondons dans la journée aux demandes reçues avant l'heure limite.</p>
      </form>
    </div>
  </div>
</section>
'''

# ============================ BOUTIQUE ======================================
cartes_toutes = "".join(carte(b) for b in BOUQUETS)
noms_occasions = []
for b in BOUQUETS:
    for o in b[4]:
        if o not in noms_occasions:
            noms_occasions.append(o)
boutons = ('<button data-oc="" aria-pressed="true">Tout</button>'
           + "".join(f'<button data-oc="{html.escape(o)}" aria-pressed="false">{html.escape(o)}</button>'
                     for o in noms_occasions))

boutique_body = f'''
<div class="hero" style="min-height:min(46vh,420px)">
  <img src="assets/hero-boutique.svg" alt="Illustration — sélection EdenFlor">
  <div class="wrap">
    <div class="eyebrow">Boutique</div>
    <h1>Le catalogue.</h1>
    <p class="sub">Huit gammes de bouquets, deux compositions en vase, une plante fleurie. Filtre par occasion ci-dessous.</p>
  </div>
</div>

<section id="occasions">
  <div class="wrap">
    <div class="filtres" id="filtres">{boutons}</div>
    <div class="grid g4" id="catalogue">{cartes_toutes}</div>
    <p class="vide" id="vide" hidden>Aucun bouquet dans cette occasion pour le moment.</p>
    <p class="note">Les filtres fonctionnent réellement — ils s'appliquent dans le navigateur, sans recharger la page. Les illustrations sont générées, les prix sont des exemples.</p>
  </div>
</section>

<section class="cream" id="devis">
  <div class="wrap">
    <div class="head">
      <div class="eyebrow">Sur devis</div>
      <h2>Deux demandes qui ne passent pas par le panier.</h2>
      <p class="lede" style="margin-top:16px">L'abonnement et l'événementiel se chiffrent après une conversation, pas avant. Un bouton d'achat sur ces deux-là donnerait un prix faux dans les deux sens.</p>
    </div>
    <div class="grid g2">
      <article class="pc">
        <div class="im"><img src="assets/abo-1.svg" alt="Illustration — abonnement fleurs" loading="lazy"><span class="tag">Illustration</span></div>
        <div class="bd">
          <span class="gam">Abonnement</span>
          <h3>Des fleurs chaque semaine</h3>
          <p>Pour un accueil, une salle d'attente, une table. La gamme suit la saison plutôt qu'un catalogue fixe : c'est ce qui permet de tenir un budget constant toute l'année.</p>
          <div class="ft"><span class="px"><span class="tbd">fréquence et tarif à définir</span></span><a href="index.html#contact">Nous écrire {ARROW}</a></div>
        </div>
      </article>
      <article class="pc">
        <div class="im"><img src="assets/evt-1.svg" alt="Illustration — composition événementielle" loading="lazy"><span class="tag">Illustration</span></div>
        <div class="bd">
          <span class="gam">Événement</span>
          <h3>Mariage, réception, inauguration</h3>
          <p>Cérémonie, tables, entrée. La date, le lieu et le nombre de tables changent tout : ça se prépare des semaines à l'avance, et ça se voit sur place.</p>
          <div class="ft"><span class="px"><span class="tbd">sur devis</span></span><a href="index.html#contact">Nous écrire {ARROW}</a></div>
        </div>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="split" style="align-items:center">
      <div>
        <div class="eyebrow">Avant de commander</div>
        <h2>Deux choses à savoir.</h2>
        <p class="lede" style="margin-top:16px">La première : le bouquet livré n'est pas exactement celui de l'illustration, et c'est expliqué sur chaque fiche. La seconde : pour des obsèques, ce n'est pas ce catalogue qu'il faut, mais le parcours dédié — il demande l'heure de la cérémonie et le lieu.</p>
        <div class="cta" style="display:flex;gap:12px;margin-top:26px;flex-wrap:wrap">
          <a class="btn btn-o" href="index.html#substitution">La règle de substitution</a>
          <a class="btn btn-p" href="deuil.html">Commande pour obsèques {ARROW}</a>
        </div>
      </div>
      <div>{SUBSTITUTION}</div>
    </div>
  </div>
</section>
'''

# ============================ FICHE PRODUIT =================================
_id, img, nom, gamme, occasions, desc, tailles = BOUQUETS[0]
opts = "".join(
    f'<div class="opt{" on" if i == 1 else ""}" data-prix="{p}&nbsp;€">'
    f'<div><div class="t">{html.escape(t)}</div>'
    f'<div class="d">{"une quinzaine de tiges" if t == "Petit" else "une vingtaine de tiges" if t == "Moyen" else "une trentaine de tiges"}</div></div>'
    f'<div class="p">{p}&nbsp;€</div></div>'
    for i, (t, p) in enumerate(tailles))

fiche_body = f'''
<section>
  <div class="wrap">
    <p class="muted" style="font-size:.9rem;margin-bottom:22px"><a href="boutique.html">Boutique</a> &nbsp;/&nbsp; {html.escape(nom)}</p>
    <div class="fiche">
      <div class="visu"><img src="assets/{img}.svg" alt="Illustration — {html.escape(nom)}"></div>
      <div>
        <div class="eyebrow">{html.escape(gamme)}</div>
        <h1 style="font-size:clamp(2rem,3.6vw,2.9rem)">{html.escape(nom)}</h1>
        <p class="lede" style="margin-top:16px">{html.escape(desc)}</p>

        <div style="margin-top:26px;font:600 12px/1 var(--sans);letter-spacing:.13em;text-transform:uppercase;color:var(--ink-3)">Taille</div>
        <div class="opts" data-opts>{opts}</div>
        <p class="muted" style="font-size:.86rem;margin-top:10px">Prix d'exemple. À remplacer par ta grille réelle.</p>

        <div class="champ"><label>Date de livraison souhaitée</label><input type="date"></div>
        <div class="champ"><label>Créneau</label>
          <select><option>Matin</option><option>Après-midi</option><option>Peu importe</option></select></div>
        <div class="champ"><label>Message sur la carte</label>
          <textarea placeholder="Le texte est recopié à la main, tel quel."></textarea></div>

        {SUBSTITUTION}

        <div style="display:flex;align-items:center;gap:16px;margin-top:22px;flex-wrap:wrap">
          <span style="font:600 22px/1 var(--serif)" id="prix-choisi">{tailles[1][1]}&nbsp;€</span>
          <a class="btn btn-b" href="#" onclick="return false">Ajouter au panier {ARROW}</a>
        </div>
        <p class="note">Le panier n'est pas connecté sur cette maquette : c'est une démonstration d'interface, pas une boutique en service.</p>
      </div>
    </div>
  </div>
</section>

<section class="cream">
  <div class="wrap">
    <div class="head"><div class="eyebrow">Entretien</div><h2>Le faire tenir une semaine.</h2></div>
    <div class="grid g4">
      <div class="fc">{icon("leaf")}<h3>Recouper en biseau</h3><p>Deux centimètres, tous les deux jours. Une tige coupée à plat contre le fond du vase ne boit plus.</p></div>
      <div class="fc">{icon("clock")}<h3>Changer l'eau</h3><p>Tous les deux jours aussi, et rincer le vase. C'est la bactérie dans l'eau qui tue le bouquet, pas le manque d'eau.</p></div>
      <div class="fc">{icon("shield")}<h3>Loin de la chaleur</h3><p>Pas au-dessus d'un radiateur ni en plein soleil derrière une vitre.</p></div>
      <div class="fc">{icon("hand")}<h3>Loin de la corbeille de fruits</h3><p>Les fruits dégagent de l'éthylène, qui fait vieillir les fleurs beaucoup plus vite. Détail méconnu, effet très visible.</p></div>
    </div>
  </div>
</section>
'''

# ============================ DEUIL =========================================
cartes_deuil = "".join(
    f'''<article class="pc">
  <div class="im"><img src="assets/{img}.svg" alt="Illustration — {html.escape(nom)}" loading="lazy"><span class="tag">Illustration</span></div>
  <div class="bd">
    <h3>{html.escape(nom)}</h3>
    <p>{html.escape(desc)}</p>
    <div class="ft"><span class="px"><span class="tbd">prix à définir</span></span></div>
  </div>
</article>''' for _i, img, nom, desc, _t in DEUIL)

deuil_body = f'''
<section>
  <div class="wrap">
    <div class="head" style="max-width:64ch">
      <div class="eyebrow">Obsèques</div>
      <h2>Une commande de deuil ne se traite pas comme les autres.</h2>
      <p class="lede" style="margin-top:16px">Il ne s'agit pas de livrer dans la journée à une personne, mais d'arriver <b>avant une heure précise</b>, dans un lieu — funérarium, lieu de culte, cimetière — qui a ses propres horaires d'accès. Et il n'y a pas de seconde chance le lendemain.</p>
      <p class="lede" style="margin-top:14px">C'est pour ça que ce parcours est séparé du catalogue et qu'il demande d'autres informations. Si le délai ne permet pas d'être à l'heure, nous le disons avant la commande plutôt qu'après.</p>
    </div>

    <div class="grid g2" style="margin-bottom:44px">
      <div class="fc" style="border-left:4px solid var(--blush)">
        {icon("clock")}
        <h3>Ce que le formulaire demande en plus</h3>
        <p>La date <b>et l'heure</b> de la cérémonie. Le lieu exact, avec son nom. Le nom du défunt, pour que l'accueil sache où déposer. Et le texte du ruban.</p>
        <p>Un délai minimum s'applique entre la commande et la cérémonie. Il est affiché avant la validation, pas découvert après.</p>
      </div>
      <div class="fc" style="border-left:4px solid var(--blush)">
        {icon("shield")}
        <h3>Ce qu'on vérifie avant d'accepter</h3>
        <p>Que le lieu est accessible à l'heure demandée, et que la composition tient le trajet. Une couronne montée sur mousse ne voyage pas comme un bouquet dans du papier.</p>
        <p>Si l'un des deux ne tient pas, la commande est refusée et expliquée. C'est plus utile qu'un remboursement le lendemain.</p>
      </div>
    </div>

    <div class="grid g2">{cartes_deuil}</div>
    <p class="note">Les prix des compositions de deuil dépendent de la taille et du montage. Ils sont à définir avec toi — je ne les invente pas.</p>
  </div>
</section>

<section class="cream">
  <div class="wrap">
    <div class="split">
      <div>
        <div class="eyebrow">Commande</div>
        <h2>Les informations nécessaires.</h2>
        <p class="lede" style="margin-top:16px">Ce formulaire est volontairement plus long que celui du catalogue. Chaque champ correspond à une erreur possible qu'on préfère éviter.</p>
      </div>
      <form class="form" data-demo>
        <div class="champ"><label>Date de la cérémonie</label><input type="date"></div>
        <div class="champ"><label>Heure de la cérémonie</label><input type="time"></div>
        <div class="champ plein"><label>Lieu (nom et adresse)</label><input type="text" placeholder="Funérarium, lieu de culte, cimetière…"></div>
        <div class="champ plein"><label>Nom du défunt</label><input type="text"></div>
        <div class="champ plein"><label>Texte du ruban</label><input type="text" placeholder="Par exemple : À notre ami"></div>
        <div class="champ"><label>Votre nom</label><input type="text"></div>
        <div class="champ"><label>Téléphone</label><input type="tel"></div>
        <div class="plein"><button class="btn btn-p wide" type="submit">Envoyer la demande</button></div>
        <p class="note" data-note>Nous confirmons par téléphone avant de composer, y compris pour dire non si le délai ne permet pas d'être à l'heure.</p>
      </form>
    </div>
  </div>
</section>
'''

# ============================ LIVRAISON =====================================
lignes_livraison = "".join(
    f'<tr><td>{html.escape(l)}</td><td><span class="tbd">à définir</span></td>'
    f'<td>{html.escape(d)}</td></tr>' for l, d in LIVRAISON)

livraison_body = f'''
<section>
  <div class="wrap">
    <div class="head" style="max-width:64ch">
      <div class="eyebrow">Livraison</div>
      <h2>Les valeurs de cette page t'appartiennent.</h2>
      <p class="lede" style="margin-top:16px">Zones, heure limite, frais, délais : ce ne sont pas des informations que je peux aller chercher. Ce sont des décisions de ton commerce, et je n'ai même pas encore ton pays. Elles restent donc <b>visiblement vides</b> plutôt que remplies au hasard.</p>
      <p class="lede" style="margin-top:14px">Un chiffre plausible sur une page de livraison ne se signale pas tout seul : il reste affiché, il a l'air juste, et quelqu'un commande dessus.</p>
    </div>

    <div class="split" style="align-items:start">
      <div class="tbl-wrap"><table class="tbl">
        <tr><th>Ce qu'il faut décider</th><th>Valeur</th><th>Pourquoi ça compte</th></tr>
        {lignes_livraison}
      </table></div>
      <div>
        <div class="fc" style="margin-bottom:16px">
          {icon("shield")}
          <h3>« À définir » n'est pas « à vérifier »</h3>
          <p>Sur le site Amarimmo, une case vide signifie qu'une autorité publie la valeur et que personne ne l'a encore vérifiée à une date précise. <b>Ici, c'est différent :</b> il n'existe aucun barème à consulter. Ce sont tes décisions, et tant qu'elles ne sont pas prises la valeur n'existe pas.</p>
          <p>La nuance a l'air théorique. Elle ne l'est pas : marquer « à vérifier » enverrait quelqu'un chercher pendant une semaine une information que personne n'a jamais écrite.</p>
        </div>
        <div class="fc">
          {icon("clock")}
          <h3>Celle qui compte le plus</h3>
          <p>L'heure limite. C'est elle qui décide si une commande passée à 15 h arrive aujourd'hui ou demain, et c'est la première source de réclamation d'une boutique de fleurs. Elle doit être affichée <b>avant le paiement</b>, pas dans le courriel de confirmation.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="cream" id="absence">
  <div class="wrap">
    <div class="head"><div class="eyebrow">Le cas qui produit les litiges</div><h2>Personne n'est là à la livraison.</h2></div>
    <div class="grid g3">
      <div class="box"><h3>Remise à un voisin ou au gardien</h3><p>Rapide et gratuit, mais suppose l'accord du destinataire et un mot déposé dans la boîte. Ne convient pas à une surprise.</p></div>
      <div class="box"><h3>Dépôt dans un lieu sûr</h3><p>À l'abri du soleil et du gel. Un bouquet laissé deux heures derrière une vitre au soleil est perdu — c'est une fausse économie.</p></div>
      <div class="box"><h3>Nouvelle présentation</h3><p>La plus sûre, et la seule qui a un coût réel. La question à trancher n'est pas « la propose-t-on », c'est <b>qui la paie</b>.</p></div>
    </div>
    <p class="note">Ces trois options existent chez tous les fleuristes. Ce qui distingue une boutique sérieuse, c'est d'écrire laquelle s'applique et à quel prix, plutôt que de laisser le livreur décider sur le pas de la porte.</p>
  </div>
</section>

<section id="fraicheur">
  <div class="wrap">
    <div class="split" style="align-items:center">
      <div>
        <div class="eyebrow">Garantie</div>
        <h2>Ce qu'une garantie de fraîcheur veut vraiment dire.</h2>
        <p class="lede" style="margin-top:16px">Ce n'est pas « les fleurs ne fanent pas ». C'est : pendant un nombre de jours annoncé, un bouquet qui s'abîme anormalement est remplacé, sur photo, sans discussion.</p>
        <p class="lede" style="margin-top:14px">Deux conditions rendent la promesse tenable — l'entretien de base a été fait, et la photo est envoyée dans le délai. Écrites clairement, elles ne se lisent pas comme une échappatoire ; laissées floues, elles ne servent à personne.</p>
      </div>
      <div>
        <div class="fc">
          {icon("leaf")}
          <h3>Le nombre de jours reste à décider</h3>
          <p>C'est un arbitrage commercial : trop court, la garantie ne rassure pas ; trop long, elle couvre l'oubli d'arrosage. Il figure dans le tableau ci-dessus, vide, en attendant ta décision.</p>
        </div>
      </div>
    </div>
  </div>
</section>
'''

if __name__ == "__main__":
    sorties = {
        "index.html": page(
            "EdenFlor — Fleuriste, bouquets composés à la main et livrés le jour même",
            "Bouquets composés à la main le jour de la livraison. La règle de substitution "
            "expliquée avant l'achat, et un parcours distinct pour les obsèques.",
            index_body, "index.html"),
        "boutique.html": page(
            "EdenFlor — Le catalogue : bouquets, compositions en vase, plante fleurie",
            "Huit gammes de bouquets filtrables par occasion : anniversaire, amour, naissance, "
            "remerciement, félicitations, entreprise.",
            boutique_body, "boutique.html"),
        "bouquet.html": page(
            f"EdenFlor — {nom}, bouquet {gamme.lower()}",
            "Exemple de fiche produit : choix de taille, date et créneau de livraison, message "
            "sur la carte, et la règle de substitution affichée avant le bouton d'achat.",
            fiche_body, "bouquet.html"),
        "deuil.html": page(
            "EdenFlor — Fleurs de deuil : couronnes et gerbes, livrées à l'heure de la cérémonie",
            "Parcours distinct pour les obsèques : date et heure de cérémonie, lieu, nom du "
            "défunt et texte du ruban. Nous refusons une commande que le délai ne permet pas.",
            deuil_body, "deuil.html"),
        "livraison.html": page(
            "EdenFlor — Livraison : zones, heure limite, absence du destinataire, fraîcheur",
            "Les décisions de livraison à arrêter : zones desservies, heure limite, frais, "
            "conduite en cas d'absence et durée de la garantie de fraîcheur.",
            livraison_body, "livraison.html"),
    }
    for nom_fichier, contenu in sorties.items():
        chemin = os.path.join(HERE, nom_fichier)
        open(chemin, "w", encoding="utf-8").write(contenu)
        print(f"  {nom_fichier}  {len(contenu)//1024} KB")
    print(f"{len(sorties)} pages construites")
