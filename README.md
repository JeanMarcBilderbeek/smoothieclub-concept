# Smoothieclub: conceptwebsite

Verbeterde testversie van [smoothieclub.nl](https://www.smoothieclub.nl), gebouwd door Claudia (Claude Code) als proef.
De originele WordPress-site is niet aangeraakt. Alle teksten en beelden zijn van smoothieclub.nl overgenomen en herschreven.

**Live:** https://jeanmarcbilderbeek.github.io/smoothieclub-concept/

## Wat is er anders dan de huidige site?

- Heldere belofte bovenaan ("Gezonde teams blenden beter") met twee routes: organisaties en thuis
- Eén duidelijke hoofdactie op elke pagina: *Vraag een voorstel aan* (reactie binnen 1 werkdag)
- Vergelijkingstabel van alle formats (keynote, twee workshops, Blendbox/Mystery Box)
- Sociaal bewijs: klantlogo's, 8,4 waardering, reviews, 3.000 bomen
- Offerteformulier dat de juiste vragen stelt (format, aantal, datum, locatie, doel)
- WhatsApp-knop en overal hetzelfde telefoonnummer en mailadres
- Consequent "je", geen corona-tekst, geen medische claims, geen woonadres of IBAN
- Snel: statische pagina's, beelden in WebP, video laadt pas na klik
- SEO-basis: titels, meta descriptions, alt-teksten, structured data (Organization, FAQ, Product)

## Techniek

- Statische HTML/CSS/JS, gehost op GitHub Pages
- Pagina's worden gegenereerd met `python tools/build.py` (kop, voet en teksten staan in dat script)
- Bestellen gaat via de bestaande WooCommerce-webshop op smoothieclub.nl
- `noindex` en `robots.txt` staan aan, zodat deze test niet concurreert met de echte site in Google
