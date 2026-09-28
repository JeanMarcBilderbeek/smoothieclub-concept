# Bouwt alle HTML-pagina's van de Smoothieclub-conceptsite.
# Gebruik: python tools/build.py  (vanuit de hoofdmap van de repo)
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHOP = "https://www.smoothieclub.nl/product/"
TEL = "06-50745730"
TEL_LINK = "tel:+31650745730"
WA = "https://wa.me/31650745730?text=Hoi%20Jean-Marc%2C%20ik%20heb%20een%20vraag%20over%20Smoothieclub"
MAIL = "info@smoothieclub.nl"

# Social-kanalen: (naam, url, svg-pad). Nieuwe kanalen hier toevoegen.
SOCIAL = [
    ("LinkedIn", "https://www.linkedin.com/company/smoothieclub/",
     "M20.4 20.5h-3.6v-5.6c0-1.3 0-3-1.8-3s-2.1 1.4-2.1 2.9v5.7H9.3V9h3.4v1.6h.1c.5-.9 1.6-1.8 3.4-1.8 3.6 0 4.3 2.4 4.3 5.5v6.2zM5.3 7.4a2.1 2.1 0 1 1 0-4.2 2.1 2.1 0 0 1 0 4.2zM7.1 20.5H3.5V9h3.6v11.5z"),
    ("Instagram", "https://www.instagram.com/smoothieclub/",
     "M12 7.2a4.8 4.8 0 1 0 0 9.6 4.8 4.8 0 0 0 0-9.6zm0 7.9a3.1 3.1 0 1 1 0-6.2 3.1 3.1 0 0 1 0 6.2zm6.1-8.1a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0zM21.9 8c-.1-1.6-.4-3-1.6-4.2S17.6 2.2 16 2.1C14.4 2 9.6 2 8 2.1 6.4 2.2 5 2.5 3.8 3.7S2.2 6.4 2.1 8C2 9.6 2 14.4 2.1 16c.1 1.6.4 3 1.6 4.2s2.6 1.5 4.2 1.6c1.6.1 6.4.1 8 0 1.6-.1 3-.4 4.2-1.6s1.5-2.6 1.6-4.2c.1-1.6.1-6.4 0-8zm-2.1 9.7a3.2 3.2 0 0 1-1.8 1.8c-1.3.5-4.3.4-5.7.4s-4.4.1-5.7-.4a3.2 3.2 0 0 1-1.8-1.8c-.5-1.3-.4-4.3-.4-5.7s-.1-4.4.4-5.7A3.2 3.2 0 0 1 6.6 4.5c1.3-.5 4.3-.4 5.7-.4s4.4-.1 5.7.4a3.2 3.2 0 0 1 1.8 1.8c.5 1.3.4 4.3.4 5.7s.1 4.4-.4 5.7z"),
    ("Facebook", "https://www.facebook.com/smoothieclub",
     "M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"),
    ("de Facebook-groep", "https://www.facebook.com/groups/493784564004776",
     "M16 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm-8 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm0 2c-2.7 0-8 1.3-8 4v3h10v-3c0-1.1.4-2.1 1.2-2.9A11 11 0 0 0 8 13zm8 0c-.3 0-.7 0-1.1.1 1.3.9 2.1 2.2 2.1 3.9v3h7v-3c0-2.7-5.3-4-8-4z"),
    ("YouTube", "https://www.youtube.com/channel/UCpndQ3--uPgfoFt1ceTe8Ew/",
     "M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.6V8.4l6.2 3.6-6.2 3.6z"),
]


def social_iconen(klasse="social"):
    return f'<ul class="{klasse}">' + "".join(
        f'<li><a href="{u}" rel="noopener" target="_blank" aria-label="Smoothieclub op {n}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="{d}"/></svg></a></li>'
        for n, u, d in SOCIAL) + "</ul>"


NAV = [
    ("workshops.html", "Workshops"),
    ("keynote.html", "Keynote"),
    ("blendbox.html", "Blendbox"),
    ("webshop.html", "Webshop"),
    ("ingredienten.html", "Ingrediënten"),
    ("over.html", "Over ons"),
]

KLANTEN = ["google", "salesforce", "ing", "klm", "shell", "prorail", "rws", "nn", "eneco",
           "bosch", "cgi", "sap", "talpa", "atradius", "tedx", "fontys", "inholland",
           "gemeente-rotterdam", "gemeente-delft", "nga"]
KLANT_NAMEN = {"rws": "Rijkswaterstaat", "nn": "Nationale-Nederlanden", "tedx": "TEDx",
               "gemeente-rotterdam": "Gemeente Rotterdam", "gemeente-delft": "Gemeente Delft",
               "nga": "NGA", "cgi": "CGI", "sap": "SAP", "ing": "ING", "klm": "KLM"}


def layout(bestand, titel, omschrijving, inhoud, schema=None):
    menu = "\n".join(
        f'<li><a href="{h}"{" aria-current=page" if h == bestand else ""}>{t}</a></li>' for h, t in NAV)
    ld = ""
    if schema:
        ld = f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>'
    return f"""<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{titel}</title>
<meta name="description" content="{omschrijving}">
<meta name="robots" content="noindex,nofollow">
<meta property="og:title" content="{titel}">
<meta property="og:description" content="{omschrijving}">
<meta property="og:image" content="assets/img/hero-team.webp">
<meta property="og:locale" content="nl_NL">
<meta name="theme-color" content="#FFF9EF">
<link rel="icon" href="favicon.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600&family=Nunito:wght@400;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
{ld}
</head>
<body>
<a class="skip" href="#inhoud">Naar de inhoud</a>
<div class="conceptbalk">Conceptversie van smoothieclub.nl, gebouwd als test. De officiële site vind je op <a href="https://www.smoothieclub.nl">smoothieclub.nl</a>.</div>
<header class="kop">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="Smoothieclub, naar de homepage"><img src="assets/img/logo.webp" alt="Smoothieclub" width="480" height="178"></a>
    <button class="hamburger" aria-label="Menu" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
    <ul class="menu" id="menu">
      {menu}
      <li><a class="knop primair klein" href="contact.html">Voorstel aanvragen</a></li>
    </ul>
  </div>
</header>
<main id="inhoud">
{inhoud}
</main>
<footer class="voet">
  <div class="wrap">
    <div>
      <a class="logo-wit" href="index.html"><img src="assets/img/logo.webp" alt="Smoothieclub" width="480" height="178"></a>
      <p>Gezonde teams blenden beter. Workshops, keynotes en Blendboxen die mensen in beweging brengen. Met de smoothie als metafoor.</p>
      <p class="klein">Smoothieclub is onderdeel van Kaders B.V. (Kaderloos), Rotterdam.</p>
      <p style="margin:14px 0 8px;color:#fff;font-weight:800">Volg Smoothieclub</p>
      {social_iconen()}
    </div>
    <div>
      <h4>Voor organisaties</h4>
      <ul>
        <li><a href="workshops.html#smoothen-your-life">Workshop Smoothen Your Life</a></li>
        <li><a href="workshops.html#teamworkshop">Teamworkshop Smoothen Your Business</a></li>
        <li><a href="keynote.html">Keynote De Prijs van Smaak</a></li>
        <li><a href="blendbox.html">Blendbox &amp; Mystery Box</a></li>
      </ul>
    </div>
    <div>
      <h4>Voor thuis</h4>
      <ul>
        <li><a href="webshop.html">Smoothie Configurators</a></li>
        <li><a href="webshop.html#kids">Voor kinderen</a></li>
        <li><a href="ingredienten.html">Ingrediënten</a></li>
        <li><a href="webshop.html#advies">Adviesgesprek</a></li>
      </ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul>
        <li><a href="{TEL_LINK}">{TEL}</a></li>
        <li><a href="mailto:{MAIL}">{MAIL}</a></li>
        <li><a href="{WA}" rel="noopener">WhatsApp</a></li>
        <li><a href="https://www.linkedin.com/in/jmbilderbeek" rel="noopener">Jean-Marc op LinkedIn</a></li>
      </ul>
    </div>
    <div class="onder">
      <span>&copy; <span id="jaar">2026</span> Smoothieclub &middot; Kaders B.V. &middot; KvK 51210010</span>
      <span>Smoothieclub geeft geen medisch advies. Een smoothie vervangt geen gevarieerd eetpatroon.</span>
    </div>
  </div>
</footer>
<a class="whatsapp" href="{WA}" rel="noopener" aria-label="Stuur Jean-Marc een WhatsApp-bericht"><svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3C8.8 3 3 8.7 3 15.8c0 2.5.7 4.9 2 7L3 29l6.4-2c2 1.1 4.3 1.7 6.6 1.7 7.2 0 13-5.7 13-12.8S23.2 3 16 3zm0 23.4c-2.1 0-4.1-.6-5.9-1.7l-.4-.3-3.8 1.2 1.2-3.7-.3-.4a10.4 10.4 0 0 1-1.7-5.7C5.1 9.9 10 5.2 16 5.2s10.9 4.7 10.9 10.6S22 26.4 16 26.4zm6-7.9c-.3-.2-1.9-1-2.2-1-.3-.1-.5-.2-.7.2l-1 1.2c-.2.2-.4.2-.7.1a8.8 8.8 0 0 1-4.4-3.8c-.3-.6.3-.5 1-1.7.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.3-1.2 1.1-1.2 2.8s1.2 3.2 1.4 3.4c.2.2 2.4 3.6 5.8 5 2.2.9 3 .9 4.1.8.7-.1 1.9-.8 2.2-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.3-.6-.4z"/></svg></a>
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def cta(titel="Klaar om te blenden?", tekst="Vertel ons wat je team nodig heeft. Je krijgt binnen 1 werkdag een voorstel op maat. Stop de twijfel!"):
    return f"""
<section class="sectie">
  <div class="wrap">
    <div class="cta-blok reveal">
      <div>
        <span class="kicker">Let's blend forces</span>
        <h2>{titel}</h2>
        <p class="intro">{tekst}</p>
        <div class="knoppen">
          <a class="knop primair" href="contact.html">Vraag een voorstel aan</a>
          <a class="knop licht" href="{TEL_LINK}">Bel {TEL}</a>
        </div>
      </div>
      <div class="contactregel">
        <img class="jm" src="assets/img/jm-portret.webp" alt="Jean-Marc Bilderbeek" width="300" height="300" loading="lazy">
        <p><strong style="color:#fff">Jean-Marc Bilderbeek</strong><br>Oprichter Smoothieclub. Je spreekt mij direct, geen tussenpersoon.</p>
        <a href="mailto:{MAIL}">✉ {MAIL}</a>
        <a href="{WA}" rel="noopener">💬 Stuur een WhatsApp</a>
      </div>
    </div>
  </div>
