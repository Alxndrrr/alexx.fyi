# Markdown Cheatsheet

### Post types
Gebruik altijd deze twee YAML velden:

```yaml
description: "Korte omschrijving voor SEO en social previews."
homepage_type: standard
blogpost_type: standard
```

Homepage types:
- `standard` = alleen datum, titel en categorieen op de homepage
- `content` = volledige blog op homepage, tenzij `<!--more-->` gebruikt wordt
- `micropost` = een micropost of Threads/Bluesky post

Blogpost types:
- `standard` = gewone blogpostpagina
- `micropost` = micropostpagina

### Standaard opmaak

Headings = *, ** of ***
Dik gedrukt = **dik gedrukt**
Schuint = *schuin*
Doorgestreept = ~~streep~~


Links = [Linktekst](https://example.com)
Bulletlist = met streepjes onder elkaar -

<span class="highlight-pink">Pink highlight</span>
<span class="highlight-purple">Purple highlight</span>
<span class="highlight-yellow">Yellow highlight</span>


## Afbeeldingen

```markdown
![Beschrijving van de afbeelding](/assets/img/bestand.png)
```

## Lijsten

```markdown
- Eerste punt
- Tweede punt
- Derde punt
```

```markdown
1. Eerste stap
2. Tweede stap
3. Derde stap
```

## Quote

```markdown
> Dit is een quote.
```

## Code

Gebruik een enkel woord of korte code zo:

```markdown
`code`
```

Gebruik meerdere regels code zo:

````markdown
```html
<p>Hello world</p>
```
````

## Horizontale lijn

```markdown
---
```

## Markeren

Deze site heeft extra stijlen voor gemarkeerde tekst:

```html
<span class="highlight-pink">Roze markering</span>

<span class="highlight-purple">Paarse markering</span>

<span class="highlight-yellow">Gele markering</span>
```

## YouTube-video

Gebruik alleen de video-ID:

```liquid
{% include youtube.html id="dQw4w9WgXcQ" %}
```

## Content Preview Break

Bij een `homepage_type: content` post kun je hiermee bepalen waar de homepage-preview stopt:

```markdown
Tekst die op de homepage verschijnt.

<!--more-->

Tekst die alleen op de volledige postpagina verschijnt.
```
