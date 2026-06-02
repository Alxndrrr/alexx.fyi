# Agent Log

Dit bestand houdt bij wat er is gemaakt, waarom het is gemaakt en wat elk onderdeel doet.

## 2026-06-02

### Doel

Een mobile-first Jekyll theme maken voor `alexx.fyi` dat direct op GitHub Pages gebruikt kan worden.

### Gemaakt

- `_config.yml`: centrale instellingen voor titel, auteur, navigatie, social links, permalink-structuur, plugins en defaults.
- `Gemfile`: gebruikt de `github-pages` gem zodat lokaal bouwen zo dicht mogelijk bij GitHub Pages blijft.
- `_layouts/default.html`: basisframe met head, header, main en footer.
- `_layouts/home.html`: homepage met introblok en de nieuwste blogposts.
- `_layouts/archive.html`: blogoverzicht voor alle posts.
- `_layouts/post.html`: blogtemplate met datum boven titel en categorieen onder titel.
- `_layouts/page.html`: template voor gewone pagina's.
- `_includes/header.html`: logo, naam en hoofdmenu.
- `_includes/footer.html`: footer met Font Awesome iconen voor Threads, RSS en mail.
- `_includes/post-card.html`: herbruikbaar blok voor blogvermeldingen.
- `_sass/_alexx.scss`: alle theme-styling, mobile-first en voorzien van CSS-commentaar per onderdeel.
- `assets/css/main.scss`: Jekyll-ingang voor de SCSS.
- `assets/img/logo.svg`: eenvoudig aanpasbaar voorbeeldlogo.
- `index.md`: homepage die de home-layout gebruikt.
- `blog.md`: blogoverzicht.
- `_pages/over.md`: voorbeeld van een gewone pagina.
- `_posts/2026-06-02-welkom-op-alexx-fyi.md`: voorbeeldblogpost.
- `manual.md`: handleiding voor aanpassen en publiceren.

### Waarom deze opzet

De site is opgezet als een volledige Jekyll-site die ook als theme-stramien werkt. De layouts en includes houden structuur en herbruikbare onderdelen gescheiden. De SCSS staat grotendeels in een enkel helder bestand zodat kleuren, fonts, spacing en componenten makkelijk terug te vinden zijn.

### Wat het doet

De homepage toont bovenin het logo met de naam ernaast, daaronder het menu, dan een introblok en daarna de blogposts. Blogposts tonen automatisch datum, titel en categorieen. Gewone pagina's gebruiken een rustig artikelstramien. De footer toont social links met Font Awesome.