</section>"""


def logos():
    imgs = "".join(
        f'<img src="assets/img/klanten/{k}.webp" alt="{KLANT_NAMEN.get(k, k.title())}" width="110" height="110" loading="lazy">'
        for k in KLANTEN)
    return f'<div class="logos" aria-label="Organisaties waar wij voor werkten"><div class="rij">{imgs}{imgs.replace("alt=", "aria-hidden=true alt=")}</div></div>'


QUOTES = [
    ("13 maart hadden we een (h)eerlijke workshop van Jean-Marc. Samen met mijn 60 collega's kregen we via een mooie smoothie-metafoor meer inzicht in het combineren van individuele kwaliteiten.",
     "Deelnemer workshop", "Review via Springest"),
    ("Jean-Marc weet op een ludieke en persoonlijke wijze een groep van bijna 50 projectleiders te overtuigen om eens iets anders te doen dan gebruikelijk.",
     "Marc Meeder", "Directeur HOMIJ (waardering 8,4)"),
    ("Very knowledgeable, concrete and focused. Working with him is an absolutely valuable addition to your event.",
     "Sven Kruithof", "International Executive Producer, ITV Studios"),
]


def quotes(n=3):
    q = "".join(f"""<figure class="quote reveal"><blockquote>{t}</blockquote><figcaption><cite>{w}<span>{r}</span></cite></figcaption></figure>"""
                for t, w, r in QUOTES[:n])
    return f'<div class="raster r3">{q}</div>'


def video(yt, label):
    return f'<button class="video" data-yt="{yt}" aria-label="{label}"><img src="https://i.ytimg.com/vi/{yt}/hqdefault.jpg" alt="" loading="lazy"><span class="play"></span></button>'


def faq(items):
    blok = "".join(f"<details><summary>{v}</summary><p>{a}</p></details>" for v, a in items)
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": v, "acceptedAnswer": {"@type": "Answer", "text": a}} for v, a in items]}
    return f'<div class="faq">{blok}</div>', schema


ORG = {
    "@context": "https://schema.org", "@type": "Organization", "name": "Smoothieclub",
    "url": "https://www.smoothieclub.nl", "logo": "assets/img/logo.webp",
    "email": MAIL, "telephone": "+31650745730", "foundingDate": "2013",
    "founder": {"@type": "Person", "name": "Jean-Marc Bilderbeek"},
    "parentOrganization": {"@type": "Organization", "name": "Kaders B.V."},
    "address": {"@type": "PostalAddress", "addressLocality": "Rotterdam", "addressCountry": "NL"},
    "sameAs": [u for _, u, _ in SOCIAL],
}

# ---------------------------------------------------------------- HOME
FAQ_HOME = [
    ("Voor hoeveel mensen is een sessie geschikt?",
     "Van een managementteam van 8 tot een zaal van 250. De teamworkshop werkt het best tot 80 deelnemers, de workshop Smoothen Your Life tot 100 en de keynote tot 250. Online met de Mystery Box kan zelfs tot 500."),
    ("Waar vindt het plaats?",
     "Op iedere locatie in Nederland: bij jullie op kantoor, op de hei of in een zaal. Jij regelt de ruimte en het team, wij nemen de blenders, verse groente en fruit en alle materialen mee. We bouwen zelf op en af."),
    ("Wat kost een workshop?",
     "Dat hangt af van het format en de groepsgrootte. Reistijd, groente, fruit, blenders, materialen en de voorbespreking zitten er altijd bij in. Geen verrassingen achteraf. Vraag een voorstel aan en je hebt binnen 1 werkdag een prijs."),
    ("Moeten deelnemers van smoothies houden?",
     "Nee. De smoothie is de metafoor, niet het doel. Het gaat om samenwerken, keuzes maken en verantwoordelijkheid nemen. Wel wordt er volop geproefd, gelachen en geproost op een gezonde samenwerking."),
    ("Kan het ook in het Engels?",
     "Ja. De keynote en de workshops zijn ook in het Engels te boeken, ideaal voor internationale teams."),
    ("Hoe snel kan het?",
     "Vaak binnen een paar weken. Bel of app even voor de actuele beschikbaarheid, dan weet je het meteen."),
]


def home():
    faq_html, faq_schema = faq(FAQ_HOME)
    inhoud = f"""
<section class="hero">
  <div class="cirkels" aria-hidden="true">
    <i style="width:420px;height:420px;background:var(--geel);right:-120px;top:-120px"></i>
    <i style="width:260px;height:260px;background:var(--roze);left:-90px;bottom:-60px"></i>
    <i style="width:160px;height:160px;background:var(--groen);left:44%;top:30px"></i>
  </div>
  <div class="wrap">
    <div>
      <span class="kicker">Teamsessies · Keynotes · Energizers</span>
      <h1>Gezonde teams <span class="markeer">blenden</span> beter.</h1>
      <p class="intro">Smoothieclub brengt je team in beweging met één verrassende metafoor: de smoothie. Samen blenden, proeven en presenteren. En aan het eind van de dag staan er concrete afspraken op tafel.</p>
      <ul class="vink">
        <li>Energie en plezier, met een serieuze boodschap</li>
        <li>Op jouw locatie, alles wordt meegenomen</li>
        <li>Voorstel op maat binnen 1 werkdag</li>
      </ul>
      <div class="knoppen">
        <a class="knop primair" href="contact.html">Vraag een voorstel aan</a>
        <a class="knop rand" href="#aanbod">Bekijk het aanbod</a>
      </div>
    </div>
    <div class="hero-beeld">
      <img src="assets/img/hero-team.webp" alt="Team poseert bij een tafel vol groente, fruit en blenders tijdens een Smoothieclub-workshop" width="1800" height="598" fetchpriority="high">
      <div class="hero-badge"><strong>8,4</strong><span>gemiddelde waardering<br>door opdrachtgevers</span></div>
    </div>
  </div>
</section>

<section class="sectie wit" style="padding-top:0">
  <div class="wrap">
    <div class="feiten">
      <div class="feit" style="--c:var(--roze)"><strong>2013</strong><span>eerste Smoothieclub-workshop</span></div>
      <div class="feit" style="--c:var(--oranje)"><strong>1000en</strong><span>deelnemers in beweging gebracht</span></div>
      <div class="feit" style="--c:var(--geel)"><strong>8 tot 250</strong><span>deelnemers per sessie</span></div>
      <div class="feit" style="--c:var(--groen)"><strong>3.000</strong><span>bomen geplant in Kenia</span></div>
    </div>
    <p class="center klein" style="margin:56px 0 18px">Onder meer vertrouwd door</p>
    {logos()}
  </div>
</section>

<section class="sectie">
  <div class="wrap">
    <div class="center" style="margin-bottom:40px">
      <span class="kicker">Waar kunnen we je mee helpen?</span>
      <h2>Kies je route</h2>
    </div>
    <div class="raster r2">
      <a class="pad reveal" href="workshops.html" style="text-decoration:none">
        <img src="assets/img/hero-event.webp" alt="" loading="lazy">
        <span class="kicker">Voor organisaties</span>
        <h3>Geef je team een gezonde boost</h3>
        <p>Teamdag, heidag, personeelsfeest of congres. Een sessie die mensen raakt en in beweging zet.</p>
        <span class="knop licht klein" style="align-self:flex-start">Bekijk workshops &amp; keynote</span>
      </a>
      <a class="pad reveal" href="webshop.html" style="text-decoration:none">
        <img src="assets/img/configurators-banner.webp" alt="" loading="lazy">
        <span class="kicker">Voor thuis</span>
        <h3>Zelf supergezonde smoothies maken</h3>
        <p>Met onze Smoothie Configurators blend je in één oogopslag. Ook voor kinderen vanaf 6 jaar.</p>
        <span class="knop licht klein" style="align-self:flex-start">Naar de webshop</span>
      </a>
    </div>
  </div>
</section>

<section class="sectie wit" id="aanbod">
  <div class="wrap">
    <div class="center" style="margin-bottom:44px">
      <span class="kicker">Ons aanbod</span>
      <h2>Vier manieren om samen te blenden</h2>
      <p class="intro">Elk format is anders. De kern is hetzelfde: mensen willen wel veranderen, maar niet veranderd worden. Dus laten we ze het zelf ontdekken.</p>
    </div>
    <div class="raster r4">
      <article class="kaart accent reveal" style="--c:var(--roze)">
        <img class="beeld" src="assets/img/hero-keynote.webp" alt="Jean-Marc op het podium voor een volle zaal" loading="lazy">
        <div class="in"><div class="meta"><span class="label">45-60 min</span><span class="label">tot 250</span></div>
        <h3>Keynote De Prijs van Smaak</h3><p>Een persoonlijk en prijswinnend verhaal over keuzes maken en eigen verantwoordelijkheid. Met proefronde.</p>
        <a class="lees" href="keynote.html">Meer over de keynote</a></div>
      </article>
      <article class="kaart accent reveal" style="--c:var(--oranje)">
        <img class="beeld" src="assets/img/hero-event.webp" alt="Volle zaal tijdens een energizing workshop" loading="lazy">
        <div class="in"><div class="meta"><span class="label">1,5-2 uur</span><span class="label">tot 100</span></div>
        <h3>Workshop Smoothen Your Life</h3><p>De energizer voor je event of personeelsdag. Luisteren, proeven en in groepjes zelf blenden.</p>
        <a class="lees" href="workshops.html#smoothen-your-life">Meer over de workshop</a></div>
      </article>
      <article class="kaart accent reveal" style="--c:var(--groen)">
        <img class="beeld" src="assets/img/hero-team.webp" alt="Team met zelfgemaakte smoothies" loading="lazy">
        <div class="in"><div class="meta"><span class="label">4-5 uur</span><span class="label">tot 80</span></div>
        <h3>Teamworkshop Smoothen Your Business</h3><p>Elk ingrediënt staat voor een concrete actie. Je team blendt zijn eigen oplossing voor een echte uitdaging.</p>
        <a class="lees" href="workshops.html#teamworkshop">Meer over de teamworkshop</a></div>
      </article>
      <article class="kaart accent reveal" style="--c:var(--blauw)">
        <img class="beeld" src="assets/img/jm-blendbox.webp" alt="Jean-Marc overhandigt een fruitmand" loading="lazy">
        <div class="in"><div class="meta"><span class="label">online &amp; thuis</span><span class="label">tot 500</span></div>
        <h3>Blendbox &amp; Mystery Box</h3><p>Een gezonde verrassing bij medewerkers thuis, samen uitgepakt tijdens een live webinar.</p>
        <a class="lees" href="blendbox.html">Meer over de Blendbox</a></div>
      </article>
    </div>
    <p class="center" style="margin-top:34px"><a class="knop rand" href="workshops.html#vergelijk">Vergelijk alle formats</a></p>
  </div>
