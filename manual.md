# Handleiding alexx.fyi

Deze Jekyll-site is mobile-first gebouwd en geschikt voor GitHub Pages.

## Lokaal bekijken

Installeer eerst Ruby en Bundler als je die nog niet hebt.

```powershell
bundle install
bundle exec jekyll serve
```

Open daarna `http://localhost:4000`.

## Belangrijkste bestanden

- `_config.yml`: sitegegevens, menu, social links en algemene instellingen.
- `_sass/_alexx.scss`: alle styling van het theme.
- `_layouts/`: templates voor homepage, posts en gewone pagina's.
- `_includes/`: herbruikbare onderdelen zoals header, footer en postkaartjes.
- `_posts/`: alle blogposts.
- `_pages/`: gewone pagina's zoals `Over`.
- `assets/img/logo.svg`: het logo.

## Naam, intro en social links aanpassen

Open `_config.yml`.

Pas deze velden aan:

```yml
title: alexx.fyi

author:
  name: Alexx
  intro: "Je intro tekst."
  email: "hello@example.com"
  threads: "https://www.threads.net/jouwnaam"
```

De intro verschijnt automatisch op de homepage.

## Menu aanpassen

Open `_config.yml` en wijzig `nav`:

```yml
nav:
  - title: Home
    url: /
  - title: Blog
    url: /blog/
  - title: Over
    url: /over/
```

Voeg een nieuw item toe wanneer je een nieuwe pagina in het menu wilt tonen.

## Kleuren en fonts aanpassen

Open `_sass/_alexx.scss`.

Bovenaan staan de CSS-variabelen:

```css
:root {
  --color-paper: #f7f3ea;
  --color-ink: #1d1b18;
  --color-muted: #746b61;
  --color-line: #ded6ca;
  --color-accent: #d54f2f;
}
```

Deze kleuren sturen bijna de hele site. Verander vooral `--color-paper`, `--color-ink` en `--color-accent` voor een andere sfeer.

## Logo vervangen

Vervang `assets/img/logo.svg` door je eigen bestand.

Als je bestandsnaam anders is, pas dan in `_config.yml` dit veld aan:

```yml
logo: "/assets/img/logo.svg"
```

## Nieuwe blog maken

Maak een nieuw Markdown-bestand in `_posts/`.

De bestandsnaam moet dit patroon volgen:

```text
YYYY-MM-DD-titel-van-je-blog.md
```

Voorbeeld:

```text
2026-06-10-mijn-nieuwe-blog.md
```

Gebruik bovenaan deze front matter:

```markdown
---
title: Mijn nieuwe blog
date: 2026-06-10
categories:
  - notities
  - persoonlijk
excerpt: Korte samenvatting voor feeds en zoekmachines.
---

Hier begint je blogtekst.
```

De site zet automatisch de datum boven de titel en de categorieen onder de titel.

## Nieuwe gewone pagina maken

Maak een Markdown-bestand in `_pages/`.

Voorbeeld `contact.md`:

```markdown
---
title: Contact
description: Waar je mij kunt vinden.
---

Schrijf hier je pagina.
```

De pagina komt dan op `/contact/`.

Wil je de pagina in het menu zetten, voeg hem dan toe aan `nav` in `_config.yml`.

## Homepage aanpassen

De homepage gebruikt `_layouts/home.html`.

De introtekst komt uit `_config.yml`:

```yml
author:
  intro: "Je intro tekst."
```

De bloglijst wordt automatisch gevuld met alles uit `_posts/`.

## Publiceren op GitHub Pages

1. Zet deze bestanden in een GitHub repository.
2. Ga in GitHub naar `Settings`.
3. Open `Pages`.
4. Kies de branch waarop je site staat, meestal `main`.
5. Kies `/root` als map.
6. Sla op.

GitHub Pages bouwt de site daarna automatisch.

## Veelvoorkomende aanpassingen

### Datumweergave aanpassen

Zoek in `_layouts/post.html` en `_includes/post-card.html` naar:

```liquid
{{ page.date | date: "%d-%m-%Y" }}
```

of:

```liquid
{{ post.date | date: "%d-%m-%Y" }}
```

Pas het datumformaat aan als je een andere weergave wilt.

### Breedte van de site aanpassen

Open `_sass/_alexx.scss` en wijzig:

```css
--content-width: 44rem;
```

Een hogere waarde maakt de site breder op grotere schermen.
