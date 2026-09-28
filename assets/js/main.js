// Smoothieclub concept: menu, video's, ingrediëntfilter, offerteformulier
(function () {
  // Mobiel menu
  var knop = document.querySelector('.hamburger');
  var menu = document.getElementById('menu');
  if (knop && menu) {
    knop.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      knop.setAttribute('aria-expanded', open);
    });
  }

  // Rustig inschuiven bij scrollen
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('zichtbaar'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('zichtbaar'); });
  }

  // YouTube pas laden na klik (sneller en privacyvriendelijk)
  document.querySelectorAll('.video[data-yt]').forEach(function (v) {
    v.addEventListener('click', function () {
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + v.dataset.yt + '?autoplay=1&rel=0';
      f.allow = 'autoplay; encrypted-media; picture-in-picture';
      f.allowFullscreen = true;
      f.title = v.getAttribute('aria-label') || 'Video';
      v.innerHTML = '';
      v.appendChild(f);
    }, { once: true });
  });

  // Filter op de ingrediëntenpagina
  var filters = document.querySelectorAll('.filters button');
  filters.forEach(function (b) {
    b.addEventListener('click', function () {
      filters.forEach(function (x) { x.setAttribute('aria-pressed', x === b); });
      var cat = b.dataset.cat;
      document.querySelectorAll('.ing').forEach(function (i) {
        i.hidden = cat !== 'alle' && i.dataset.cat !== cat;
      });
    });
  });

  // Klik in de ingrediëntenindex: filter terug op "Alles" zodat de kaart zichtbaar is
  document.querySelectorAll('.ing-index a').forEach(function (a) {
    a.addEventListener('click', function () {
      var alle = document.querySelector('.filters button[data-cat="alle"]');
      if (alle) alle.click();
    });
  });

  // Offerteformulier: vooraf invullen via ?type=... en versturen als e-mail
  var form = document.getElementById('offerte');
  if (form) {
    var type = new URLSearchParams(location.search).get('type');
    if (type) {
      var r = form.querySelector('input[name="type"][value="' + type + '"]');
      if (r) r.checked = true;
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var d = new FormData(form);
      var regels = [
        'Waar ben je naar op zoek: ' + (d.get('type') || '-'),
        'Aantal deelnemers: ' + (d.get('aantal') || '-'),
        'Gewenste datum: ' + (d.get('datum') || '-'),
        'Locatie: ' + (d.get('locatie') || '-'),
        '',
        'Toelichting:',
        d.get('bericht') || '-',
        '',
        'Naam: ' + d.get('naam'),
        'Organisatie: ' + (d.get('organisatie') || '-'),
        'E-mail: ' + d.get('email'),
        'Telefoon: ' + (d.get('telefoon') || '-')
      ];
      var onderwerp = 'Voorstel aanvragen: ' + (d.get('type') || 'Smoothieclub') + (d.get('organisatie') ? ' voor ' + d.get('organisatie') : '');
      location.href = 'mailto:info@smoothieclub.nl?subject=' + encodeURIComponent(onderwerp) + '&body=' + encodeURIComponent(regels.join('\n'));
      var ok = document.getElementById('bedankt');
      if (ok) ok.hidden = false;
    });
  }

  var jaar = document.getElementById('jaar');
  if (jaar) jaar.textContent = new Date().getFullYear();
})();