</section>

<section class="sectie">
  <div class="wrap">
    <div class="center" style="margin-bottom:40px">
      <span class="kicker">Zo werkt het</span>
      <h2>Van eerste belletje tot proost</h2>
      <p class="intro">Jij regelt de ruimte en het team. Wij de rest.</p>
    </div>
    <div class="stappen">
      <div class="stap reveal" style="--c:var(--geel)"><h3>Kennismaken</h3><p>We bespreken wat er speelt in je team en wat de sessie moet opleveren. Binnen 1 werkdag heb je een voorstel.</p></div>
      <div class="stap reveal" style="--c:var(--roze)"><h3>Voorbereiden op maat</h3><p>We stemmen het programma af op jullie uitdagingen. Bij de teamworkshop voeren we vooraf 8 vertrouwelijke interviews.</p></div>
      <div class="stap reveal" style="--c:var(--groen)"><h3>Blenden en proosten</h3><p>We komen met blenders, dagverse groente en fruit. Na afloop heb je energie, inzicht en concrete afspraken.</p></div>
    </div>
    <p class="center" style="margin-top:34px"><a class="knop primair" href="contact.html">Plan een kennismaking</a></p>
  </div>
</section>

<section class="sectie donker">
  <div class="wrap split">
    <div class="reveal">
      {video("47OaeMYnndk", "Bekijk de keynote De Prijs van Smaak")}
    </div>
    <div class="reveal">
      <span class="kicker">Het verhaal achter Smoothieclub</span>
      <h2>Van een ongeneeslijke diagnose naar <span class="markeer">een missie</span></h2>
      <p>In 2008 kreeg Jean-Marc Bilderbeek zijn eerste epileptische aanval. Drukke baan, 'lekker' en 'makkelijk' bepaalden zijn eetpatroon. De diagnose was een keiharde wake-up call: hij moest zelf veranderen.</p>
      <p>Zijn zoektocht leidde naar de blender. En naar een inzicht dat verder gaat dan voeding: elke keuze heeft een prijs. Dat noemt hij <em>de prijs van smaak</em>. Sinds 2013 neemt hij teams en zalen mee in dat verhaal.</p>
      <div class="knoppen"><a class="knop licht" href="over.html">Lees het hele verhaal</a></div>
    </div>
  </div>
</section>

<section class="sectie">
  <div class="wrap">
    <div class="center" style="margin-bottom:40px"><span class="kicker">Wat deelnemers zeggen</span><h2>Ervaringen</h2></div>
    {quotes()}
  </div>
</section>

<section class="sectie wit">
  <div class="wrap split omgekeerd">
    <div class="reveal"><img class="foto" src="assets/img/p-totaal.webp" alt="De Smoothie Configurators voor volwassenen en kinderen" loading="lazy"></div>
    <div class="reveal">
      <span class="kicker">Webshop</span>
      <h2>Zelf blenden? Begin met de Smoothie Configurator</h2>
      <p>14 doelgerichte smoothies op één kaart, met 23 ingrediënten die je gewoon bij de supermarkt haalt. Je ziet in één oogopslag wat erin gaat en hoeveel. Voor kinderen zijn er speciale KIDS-versies.</p>
      <ul class="vink"><li>Direct te downloaden als PDF, vanaf € 8,75</li><li>Of stevig gelamineerd, handig naast de blender</li><li>Per verkochte Configurator planten we een boom in Kenia</li></ul>
      <div class="knoppen"><a class="knop primair" href="webshop.html">Bekijk de Configurators</a></div>
    </div>
  </div>
</section>

<section class="sectie">
  <div class="wrap" style="max-width:860px">
    <div class="center" style="margin-bottom:34px"><span class="kicker">Veelgestelde vragen</span><h2>Goed om te weten</h2></div>
    {faq_html}
  </div>
</section>
{cta()}
"""
    return layout("index.html", "Smoothieclub | Teamworkshops, keynotes en energizers met de smoothie als metafoor",
                  "Smoothieclub brengt teams in beweging met workshops, keynotes en Blendboxen. Samen blenden, proeven en concrete afspraken maken. Op iedere locatie, 8 tot 250 deelnemers.",
                  inhoud, [ORG, faq_schema])


# ---------------------------------------------------------------- WORKSHOPS
def workshops():
    inhoud = f"""
<section class="pagina-hero">
  <img class="bg" src="assets/img/hero-workshops.webp" alt="" fetchpriority="high">
  <div class="wrap">
    <div class="kruimel"><a href="index.html">Home</a> / Workshops</div>
    <h1>Teamworkshops die <span class="markeer">écht</span> iets opleveren</h1>
    <p>Geen braaf uitje, maar een sessie waar je team over blijft praten. Met energie, humor en een serieuze boodschap. Anders kijken. Wèl oplossen.</p>
    <div class="knoppen"><a class="knop primair" href="contact.html?type=Workshop">Vraag een voorstel aan</a><a class="knop licht" href="#vergelijk">Vergelijk de formats</a></div>
  </div>
</section>

<section class="sectie wit" id="smoothen-your-life">
  <div class="wrap split">
    <div class="reveal">
      <span class="kicker">Voor events, personeelsdagen en klantendagen</span>
      <h2>Workshop Smoothen Your Life</h2>
      <p class="intro">De energizer die je event naar een hoger plan tilt. In 1,5 tot 2 uur van luisteren naar zelf doen.</p>
      <p>Jean-Marc neemt je mee in zijn verhaal, vol humor en prikkelende inzichten over voeding, keuzes en de prijs van smaak. Daarna gaan de blenders aan. In groepjes maken deelnemers met de Smoothie Configurator® smoothies die passen bij hun eigen doel. Aan het eind proost iedereen op een gezonde samenwerking.</p>
      <h3 style="margin-top:1.4em">Dit krijg je</h3>
      <ul class="vink">
        <li>Een actieve ervaring die aanzet tot outside-the-box denken</li>
        <li>Iedereen leert snel en makkelijk een smoothie maken</li>
        <li>Blenders per groep, 25 soorten dagverse groente en fruit, informatiekaarten</li>
        <li>Opbouw, afbouw, reistijd en voorbespreking inbegrepen</li>
        <li>Geschikt tot 100 deelnemers, ook in het Engels</li>
      </ul>
      <div class="knoppen"><a class="knop primair" href="contact.html?type=Workshop%20Smoothen%20Your%20Life">Boek deze workshop</a></div>
    </div>
    <div class="reveal"><img class="foto" src="assets/img/hero-event.webp" alt="Jean-Marc maakt een selfie met een enthousiaste zaal" loading="lazy" style="aspect-ratio:4/3.4;object-fit:cover"></div>
  </div>
</section>

<section class="sectie" id="teamworkshop">
  <div class="wrap split omgekeerd">
    <div class="reveal">
      <span class="kicker">Voor teams met een echte uitdaging</span>
      <h2>Teamworkshop Smoothen Your Business</h2>
      <p class="intro">Samen werken aan gezond samenwerken. Je team blendt zijn eigen oplossing, letterlijk.</p>
      <p>Loopt de samenwerking vast? Staat er een verandering voor de deur? In deze workshop maken groepjes een smoothie als antwoord op een vooraf bepaalde uitdaging. Elk ingrediënt staat voor een concrete actie. Dat levert hilarische presentaties op, met een heel serieuze uitkomst: afspraken waar iedereen achter staat.</p>
      <p>Het bijzondere: jij hoeft het programma niet te bedenken. Jean-Marc voert vooraf 8 vertrouwelijke gesprekken met een dwarsdoorsnede van je team. Die gesprekken bepalen de thema's. Zo kun jij als leidinggevende gewoon meedoen.</p>
      <div class="knoppen"><a class="knop primair" href="contact.html?type=Teamworkshop%20Smoothen%20Your%20Business">Bespreek je uitdaging</a></div>
    </div>
    <div class="reveal">
      <ol class="tijdlijn">
        <li><strong>Vooraf: 8 interviews</strong>Wanneer is deze dag voor jou geslaagd? Waar loop je tegenaan? Wie verdient een pluim?</li>
        <li><strong>Keynote De Prijs van Smaak</strong>Het verhaal van Jean-Marc als opwarmer: keuzes maken en verantwoordelijkheid nemen.</li>
        <li><strong>Proeven</strong>Een ter plekke gemaakte smoothie. Smaak is niet altijd de beste raadgever.</li>
        <li><strong>Blenden in groepjes</strong>Elk ingrediënt is een actie. Samen stel je de ideale blend voor jullie uitdaging samen.</li>
        <li><strong>Presenteren en proosten</strong>Elke groep pitcht zijn blend. De acties gaan mee naar de werkvloer.</li>
      </ol>
      <p class="klein">Duur 4 tot 5 uur · tot 80 deelnemers · inclusief voorbespreking, interviews, inkoop, materiaal en evaluatie</p>
    </div>
  </div>
</section>

