# Bouwt alle HTML-pagina's van de Smoothieclub-conceptsite.
# Gebruik: python tools/build.py  (vanuit de hoofdmap van de repo)
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHOP = "https://www.smoothieclub.nl/product/"
TEL = "06-50745730"
TEL_LINK = "tel:+31650745730"
WA = "https://wa.me/31650745730?text=Hoi%20Jean-Marc%2C%20ik%20heb%20een%20vraag%20over%20Smoothieclub"
MAIL = "info@smoothieclub.nl"

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
        <li><a href="https://www.youtube.com/c/JeanMarcBilderbeek" rel="noopener">YouTube</a></li>
        <li><a href="https://www.linkedin.com/in/jmbilderbeek" rel="noopener">LinkedIn</a></li>
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
    ("smoothie-configurator-nl", "p-configurator", "Smoothie Configurator", "16+", "Klassieker",
     "14 doelgerichte smoothies op basis van 23 ingrediënten uit de supermarkt. Meer energie, een frisse start na een feestje of juist een stevig ontbijt: je ziet in één oogopslag wat erin gaat. Gemaakt op nut, niet op smaak. Durf jij het aan?",
     "8,75", "PDF € 8,75 · gelamineerd € 12,50"),
    ("kids-smoothie-configurator", "p-kids", "KIDS Smoothie Configurator", "8+", "",
     "Hét hulpmiddel om kinderen meer groente en fruit te laten eten. 15 ingrediënten, elke blend bevat een portie groente en wordt toegankelijk gemaakt met zoet fruit. Laat je kind kiezen: vandaag sterk, slim of cool?",
     "8,75", "PDF € 8,75 · gelamineerd € 12,50"),
    ("kids-smoothie-challenge", "p-challenge", "KIDS Smoothie Challenge", "6+", "",
     "In 8 levels leren de jongste kids zelf smoothies maken. Elke dag een level, en na 8 dagen verdienen ze een echt Smoothie Certificaat. Uitdagend, cool en belonend. Altijd samen met een volwassene snijden en blenden.",
     "8,75", "PDF € 8,75 · gelamineerd € 10,95"),
    ("smoothieclub-totaalpakket", "p-totaal", "Totaalpakket voor het hele gezin", "6+ tot 99", "Voordeligst",
     "Alle drie de Configurators in één pakket: de Challenge, de KIDS Configurator en de Smoothie Configurator voor volwassenen. Het hele gezin kan direct aan de slag.",
     "19,95", "PDF € 19,95 · gelamineerd € 27,50"),
]