<section class="sectie wit" id="vergelijk">
  <div class="wrap">
    <div class="center" style="margin-bottom:36px"><span class="kicker">Welke past bij jou?</span><h2>Alle formats naast elkaar</h2></div>
    <div class="tabel-wrap reveal">
      <table class="vergelijk">
        <thead><tr><th></th><th>Keynote</th><th>Smoothen Your Life</th><th>Smoothen Your Business</th><th>Blendbox / Mystery Box</th></tr></thead>
        <tbody>
          <tr><th>Ideaal voor</th><td>Congres, kick-off, inspiratiesessie</td><td>Personeelsdag, event, klantendag</td><td>Team in verandering of met een vraagstuk</td><td>Hybride en thuiswerkende teams</td></tr>
          <tr><th>Duur</th><td>45-60 minuten</td><td>1,5-2 uur</td><td>4-5 uur</td><td>Webinar naar keuze</td></tr>
          <tr><th>Deelnemers</th><td>tot 250</td><td>tot 100</td><td>tot 80</td><td>tot 500</td></tr>
          <tr><th>Zelf blenden</th><td>Proefronde</td><td>Ja, in groepjes</td><td>Ja, als teamoplossing</td><td>Thuis, met box</td></tr>
          <tr><th>Resultaat</th><td>Inspiratie en inzicht</td><td>Energie en gezond gedrag</td><td>Concrete teamafspraken</td><td>Verbinding op afstand</td></tr>
          <tr><th></th><td><a class="knop primair klein" href="keynote.html">Bekijk</a></td><td><a class="knop primair klein" href="#smoothen-your-life">Bekijk</a></td><td><a class="knop primair klein" href="#teamworkshop">Bekijk</a></td><td><a class="knop primair klein" href="blendbox.html">Bekijk</a></td></tr>
        </tbody>
      </table>
    </div>
    <p class="center klein" style="margin-top:18px">Twijfel je? Bel {TEL}. In 10 minuten weten we samen welk format past.</p>
  </div>
</section>

<section class="sectie">
  <div class="wrap">
    <div class="center" style="margin-bottom:40px"><span class="kicker">Ervaringen</span><h2>Wat teams erover zeggen</h2></div>
    {quotes()}
  </div>
</section>
{cta("Maak van je teamdag iets om over na te praten", "Vertel ons over je team en je uitdaging. Binnen 1 werkdag heb je een voorstel op maat.")}
"""
    return layout("workshops.html", "Teamworkshops en energizers | Smoothieclub",
                  "Teamworkshop Smoothen Your Business en workshop Smoothen Your Life: samen blenden, proeven en concrete teamafspraken maken. Op iedere locatie, tot 100 deelnemers.",
                  inhoud, ORG)


# ---------------------------------------------------------------- KEYNOTE
def keynote():
    inhoud = f"""
<section class="pagina-hero">
  <img class="bg" src="assets/img/hero-keynote.webp" alt="" fetchpriority="high">
  <div class="wrap">
    <div class="kruimel"><a href="index.html">Home</a> / Keynote</div>
    <h1>Keynote <span class="markeer">De Prijs van Smaak</span></h1>
    <p>Een prijswinnend, persoonlijk en kwetsbaar verhaal over keuzes maken en verantwoordelijkheid nemen. Pas op: het enthousiasme is aanstekelijk.</p>
    <div class="knoppen"><a class="knop primair" href="contact.html?type=Keynote">Check beschikbaarheid</a><a class="knop licht" href="#video">Bekijk een fragment</a></div>
  </div>
</section>

<section class="sectie wit">
  <div class="wrap split">
    <div class="reveal">
      <span class="kicker">Waar gaat het over?</span>
      <h2>Van een ongeneeslijke ziekte naar een uniek bedrijf</h2>
      <p>Jean-Marc Bilderbeek had een druk leven als interim manager, projectleider en trainer. Tot hij in 2008 zijn eerste epileptische aanval kreeg. De boodschap van de arts: dit gaat nooit meer over. Zijn wereld stortte deels in.</p>
      <p>Eén ding werd snel duidelijk: hij moest zelf veranderen. Hij ontdekte dat 'lekker' en 'makkelijk' zijn keuzes bepaalden. Zijn zoektocht leverde inzichten op over gezondheid, eigen verantwoordelijkheid en kaderloos denken. En over de prijs die we betalen voor smaak.</p>
      <p>Die inzichten blijken ijzersterke metaforen voor wat organisaties en teams doormaken bij verandering. Daarom werkt dit verhaal in elke zaal.</p>
    </div>
    <div class="reveal">
      <h3>Wat je publiek meeneemt</h3>
      <ul class="vink">
        <li>Waarom mensen wel willen veranderen, maar niet veranderd willen worden</li>
        <li>Hoe je bewuste keuzes maakt, op het werk en daarbuiten</li>
        <li>De kracht van eigen verantwoordelijkheid</li>
        <li>Inzichten die de volgende ochtend al toepasbaar zijn</li>
        <li>Een proefronde met een ter plekke gemaakte smoothie</li>
      </ul>
      <div class="raster r2" style="margin-top:24px">
        <div class="feit" style="--c:var(--roze)"><strong>45-60</strong><span>minuten</span></div>
        <div class="feit" style="--c:var(--groen)"><strong>tot 250</strong><span>deelnemers</span></div>
        <div class="feit" style="--c:var(--geel)"><strong>NL / EN</strong><span>taal</span></div>
        <div class="feit" style="--c:var(--oranje)"><strong>#2 van 96</strong><span>MPI Keynote Challenge</span></div>
      </div>
    </div>
  </div>
</section>

<section class="sectie donker" id="video">
  <div class="wrap" style="max-width:960px">
    <div class="center" style="margin-bottom:30px"><span class="kicker">Zie het zelf</span><h2>Jean-Marc in actie</h2></div>
    {video("47OaeMYnndk", "Bekijk de keynote De Prijs van Smaak")}
  </div>
</section>

<section class="sectie">
  <div class="wrap split omgekeerd">
    <div class="reveal"><img class="foto" src="assets/img/jm-pepers.webp" alt="Jean-Marc lachend met rode pepers en bleekselderij" loading="lazy"></div>
    <div class="reveal">
      <span class="kicker">Over de spreker</span>
      <h2>Jean-Marc Bilderbeek</h2>
      <p>Verandermanager, trainer en spreker. Sinds 2008 eigenaar van Kaderloos. 20+ jaar ervaring met verandertrajecten bij onder meer Rijkswaterstaat, UWV, ProRail, Nationale-Nederlanden, Rabobank, KLM en Macaw. Coachte sprekers van TEDx Rotterdam.</p>
      <p>Zijn credo: <strong>"Mensen willen wel veranderen, maar niet veranderd worden."</strong></p>
      <p>Partners noemen hem ondernemend, energiek en resultaatgericht. Deelnemers vooral: aanstekelijk.</p>
      <div class="knoppen"><a class="knop primair" href="contact.html?type=Keynote">Boek Jean-Marc</a><a class="knop rand" href="over.html">Meer over Jean-Marc</a></div>
    </div>
  </div>
</section>
{cta("Zet je publiek in beweging", "Check de beschikbaarheid voor jouw datum. Je hoort binnen 1 werkdag van ons.")}
"""
    ev = {"@context": "https://schema.org", "@type": "Service", "name": "Keynote De Prijs van Smaak",
          "provider": {"@type": "Person", "name": "Jean-Marc Bilderbeek"}, "areaServed": "NL"}
    return layout("keynote.html", "Keynote De Prijs van Smaak door Jean-Marc Bilderbeek | Smoothieclub",
                  "Boek de prijswinnende keynote De Prijs van Smaak van Jean-Marc Bilderbeek: persoonlijk, energiek en direct toepasbaar. 45-60 minuten, tot 250 deelnemers, NL en EN.",
                  inhoud, [ORG, ev])


# ---------------------------------------------------------------- BLENDBOX
def blendbox():
    inhoud = f"""
<section class="pagina-hero">
  <img class="bg" src="assets/img/jm-blendbox.webp" alt="" fetchpriority="high" style="object-position:center 30%">
  <div class="wrap">
    <div class="kruimel"><a href="index.html">Home</a> / Blendbox</div>
    <h1>Een gezonde verrassing, <span class="markeer">bij iedereen thuis</span></h1>
    <p>Met de Blendbox en de Mystery Box verbind je collega's, klanten of relaties, waar ze ook werken. Origineel, persoonlijk en blijvend.</p>
    <div class="knoppen"><a class="knop primair" href="contact.html?type=Blendbox">Vraag een voorstel aan</a></div>
  </div>
</section>

<section class="sectie wit">
  <div class="wrap">
    <div class="center" style="margin-bottom:40px"><span class="kicker">Twee smaken</span><h2>Kies wat past bij je doel</h2></div>
    <div class="raster r2">
      <article class="kaart accent reveal" style="--c:var(--oranje)">
        <div class="in">
          <h3>Blendbox</h3>
          <p>Een pakket dat bij medewerkers of relaties thuis wordt bezorgd. Met gelamineerde Smoothie Configurators voor naast de blender. Kies je voor een variant met vers fruit, dan kan iedereen direct aan de slag.</p>
          <ul class="vink">
            <li>Verschillende pakketten, ook met vers fruit</li>
            <li>Configurator voor volwassenen en een KIDS-versie voor het gezin</li>
            <li>Met je eigen logo en een QR-code naar een persoonlijke videoboodschap</li>
            <li>Optioneel met blender en instructievideo</li>
          </ul>
          <a class="knop primair klein" href="contact.html?type=Blendbox" style="align-self:flex-start;margin-top:14px">Stel je Blendbox samen</a>
        </div>
      </article>
      <article class="kaart accent reveal" style="--c:var(--blauw)">
        <div class="in">
          <h3>Mystery Box programma</h3>
          <p>Een outside-the-box programma dat in een doosje past. Deelnemers krijgen een week vooraf een teaservideo. De dag ervoor ligt er een gesloten box op de mat. Tijdens het live webinar pakt iedereen hem tegelijk uit.</p>
          <ul class="vink">
            <li>Live keynote plus maatwerk rond jullie doelen</li>
            <li>Tot 500 deelnemers, hybride of volledig online</li>
            <li>Luxe box, brievenbusdoos of envelop, met persoonlijke brief</li>
            <li>Per deelnemer planten we een boom via AfricaWoodGrow</li>
          </ul>
          <a class="knop primair klein" href="contact.html?type=Mystery%20Box" style="align-self:flex-start;margin-top:14px">Bespreek je Mystery Box</a>
        </div>
      </article>
    </div>
  </div>
</section>

<section class="sectie">
  <div class="wrap split">
    <div class="reveal">{video("lT5AWtMx8HU", "Bekijk de video over de Blendbox")}</div>
    <div class="reveal">
      <span class="kicker">Waarom het werkt</span>
      <h2>Aandacht die je kunt proeven</h2>
      <p>Een bedankje per mail is zo vergeten. Een box met vers fruit en een configurator die maanden in de keuken hangt niet. Combineer de levering met een Smoothieclub-webinar en je team deelt een ervaring, ook op afstand.</p>
      <p>Alles is aan te passen: inhoud, verpakking, boodschap en timing. So: let's blend ideas.</p>
      <div class="knoppen"><a class="knop primair" href="contact.html?type=Blendbox">Vraag een voorstel aan</a><a class="knop rand" href="{TEL_LINK}">Bel {TEL}</a></div>
    </div>
  </div>
</section>
{cta("Verras je team of relaties", "Vertel ons voor wie de box is en wanneer hij moet landen. Wij denken mee over inhoud, budget en timing.")}
"""
    return layout("blendbox.html", "Blendbox en Mystery Box: gezonde verrassing voor je team | Smoothieclub",
                  "Verras medewerkers of relaties thuis met een Blendbox of Mystery Box. Met Smoothie Configurators, vers fruit en een live webinar. Tot 500 deelnemers.",
                  inhoud, ORG)


# ---------------------------------------------------------------- WEBSHOP
PRODUCTEN = [
    ("smoothie-configurator-nl", "p-configurator", "Smoothie Configurator", "Leeftijd 16+", "Klassieker",
     "14 doelgerichte smoothies op basis van 23 ingrediënten uit de supermarkt. Meer energie, een frisse start na een feestje of juist een stevig ontbijt: je ziet in één oogopslag wat erin gaat. Gemaakt op nut, niet op smaak. Durf jij het aan?",
     "8,75", "PDF € 8,75 · gelamineerd € 12,50"),
    ("kids-smoothie-configurator", "p-kids", "KIDS Smoothie Configurator", "Leeftijd 8+", "",
     "Hét hulpmiddel om kinderen meer groente en fruit te laten eten. 15 ingrediënten, elke blend bevat een portie groente en wordt toegankelijk gemaakt met zoet fruit. Laat je kind kiezen: vandaag sterk, slim of cool?",
     "8,75", "PDF € 8,75 · gelamineerd € 12,50"),
    ("kids-smoothie-challenge", "p-challenge", "KIDS Smoothie Challenge", "Leeftijd 6+", "",
     "In 8 levels leren de jongste kids zelf smoothies maken. Elke dag een level. Na 8 dagen verdienen ze een echt Smoothie Certificaat. Uitdagend, cool en belonend. Altijd samen met een volwassene snijden en blenden.",
     "8,75", "PDF € 8,75 · gelamineerd € 10,95"),
    ("smoothieclub-totaalpakket", "p-totaal", "Totaalpakket voor het hele gezin", "Leeftijd 6+ tot 99", "Voordeligst",
     "Alle drie de Configurators in één pakket: de Challenge, de KIDS Configurator en de Smoothie Configurator voor volwassenen. Het hele gezin kan direct aan de slag.",
     "19,95", "PDF € 19,95 · gelamineerd € 27,50"),
    ("adviesgesprek", "p-advies", "Adviesgesprek met Jean-Marc", "Online · 45 minuten", "Persoonlijk",
     "45 minuten kaderloos sparren over jouw persoonlijke of zakelijke vraag. Over je team, je organisatie of je eigen volgende stap. Je krijgt direct toepasbare ideeën, gebaseerd op 25+ jaar ervaring met verandering.",
     "87,50", "Inclusief een Smoothie Configurator naar keuze"),
]


def webshop():
    kaarten = "".join(f"""
      <article class="product reveal"{' id="kids"' if slug == 'kids-smoothie-configurator' else ''}>
        {f'<span class="lint">{lint}</span>' if lint else ''}
        <img src="assets/img/{img}.webp" alt="{naam}" loading="lazy" width="700" height="700">
        <div class="in">
          <span class="label" style="align-self:flex-start;margin-bottom:10px">{leeftijd}</span>
          <h3>{naam}</h3>
          <p>{tekst}</p>
          <div class="prijs">{"" if slug == "adviesgesprek" else "vanaf "}€ {prijs}</div>
          <div class="varianten">{var}</div>
          <a class="knop primair klein" href="{SHOP}{slug}/" rel="noopener">{"Boek je gesprek" if slug == "adviesgesprek" else "Bestellen"}</a>
        </div>
      </article>""" for slug, img, naam, leeftijd, lint, tekst, prijs, var in PRODUCTEN)
    prod_schema = [{"@context": "https://schema.org", "@type": "Product", "name": naam, "image": f"assets/img/{img}.webp",
                    "brand": "Smoothieclub", "offers": {"@type": "Offer", "priceCurrency": "EUR", "price": prijs.replace(",", "."),
                                                        "url": f"{SHOP}{slug}/", "availability": "https://schema.org/InStock"}}
                   for slug, img, naam, leeftijd, lint, tekst, prijs, var in PRODUCTEN]
    inhoud = f"""
<section class="pagina-hero">
  <img class="bg" src="assets/img/configurators-banner.webp" alt="" fetchpriority="high">
  <div class="wrap">
    <div class="kruimel"><a href="index.html">Home</a> / Webshop</div>
    <h1>Smoothie Configurators en <span class="markeer">advies op maat</span></h1>
    <p>Met de Smoothie Configurator weet je precies wat erin gaat en hoeveel. Voor jezelf, je kinderen of het hele gezin. Liever persoonlijk sparren? Boek een adviesgesprek van 45 minuten met Jean-Marc.</p>
    <div class="knoppen"><a class="knop primair" href="#producten">Bekijk de Configurators</a><a class="knop licht" href="#advies">Boek een adviesgesprek</a></div>
  </div>
</section>

<section class="sectie wit" style="padding-top:0">
  <div class="wrap">
    <div class="feiten">
      <div class="feit" style="--c:var(--roze)"><strong>Direct</strong><span>PDF in je mailbox na betaling</span></div>
      <div class="feit" style="--c:var(--geel)"><strong>Gelamineerd</strong><span>ook per post, voor naast de blender</span></div>
      <div class="feit" style="--c:var(--groen)"><strong>1 = 1 boom</strong><span>per Configurator een boom in Kenia</span></div>
      <div class="feit" style="--c:var(--blauw)"><strong>Veilig</strong><span>betalen via onze eigen webshop</span></div>
    </div>
  </div>
</section>

<section class="sectie" id="producten">
  <div class="wrap">
    <div class="center" style="margin-bottom:40px">
      <span class="kicker">Onze producten</span>
      <h2>Kies wat bij je past</h2>
      <p class="intro">Alle prijzen zijn inclusief btw. Bij de gelamineerde versie komen verzendkosten erbij.</p>
    </div>
    <div class="producten">{kaarten}</div>
    <p class="center klein" style="margin-top:24px">Bestellen en betalen gaat via de officiële webshop op smoothieclub.nl.</p>
  </div>
</section>

<section class="sectie wit">
  <div class="wrap split">
    <div class="reveal">
      <span class="kicker">Ons uitgangspunt</span>
      <h2>Nut boven smaak. Dat is de prijs van smaak.</h2>
      <p>De meeste smoothierecepten zijn gemaakt om lekker te zijn. Veel zoet fruit, weinig groente. Wij doen het andersom: het doel van de smoothie bepaalt de ingrediënten. Dat is soms even slikken. Maar je smoothie wordt er voedzamer, goedkoper en duurzamer van.</p>
      <p>Onze recepten volgen de <strong>gele B</strong>: ge-zond, le-kker en b-etaalbaar. Alle ingrediënten zijn gewoon verkrijgbaar in Nederland.</p>
      <div class="knoppen"><a class="knop rand" href="ingredienten.html">Bekijk onze ingrediënten</a></div>
    </div>
    <div class="reveal"><img class="foto" src="assets/img/configurator-a4.webp" alt="De Smoothie Configurator: een kleurrijke tabel met ingrediënten en blends" loading="lazy"></div>
  </div>
</section>

<section class="sectie" id="advies">
  <div class="wrap split omgekeerd">
    <div class="reveal"><img class="foto" src="assets/img/p-advies.webp" alt="Jean-Marc met een tekstballon: heb je specifieke wensen of vragen?" loading="lazy"></div>
    <div class="reveal">
      <span class="kicker">Persoonlijk</span>
      <h2>Adviesgesprek met Jean-Marc</h2>
      <p>45 minuten écht kaderloos sparren over jouw persoonlijke of zakelijke vraag. Over je team, je organisatie of je eigen volgende stap. Je krijgt direct toepasbare ideeën en na afloop een Smoothie Configurator naar keuze.</p>
      <ul class="vink"><li>Online, op een moment dat jou past</li><li>25+ jaar ervaring met verandering bij 250+ organisaties</li><li>Vertrouwelijk en volledig op jouw situatie afgestemd</li></ul>
      <div class="prijs" style="margin-top:14px">€ 87,50 <small>incl. btw</small></div>
      <div class="knoppen"><a class="knop primair" href="{SHOP}adviesgesprek/" rel="noopener">Boek je gesprek</a></div>
    </div>
  </div>