def webshop():
    kaarten = "".join(f"""
      <article class="product reveal"{' id="kids"' if slug.startswith('kids-smoothie-c') else ''}>
        {f'<span class="lint">{lint}</span>' if lint else ''}
        <img src="assets/img/{img}.webp" alt="{naam}" loading="lazy" width="700" height="700">
        <div class="in">
          <span class="label" style="align-self:flex-start;margin-bottom:10px">Leeftijd {leeftijd}</span>
          <h3>{naam}</h3>
          <p>{tekst}</p>
          <div class="prijs">vanaf € {prijs}</div>
          <div class="varianten">{var}</div>
          <a class="knop primair klein" href="{SHOP}{slug}/" rel="noopener">Bestellen</a>
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
    <h1>Supergezonde smoothies, <span class="markeer">in één oogopslag</span></h1>
    <p>Met de Smoothie Configurator weet je precies wat erin gaat en hoeveel. Voor jezelf, voor je kinderen of voor het hele gezin.</p>
    <div class="knoppen"><a class="knop primair" href="#producten">Bekijk de Configurators</a></div>
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
      <span class="kicker">Onze Configurators</span>
      <h2>Kies je Configurator</h2>
      <p class="intro">Alle prijzen zijn inclusief btw. Bij de gelamineerde versie komen verzendkosten erbij.</p>
    </div>
    <div class="raster r4">{kaarten}</div>
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
    return layout("webshop.html", "Webshop: Smoothie Configurators voor volwassenen en kinderen | Smoothieclub",
                  "Bestel de Smoothie Configurator, de KIDS Configurator, de Smoothie Challenge of het Totaalpakket. Direct als PDF vanaf € 8,75 of gelamineerd. Per Configurator een boom in Kenia.",
                  inhoud, [ORG] + prod_schema)


# ---------------------------------------------------------------- INGREDIENTEN
INGR = [
    ("bleekselderij", "Bleekselderij", "groente", "Fris en licht zoutig. Veel vocht, mooie basis."),
    ("boerenkool", "Boerenkool", "groente", "Stevig groen. Rauw prima te blenden."),
    ("broccoli", "Broccoli", "groente", "Groene kracht. Gebruik ook de steel."),
    ("biet", "Biet", "groente", "Aards en zoetig. Geeft een diepe kleur."),
    ("paprika", "Paprika", "groente", "Zoet en fris. Rood of geel werkt het best."),
    ("venkel", "Venkel", "groente", "Licht anijs. Verrassend fris."),
    ("witlof", "Witlof", "groente", "Licht bitter. Mooi tegenwicht voor zoet fruit."),
    ("wortel", "Wortel", "groente", "Zoet en oranje. Kinderen vinden hem vaak lekker."),
    ("peterselie", "Peterselie", "groente", "Frisse kruidenkick. Een handje is genoeg."),
    ("tarwegras", "Tarwegras", "superfood", "Intens groen. Gebruik een kleine dosis."),
    ("avocado", "Avocado", "fruit", "Maakt elke blend romig en vol."),
    ("banaan", "Banaan", "fruit", "Zoet en romig. Een natuurlijke binder."),
    ("blauwe-bessen", "Blauwe bessen", "fruit", "Zoetzuur. Diepvries werkt ook prima."),
    ("citroen", "Citroen", "fruit", "Frisse zuren die groene smaken oppeppen."),
    ("kiwi", "Kiwi", "fruit", "Fris en zuur. Met schil blenden kan."),
    ("goji", "Goji bes", "fruit", "Gedroogd. Licht zoet en zuur."),
    ("gember", "Gemberwortel", "fruit", "Pittig en warm. Begin met een klein stukje."),
    ("amandel", "Amandelen", "zaden", "Nootachtig en romig. Even weken helpt."),
    ("chia", "Chiazaad", "zaden", "Maakt je smoothie dikker. Laat even staan."),
    ("hennepzaad", "Hennepzaad", "zaden", "Mild en nootachtig."),
    ("lijnzaad", "Lijnzaad", "zaden", "Liefst gemalen. Mild van smaak."),
    ("pompoenpitten", "Pompoenpitten", "zaden", "Groen, nootachtig en knapperig."),
    ("bijenpollen", "Bijenpollen", "superfood", "Bloemig en zoet. Een theelepel is genoeg."),
    ("chlorella", "Chlorella poeder", "superfood", "Zeer intens groen. Echt een mespuntje."),
    ("hennep-eiwit", "Hennep eiwit", "superfood", "Plantaardig poeder, aards van smaak."),
    ("maca", "Maca poeder", "superfood", "Moutig, met een tikje karamel."),
    ("kokoswater", "Kokoswater", "basis", "Licht zoete vloeistof. Alternatief voor water."),
    ("kokosvet", "Kokosolie", "basis", "Geeft body. Een theelepel is genoeg."),
    ("olijfolie", "Olijfolie (koud geperst)", "basis", "Een scheutje maakt groene blends zachter."),
]
CATS = [("alle", "Alles"), ("groente", "Groente"), ("fruit", "Fruit"), ("zaden", "Zaden & noten"),
        ("superfood", "Poeders & superfoods"), ("basis", "Vloeistof & olie")]


def ingredienten():
    knoppen = "".join(f'<button type="button" data-cat="{c}" aria-pressed="{str(c == "alle").lower()}">{n}</button>' for c, n in CATS)
    tegels = "".join(f'<article class="ing" data-cat="{cat}"><img src="assets/img/ing/{img}.webp" alt="" loading="lazy"><h3>{naam}</h3><p>{t}</p></article>'
                     for img, naam, cat, t in INGR)
    inhoud = f"""
<section class="pagina-hero">
  <img class="bg" src="assets/img/jm-pepers.webp" alt="" fetchpriority="high">
  <div class="wrap">
    <div class="kruimel"><a href="index.html">Home</a> / Ingrediënten</div>
    <h1>Onze <span class="markeer">nuttige</span> ingrediënten</h1>
    <p>Gewoon te koop in Nederland, betaalbaar en met een reden in de blend. Dit zijn de 29 ingrediënten waarmee wij werken.</p>
  </div>
</section>

<section class="sectie wit">
  <div class="wrap">
    <div class="split" style="margin-bottom:56px">
      <div>
        <span class="kicker">The smooth way</span>
        <h2>Meer rauwe groente, zonder gedoe</h2>
      </div>
      <div>
        <p>Groente en fruit rauw eten is een goed idee. Maar wie eet er nou een krop boerenkool? Met voldoende water in de blender gaat het ineens heel makkelijk. Combineer zelf zoveel mogelijk, of gebruik onze Configurators als startpunt.</p>
        <p class="klein">Tip: begin met veel groente en weinig fruit. Je smaak went sneller dan je denkt.</p>
      </div>
    </div>
    <div class="filters" role="group" aria-label="Filter op soort">{knoppen}</div>
    <div class="raster r4">{tegels}</div>
    <p class="melding" style="margin-top:36px">Smoothieclub geeft geen medisch advies. Een smoothie is een aanvulling op een gevarieerd eetpatroon, geen vervanging. Gebruik je medicijnen of heb je een allergie? Overleg dan eerst met je arts.</p>
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
    return layout("ingredienten.html", "Ingrediënten voor gezonde smoothies | Smoothieclub",
                  "De 29 ingrediënten waarmee Smoothieclub werkt: groente, fruit, zaden, poeders en olie. Betaalbaar, gewoon verkrijgbaar en met een reden in de blend.",
                  inhoud, ORG)


# ---------------------------------------------------------------- OVER
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
        (ROOT / naam).write_text(html, encoding="utf-8")
        print("gebouwd:", naam)