</section>
{cta("Liever een Blendbox voor je team?", "Configurators met je eigen logo, vers fruit en een persoonlijke videoboodschap. Vraag een voorstel op maat aan.")}
"""
    return layout("webshop.html", "Webshop: Smoothie Configurators en adviesgesprek met Jean-Marc | Smoothieclub",
                  "Bestel de Smoothie Configurator, de KIDS Configurator, de Smoothie Challenge of het Totaalpakket, direct als PDF vanaf € 8,75. Of boek een adviesgesprek van 45 minuten met Jean-Marc Bilderbeek.",
                  inhoud, [ORG] + prod_schema)


# ---------------------------------------------------------------- INGREDIENTEN
# Ingrediënten: bron zijn de basiskaarten en ingrediëntpagina's van de oude smoothieclub.nl.
# Per ingrediënt: (id/anker, beeld, naam, categorie, portie per smoothie, rijk aan, wat het doet, goed om te weten).
# Formulering volgt de toegestane Europese voedingsclaims: wat erin zit en waar dat aan bijdraagt, geen genezingsclaims.
INGR = [
    ("bleekselderij", "bleekselderij", "Bleekselderij", "groente", "1/3 bos",
     ["vitamine B", "vitamine C", "vezels", "water", "antioxidanten"],
     ["Werkt vochtafdrijvend", "Vezels ondersteunen je spijsvertering", "Vitamine C draagt bij aan je weerstand",
      "Heel weinig calorieën: verteren kost meer energie dan het oplevert"],
     "Staat al eeuwen bekend als lustopwekkend."),
    ("boerenkool", "boerenkool", "Boerenkool", "groente", "2 handjes",
     ["ijzer", "calcium", "vitamine A", "vitamine C", "omega-3", "vezels"],
     ["Bevat meer ijzer dan rundvlees: ijzer is nodig voor zuurstoftransport in je bloed",
      "Vitamine A draagt bij aan een normaal gezichtsvermogen", "Calcium is nodig voor sterke botten",
      "Vitamine C ondersteunt je immuunsysteem", "Veel vezels, dus lang een verzadigd gevoel"],
     "Combineer met citroen: vitamine C helpt je lichaam het ijzer op te nemen. Bevroren boerenkool werkt ook prima en koelt meteen je smoothie."),
    ("broccoli", "broccoli", "Broccoli", "groente", "2 roosjes",
     ["vezels", "vitamine A", "vitamine C", "foliumzuur", "sulforafaan", "flavonoïden"],
     ["Vezels dragen bij aan een goede spijsvertering",
      "Sulforafaan activeert de eigen antioxidatieve afweer van je lichaam",
      "Foliumzuur is extra belangrijk tijdens de zwangerschap", "Weinig calorieën: 43 kcal per kop"],
     "Gebruik ook de steel, daar zitten net zoveel voedingsstoffen in."),
    ("biet", "biet", "Biet (rauw)", "groente", "½ stuk",
     ["betalaïnen", "antioxidanten", "mangaan"],
     ["Antioxidanten helpen je cellen te beschermen tegen vrije radicalen",
      "Betalaïnen ondersteunen de ontstekingsremmende processen in je lichaam",
      "Mangaan helpt bij de verwerking van vitamine C en B1", "Stimuleert de spijsvertering"],
     "Altijd rauw gebruiken. Betalaïnen verdwijnen bij koken: na een uur is er vrijwel niets meer van over."),
    ("paprika", "paprika", "Paprika", "groente", "1 stuk",
     ["vitamine C", "vezels"],
     ["Vooral rode paprika zit boordevol vitamine C, goed voor je weerstand",
      "Veel vezels en voedingsstoffen, weinig calorieën"],
     "Paprika is familie van de rode peper, maar niet heet. Last van je maag bij rauwe paprika? Haal dan het velletje eraf."),
    ("venkel", "venkel", "Venkel", "groente", "½ stuk",
     ["vezels", "etherische oliën"],
     ["Brengt je darmen tot rust en helpt tegen winderigheid",
      "Staat bekend om het in balans brengen van vrouwelijke hormoonschommelingen",
      "Werkt eetlustopwekkend"],
     "Smaakt licht naar anijs. En je gaat er fris van ruiken."),
    ("witlof", "witlof", "Witlof", "groente", "",
     ["vitamine C", "kalium", "mineralen"],
     ["Kalium is nodig voor je spieren en zenuwstelsel en draagt bij aan een normale bloeddruk",
      "Handig na flink zweten, bijvoorbeeld bij duursport: dan verlies je extra kalium",
      "Extreem weinig calorieën"],
     "Te bitter? Haal de buitenste bladeren weg, snijd het kontje eraf en verwijder de kegelvormige kern. Bewaar witlof donker in de koelkast."),
    ("wortel", "wortel", "Wortel", "groente", "1 worteltje",
     ["vezels", "carotenoïden", "mineralen"],
     ["Carotenoïden worden in je lichaam omgezet in vitamine A, goed voor je ogen",
      "Boordevol vezels en mineralen",
      "Onderzoek wijst erop dat wortels de kwaliteit van sperma kunnen verbeteren"],
     "Rook je? Wees dan zuinig met wortelsap. De concentratie caroteen is daarin veel hoger. Te veel caroteen is voor rokers juist ongunstig."),
    ("peterselie", "peterselie", "Peterselie", "groente", "",
     ["vitamine C", "ijzer", "silicium", "B-vitaminen", "caroteen"],
     ["Uitzonderlijk veel vitamine C: 80 tot 300 mg per 100 gram",
      "IJzer helpt bij de aanmaak van rode bloedcellen", "Helpt een maaltijd sneller te verteren"],
     "Kauw na een avondje knoflook op een takje peterselie, dan ruik je weer fris."),
    ("gember", "gember", "Gemberwortel", "groente", "1 duimpje",
     ["gingerol", "shogaol", "vitamine B1, B2, B6 en C", "kalium", "magnesium", "zink"],
     ["Gingerol helpt tegen misselijkheid, ook bij reisziekte en zwangerschap",
      "Stimuleert de aanmaak van speeksel, waardoor je eten beter verteert",
      "Helpt tegen een opgeblazen gevoel", "Ondersteunt je weerstand, ook bij keelpijn en griepgevoel"],
     "Marco Polo zou gember als eerste vanuit China naar Europa hebben gebracht."),
    ("avocado", "avocado", "Avocado", "fruit", "",
     ["onverzadigde vetten", "kalium", "ijzer", "eiwit"],
     ["Onverzadigde vetten dragen bij aan een normaal cholesterolgehalte",
      "Gezonde vetten zijn goed voor je hersenen", "Ook goed voor je huid: daarom zit avocado in veel schoonheidsmaskers"],
     "Bij een rijpe avocado hoor je de pit rammelen als je schudt. Leuk weetje: de likeur advocaat dankt zijn naam aan de avocado."),
    ("banaan", "banaan", "Banaan", "fruit", "1 stuk",
     ["kalium", "vitamine B6", "vitamine A, B1, B2 en C", "tryptofaan", "vezels"],
     ["Geeft energie: zowel snelle als langzame suikers",
      "Vitamine B6 ondersteunt de samenwerking tussen zenuwen en spieren",
      "Kalium draagt bij aan een normale bloeddruk", "Vezels ondersteunen een goede stoelgang",
      "Tryptofaan is een bouwstof voor serotonine, het stofje dat je beter laat voelen"],
     "Hoe geler de banaan, hoe meer vitamine A. Vergeleken met een appel bevat een banaan vier keer zoveel eiwit en vijf keer zoveel ijzer."),
    ("blauwe-bessen", "blauwe-bessen", "Blauwe bessen", "fruit", "",
     ["antioxidanten", "vitamine A, B en C", "magnesium", "ijzer"],
     ["Van alle fruit het hoogste gehalte aan antioxidanten",
      "Antioxidanten beschermen je lichaam tegen oxidatieve stress, een van de oorzaken van veroudering",
      "Vitamine C draagt bij aan je weerstand"],
     "De blauwe bes komt uit Noord-Amerika en werd eerst vooral als kleurstof gebruikt."),
    ("citroen", "citroen", "Citroen", "fruit", "½ stuk",
     ["vitamine C", "flavonoïden", "rutine", "limoneen"],
     ["Vitamine C draagt bij aan je weerstand",
      "Vitamine C helpt je lichaam plantaardig ijzer op te nemen",
      "Stimuleert je darmen en een regelmatige stoelgang",
      "Antioxidanten gaan vrije radicalen tegen"],
     "Edmund Hillary, de eerste op de top van de Mount Everest, zei dat het zonder citroenen niet was gelukt."),
    ("kiwi", "kiwi", "Kiwi", "fruit", "1 stuk",
     ["vitamine C", "kalium", "foliumzuur", "magnesium", "zink", "vitamine E", "vezels"],
     ["Eén kiwi levert 166% van je dagelijkse behoefte aan vitamine C",
      "Vitamine C helpt bij de opname van ijzer en koper",
      "Kalium draagt bij aan een normale bloeddruk", "Een vetarme bron van vitamine E"],
     "Gooi de schil niet weg: de meeste vitamines zitten er net onder. Goed wassen en gewoon meeblenden."),
    ("goji", "goji", "Goji bes", "fruit", "2 eetlepels (20 g)",
     ["vitamine C, A, B1 en B2", "ijzer", "koper", "magnesium", "calcium", "aminozuren", "polysachariden"],
     ["Een van de meest voedingsrijke vruchten op aarde",
      "Polysachariden zorgen voor een geleidelijke stijging van je bloedsuiker",
      "Geeft lang een verzadigd gevoel"],
     "Ook gedroogd behoudt de goji bes bijna al zijn voedingswaarde."),
    ("amandel", "amandel", "Amandelen", "zaden", "10 stuks",
     ["eiwit (19,5%)", "vezels", "onverzadigde vetten", "vitamine E", "calcium", "kalium"],
     ["Vitamine E helpt je cellen te beschermen tegen oxidatieve schade",
      "Onverzadigde vetten dragen bij aan een normaal cholesterolgehalte",
      "Eiwit helpt je spiermassa te behouden, een goede vleesvervanger", "Van alle noten de meeste calcium",
      "Vezels geven een lang verzadigd gevoel"],
     "Eigenlijk geen noot maar een steenvrucht. Veel calorieën, dus met mate."),
    ("chia", "chia", "Chiazaad", "zaden", "max. 2 à 3 eetlepels per dag",
     ["omega-3", "eiwitten", "vezels (40%)", "vitaminen", "mineralen"],
     ["De rijkste plantaardige bron van omega-3 vetzuren, goed voor hart en bloedvaten",
      "Eiwitten ondersteunen je spierherstel", "Vezels zijn goed voor je darmwerking",
      "Geeft lang een vol gevoel en minder trek in zoetigheid"],
     "Laat de zaadjes 10 minuten weken in koud water. Ze worden dan gelachtig en je lichaam neemt de voedingsstoffen makkelijker op. Niet meer dan 2 à 3 eetlepels per dag en wissel af met lijnzaad."),
    ("hennepzaad", "hennepzaad", "Hennepzaad", "zaden", "",
     ["complete eiwitten", "essentiële vetzuren", "gamma-linoleenzuur", "magnesium", "zink", "vitamine E, C en B"],
     ["Een complete eiwitbron met alle essentiële aminozuren",
      "Het hoogste percentage essentiële vetzuren van vrijwel elk zaad, een goed alternatief voor vis",
      "Mineralen als fosfor, calcium en magnesium zijn goed voor je botten"],
     "Hennep groeit zonder pesticiden en is dus duurzaam. Hennep is niet hetzelfde als marihuana: het verschil zit in het THC-gehalte."),
    ("lijnzaad", "lijnzaad", "Lijnzaad", "zaden", "2 eetlepels",
     ["omega-3", "omega-6", "vitamine B1 en B2", "calcium", "magnesium", "zink", "kalium"],
     ["Omega-3 vetzuren zijn goed voor je ogen, je hersenen en je hormoonhuishouding"],
     "Koop heel lijnzaad en kneus het vlak voor gebruik, of gooi het zo in de blender. Gebroken lijnzaad oxideert en verliest zijn waarde. Drink er ruim water bij."),
    ("pompoenpitten", "pompoenpitten", "Pompoenpitten", "zaden", "",
     ["vitamine E", "mangaan", "magnesium", "ijzer", "zink", "koper", "fosfor"],
     ["100 gram bevat 237% van je dagelijkse behoefte aan vitamine E",
      "Rijk aan magnesium en ijzer: goed tegen vermoeidheid",
      "Zink draagt bij aan een normaal testosterongehalte"],
     "De percentages gelden voor 100 gram. Een handje in je smoothie is dus een deel daarvan."),
    ("bijenpollen", "bijenpollen", "Bijenpollen", "superfood", "",
     ["vitamine A, B, C, D en E", "selenium", "calcium", "magnesium", "enzymen", "aminozuren"],
     ["Vitaminen dragen bij aan je energie, spijsvertering en weerstand",
      "Calcium en magnesium zijn goed voor stevige botten",
      "Selenium helpt je cellen te beschermen", "Caloriearm"],
     "Ook puur te eten. Allergisch voor bijenproducten? Sla dit ingrediënt dan over."),
    ("chlorella", "chlorella", "Chlorella poeder", "superfood", "2 theelepels (10 g)",
     ["eiwit (60%)", "chlorofyl", "zink", "vitaminen", "mineralen", "aminozuren"],
     ["Zink draagt bij aan gezonde huid, haar en nagels",
      "Helpt de opname van ijzer uit bladgroenten",
      "Ondersteunt je immuunsysteem", "De rijkste natuurlijke bron van chlorofyl"],
     "Chlorella is een eencellige alg uit zoetwatervijvers. De smaak is intens, dus houd je aan de portie."),
    ("hennep-eiwit", "hennep-eiwit", "Hennep eiwit", "superfood", "1 à 2 eetlepels (20-30 g)",
     ["eiwit (50%)", "alle essentiële aminozuren", "omega-3 en omega-6", "ijzer", "magnesium", "zink"],
     ["Een van de rijkste bronnen van plantaardige eiwitten, populair bij sporters",
      "Eiwit draagt bij aan opbouw en behoud van spiermassa",
      "Glutenvrij en geschikt bij lactose-intolerantie en voor vegetariërs"],
     "Gemaakt van de pulp die overblijft na het koud persen van hennepolie."),
    ("maca", "maca", "Maca poeder", "superfood", "1 eetlepel",
     ["ijzer", "calcium", "vitamine B3", "enzymen", "essentiële aminozuren"],
     ["Een echt energiebommetje", "Staat bekend om het verminderen van stressgevoel",
      "Wordt van oudsher gebruikt om het libido te verhogen"],
     "Maca groeit in Peru boven de 2.500 meter. De Inca's gaven het hun krijgers voor energie en kracht."),
    ("tarwegras", "tarwegras", "Tarwegras", "superfood", "",
     ["vitamine A, B, C, E en K", "ijzer", "kalium", "calcium", "magnesium", "zink"],
     ["Bevat een goede balans van de vitaminen en mineralen die je nodig hebt",
      "Een energieboost", "Staat bekend om zijn reinigende werking"],
     "Tarwegras zijn de jonge scheuten van de tarweplant."),
    ("kokoswater", "kokoswater", "Kokoswater", "basis", "¼ liter",
     ["kalium", "calcium", "magnesium", "natrium", "vitamine B2", "fosfor"],
     ["Hydrateert sterk, ideaal voor sporters",
      "Kalium draagt bij aan een normale bloeddruk en spierwerking",
      "Helpt bij herstel na inspanning", "Bijna geen vet"],
     "500 ml kokoswater bevat evenveel kalium als 3 bananen. Het bevat wel natuurlijke suikers, dus niet te veel per dag."),
    ("kokosvet", "kokosvet", "Kokosolie", "basis", "",
     ["MCT-vetzuren", "laurinezuur (50%)"],
     ["Helpt je lichaam calcium, magnesium en de vitamines A, D, E en K op te nemen",
      "Laurinezuur ondersteunt je weerstand",
      "MCT-vetzuren breekt je lichaam makkelijker af dan de meeste andere verzadigde vetten"],
     "Koud gebruiken? Kies de ongeraffineerde, niet-ontgeurde versie. Kokosolie is ook goed om in te bakken."),
    ("olijfolie", "olijfolie", "Olijfolie (koud geperst)", "basis", "4 eetlepels (50 ml)",
     ["enkelvoudig onverzadigde vetzuren", "antioxidanten"],
     ["Onverzadigde vetzuren dragen bij aan een normaal cholesterolgehalte",
      "Antioxidanten beschermen je cellen tegen veroudering",
      "Bevat een stof met een ontstekingsremmende werking"],
     "Koude olijfolie is veel gezonder dan verhitte. Kies daarom altijd koud geperst."),
]
CATS = [("alle", "Alles"), ("groente", "Groente"), ("fruit", "Fruit"), ("zaden", "Zaden & noten"),
        ("superfood", "Poeders & superfoods"), ("basis", "Vloeistof & olie")]


def ingredienten():
    knoppen = "".join(f'<button type="button" data-cat="{c}" aria-pressed="{str(c == "alle").lower()}">{n}</button>' for c, n in CATS)
    catnaam = dict(CATS)

    def kaart(anker, img, naam, cat, portie, rijk, doet, tip):
        chips = "".join(f"<li>{r}</li>" for r in rijk)
        lijst = "".join(f"<li>{d}</li>" for d in doet)
        port = f'<span class="label">Per smoothie: {portie}</span>' if portie else ""
        return f"""<article class="ing reveal" id="{anker}" data-cat="{cat}">
  <div class="ing-kop"><img src="assets/img/ing/{img}.webp" alt="{naam}" loading="lazy">
    <div><span class="kicker">{catnaam[cat]}</span><h3>{naam}</h3>{port}</div></div>
  <p class="ing-sub">Rijk aan</p><ul class="chips">{chips}</ul>
  <p class="ing-sub">Wat doet het voor je lijf?</p><ul class="vink klein-vink">{lijst}</ul>
  <p class="ing-tip"><strong>Goed om te weten:</strong> {tip}</p>
</article>"""

    tegels = "".join(kaart(*i) for i in INGR)
    index = " · ".join(f'<a href="#{i[0]}">{i[2]}</a>' for i in sorted(INGR, key=lambda x: x[2]))
    inhoud = f"""
<section class="pagina-hero">
  <img class="bg" src="assets/img/jm-pepers.webp" alt="" fetchpriority="high">
  <div class="wrap">
    <div class="kruimel"><a href="index.html">Home</a> / Ingrediënten</div>
    <h1>Onze <span class="markeer">nuttige</span> ingrediënten</h1>
    <p>29 ingrediënten, gewoon verkrijgbaar in Nederland en betaalbaar. Per ingrediënt zie je wat erin zit, wat het voor je lijf doet en hoeveel je per smoothie gebruikt.</p>
  </div>
</section>

<section class="sectie wit">
  <div class="wrap">
    <div class="split" style="margin-bottom:48px">
      <div>
        <span class="kicker">Nut boven smaak</span>
        <h2>Elk ingrediënt heeft een reden</h2>
      </div>
      <div>
        <p>Groente en fruit bevatten vrijwel alle voedingsstoffen die je lichaam nodig heeft. Veel daarvan gaan verloren bij koken en bakken. In de blender blijven ze heel. Met voldoende water erbij drink je ze zo weg.</p>
        <p>In onze Smoothie Configurators bepaalt het doel van je smoothie welke ingrediënten erin gaan. Niet de smaak. Hieronder zie je waarom.</p>
      </div>
    </div>
    <div class="filters" role="group" aria-label="Filter op soort">{knoppen}</div>
    <p class="ing-index klein">{index}</p>
    <div class="raster r2 ing-raster">{tegels}</div>
    <p class="melding" style="margin-top:36px">Smoothieclub geeft geen medisch advies. Een smoothie is een aanvulling op een gevarieerd eetpatroon, geen vervanging en geen medicijn. Gebruik je medicijnen, ben je zwanger of heb je een allergie? Overleg dan eerst met je arts.</p>
  </div>
</section>

<section class="sectie">
  <div class="wrap split">
    <div class="reveal"><img class="foto" src="assets/img/kids-praktijk.webp" alt="De KIDS Smoothie Configurator in gebruik in de keuken" loading="lazy"></div>
    <div class="reveal">
      <span class="kicker">Aan de slag</span>
      <h2>Welke blend past bij jouw doel?</h2>
      <p>In de Smoothie Configurator zie je per doel welke ingrediënten je gebruikt en in welke hoeveelheid. Zo maak je in een paar minuten een smoothie die ergens voor dient.</p>
      <div class="knoppen"><a class="knop primair" href="webshop.html">Naar de Configurators</a></div>
    </div>
  </div>
</section>
"""
    return layout("ingredienten.html", "Nuttige ingrediënten voor gezonde smoothies | Smoothieclub",
                  "29 nuttige smoothie-ingrediënten: wat erin zit, wat het voor je lichaam doet en hoeveel je per smoothie gebruikt. Van boerenkool en gember tot chiazaad en kokoswater.",
                  inhoud, ORG)


def over():
    inhoud = f"""
<section class="pagina-hero">
  <img class="bg" src="assets/img/hero-event.webp" alt="" fetchpriority="high">
  <div class="wrap">
    <div class="kruimel"><a href="index.html">Home</a> / Over ons</div>
    <h1>Smoothieclub is all about <span class="markeer">blending together</span></h1>
    <p>Mens, organisatie, gezondheid en duurzaamheid samen in één blend. Van weerstand naar beweging.</p>
  </div>
</section>

<section class="sectie wit">
  <div class="wrap split">
    <div class="reveal">
      <span class="kicker">Onze missie</span>
      <h2>Mensen in beweging, van binnenuit</h2>
      <p class="intro">Smoothieclub motiveert mensen om verantwoordelijkheid te nemen voor hun eigen gedrag en voor hun fysieke én mentale gezondheid. En ja, we stimuleren ook het eten van groente en fruit.</p>
      <p>Wie zich fit voelt, presteert beter. Wie zelf kiest, houdt het langer vol. Daarom leggen wij niets op. We laten mensen ervaren, proeven en zelf ontdekken. Dat levert gemotiveerde medewerkers op die open staan voor verandering.</p>
    </div>
    <div class="reveal">
      <div class="raster r2">
        <div class="feit" style="--c:var(--roze)"><strong>Events met passie</strong><span>Energie die blijft hangen</span></div>
        <div class="feit" style="--c:var(--oranje)"><strong>Elke groep</strong><span>Van 8 tot 500 deelnemers</span></div>
        <div class="feit" style="--c:var(--geel)"><strong>Verfrissend</strong><span>Anders dan anders</span></div>
        <div class="feit" style="--c:var(--groen)"><strong>Elke locatie</strong><span>Wij nemen alles mee</span></div>
      </div>
    </div>
  </div>
</section>

<section class="sectie">
  <div class="wrap split omgekeerd">
    <div class="reveal"><img class="foto" src="assets/img/jm-pepers.webp" alt="Jean-Marc Bilderbeek" loading="lazy"></div>
    <div class="reveal">
      <span class="kicker">De oprichter</span>
      <h2>Het verhaal van Jean-Marc</h2>
      <p>In 2008 kreeg Jean-Marc Bilderbeek zijn eerste epileptische aanval. Hij had een druk leven als projectleider en trainer. Na de diagnose kwamen de medicijnen, de aanvallen en de vraag: hoe nu verder?</p>
      <p>Hij besloot zelf te veranderen. Hij ging op zoek, stapte uit zijn comfortzone en liet aannames los. In 2012 maakte hij zijn eerste smoothie. In 2013 gaf hij zijn eerste Smoothieclub-workshop in Amsterdam.</p>
      <p>Wat hij leerde over keuzes en verantwoordelijkheid bleek precies te passen bij wat teams doormaken bij verandering. Zo ontstond Smoothieclub: de smoothie als metafoor voor de ideale blend van mensen en ideeën.</p>
      <p><strong>"Mensen willen wel veranderen, maar niet veranderd worden."</strong></p>
    </div>
  </div>
</section>

<section class="sectie wit">
  <div class="wrap" style="max-width:900px">
    <div class="center"><span class="kicker">Onze definitie</span>
      <p class="slogan">"Een smoothie is een vloeibaar voedingsmiddel van in Nederland verkrijgbare, betaalbare én effectieve ingrediënten, samengesteld op de gewenste combinatie van nut, smaak en prijs."</p>
    </div>
  </div>
</section>

<section class="sectie groen">
  <div class="wrap split">
    <div class="reveal">
      <span class="kicker">Duurzaam blenden</span>
      <h2>3.000 bomen en tellen</h2>
      <p>Voor elke verkochte Configurator en elke Mystery Box-deelnemer planten we een jonge boom via AfricaWoodGrow in Kenia. Een deel van de Mystery Box-inhoud wordt gemaakt door Rotterdammers met een afstand tot de arbeidsmarkt. En we gebruiken zo min mogelijk plastic en zoveel mogelijk gerecycled papier.</p>
    </div>
    <div class="reveal">
      <span class="kicker">Onderdeel van Kaderloos</span>
      <h2>Verandering zit in ons DNA</h2>
      <p>Smoothieclub is onderdeel van Kaders B.V., de veranderorganisatie achter Kaderloos en Blending Forces. Sinds 2008 werkten we voor zo'n 150 organisaties, van ministeries en gemeenten tot Google en Salesforce.</p>
      <div class="knoppen"><a class="knop licht" href="https://www.kaderloos.nl" rel="noopener">Naar kaderloos.nl</a></div>
    </div>
  </div>
</section>

<section class="sectie">
  <div class="wrap">
    <p class="center klein" style="margin-bottom:18px">Onder meer vertrouwd door</p>
    {logos()}
  </div>
</section>
{cta()}
"""
    return layout("over.html", "Over Smoothieclub en oprichter Jean-Marc Bilderbeek",
                  "Smoothieclub motiveert mensen en teams om verantwoordelijkheid te nemen voor gedrag en gezondheid. Het verhaal van oprichter Jean-Marc Bilderbeek en onze missie.",
                  inhoud, ORG)


# ---------------------------------------------------------------- CONTACT
def contact():
    types = ["Workshop Smoothen Your Life", "Teamworkshop Smoothen Your Business", "Keynote", "Blendbox", "Mystery Box", "Weet ik nog niet"]
    radio = "".join(f'<label><input type="radio" name="type" value="{t}"{" required" if i == 0 else ""}><span>{t}</span></label>' for i, t in enumerate(types))
    inhoud = f"""
<section class="sectie" style="padding-top:64px">
  <div class="wrap split" style="align-items:start">
    <div>
      <span class="kicker">Contact</span>
      <h1>Let's blend!</h1>
      <p class="intro">Vertel ons wat je zoekt. Je krijgt binnen 1 werkdag een reactie, meestal met een voorstel op maat.</p>
      <ul class="vink">
        <li>Je spreekt Jean-Marc zelf, geen tussenpersoon</li>
        <li>Alles inbegrepen: reistijd, groente, fruit, blenders en materialen</li>
        <li>Vrijblijvend, je zit nergens aan vast</li>
      </ul>
      <div class="cta-blok compact">
        <img class="jm" src="assets/img/jm-portret.webp" alt="Jean-Marc Bilderbeek" width="300" height="300">
        <div class="contactregel">
          <strong style="color:#fff;font-size:1.1rem">Liever direct contact?</strong>
          <a href="{TEL_LINK}">📞 {TEL}</a>
          <a href="{WA}" rel="noopener">💬 WhatsApp</a>
          <a href="mailto:{MAIL}">✉ {MAIL}</a>
        </div>
      </div>
      <h3 style="margin-top:32px">Volg ons</h3>
      <p>Recepten, tips en een kijkje achter de schermen bij onze workshops.</p>
      {social_iconen("social donker")}
      <p style="margin-top:12px"><a href="https://www.facebook.com/groups/493784564004776" rel="noopener" target="_blank">Word lid van onze Facebook-groep</a> en blend mee met andere smoothie-fans.</p>
      <p class="klein" style="margin-top:24px">Smoothieclub is onderdeel van Kaders B.V., Rotterdam · KvK 51210010 · <a href="https://www.kaderloos.nl" rel="noopener">kaderloos.nl</a></p>
    </div>
    <form class="formulier" id="offerte" novalidate>
      <h2 style="font-size:1.6rem">Vraag een voorstel aan</h2>
      <div class="veld"><label>Waar ben je naar op zoek? *</label><div class="keuze">{radio}</div></div>
      <div class="twee">
        <div class="veld"><label for="aantal">Aantal deelnemers</label><input id="aantal" name="aantal" type="number" min="1" inputmode="numeric" placeholder="bv. 40"></div>
        <div class="veld"><label for="datum">Gewenste datum</label><input id="datum" name="datum" type="text" placeholder="bv. half november"></div>
      </div>
      <div class="veld"><label for="locatie">Locatie</label><input id="locatie" name="locatie" type="text" placeholder="Plaats of online"></div>
      <div class="veld"><label for="bericht">Wat moet de sessie opleveren?</label><textarea id="bericht" name="bericht" rows="4" placeholder="Vertel kort over je team, de aanleiding en je doel"></textarea></div>
      <div class="twee">
        <div class="veld"><label for="naam">Naam *</label><input id="naam" name="naam" type="text" autocomplete="name" required></div>
        <div class="veld"><label for="organisatie">Organisatie</label><input id="organisatie" name="organisatie" type="text" autocomplete="organization"></div>
      </div>
      <div class="twee">
        <div class="veld"><label for="email">E-mail *</label><input id="email" name="email" type="email" autocomplete="email" required></div>
        <div class="veld"><label for="telefoon">Telefoon</label><input id="telefoon" name="telefoon" type="tel" autocomplete="tel"></div>
      </div>
      <button class="knop primair" type="submit" style="width:100%;justify-content:center">Verstuur mijn aanvraag</button>
      <p class="klein" style="margin-top:12px">Je mailprogramma opent met je aanvraag erin. Je gegevens gebruiken we alleen om je aanvraag te beantwoorden.</p>
      <p class="melding" id="bedankt" hidden>Dank je wel! Verstuur de mail die net is geopend. Opent er niets? Mail dan naar {MAIL} of bel {TEL}.</p>
    </form>
  </div>
</section>
"""
    return layout("contact.html", "Contact en voorstel aanvragen | Smoothieclub",
                  "Vraag een voorstel aan voor een teamworkshop, keynote of Blendbox. Reactie binnen 1 werkdag. Bel of app 06-50745730 of mail info@smoothieclub.nl.",
                  inhoud, ORG)


def fout():
    inhoud = """
<section class="sectie center">
  <div class="wrap">
    <span class="kicker">404</span>
    <h1>Deze blend bestaat niet</h1>
    <p class="intro">De pagina die je zoekt is er niet (meer). Geen zorgen, we helpen je verder.</p>
    <div class="knoppen" style="justify-content:center"><a class="knop primair" href="index.html">Naar de homepage</a><a class="knop rand" href="contact.html">Contact</a></div>
  </div>
</section>"""
    return layout("404.html", "Pagina niet gevonden | Smoothieclub", "Deze pagina bestaat niet.", inhoud)


PAGINAS = {"index.html": home, "workshops.html": workshops, "keynote.html": keynote, "blendbox.html": blendbox,
           "webshop.html": webshop, "ingredienten.html": ingredienten, "over.html": over, "contact.html": contact,
           "404.html": fout}

if __name__ == "__main__":
    for naam, fn in PAGINAS.items():
        html = fn()
        assert "—" not in html, f"em dash in {naam}"
        zichtbaar = re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", "", html, flags=re.S))
        fout = re.search(r".{0,40},\s+en\b.{0,20}", zichtbaar)
        assert not fout, f'", en" in {naam}: {fout.group(0) if fout else ""}'  # huisstijl JM: nooit komma voor "en"
        (ROOT / naam).write_text(html, encoding="utf-8")
        print("gebouwd:", naam)
