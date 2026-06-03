# Markdown Cheatsheet

### Type posts
Dit zijn de type posts doe ik kan toevoegen
- Content = volledige blog op homepage, tenzij <!--more--> gebruikt wordt
- Micropost = een micropost of threads post

### Standaard opmaak

Headings = *, ** of ***
Dik gedrukt = **dik gedrukt**
Schuint = *schuin*
Doorgestreept = ~~streep~~


Links = [Linktekst](https://example.com)
Bulletlist = met streepjes onder elkaar -


## Koppen

```markdown
# Grote titel
## Tussenkop
### Kleine tussenkop
```

## Tekst

```markdown
Normale tekst.

**Vetgedrukte tekst**

*Schuingedrukte tekst*

~~Doorgestreepte tekst~~
```

## Links

```markdown
[Linktekst](https://example.com)
```

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
<mark>Roze markering</mark>

<span class="highlight-bg-orange">Paarse markering</span>

<span class="highlight-bg-yellow">Gele markering</span>
```

## YouTube-video

Gebruik alleen de video-ID:

```liquid
{% include youtube.html id="dQw4w9WgXcQ" %}
```

## Content Preview Break

Bij een `type: content` post kun je hiermee bepalen waar de homepage-preview stopt:

```markdown
Tekst die op de homepage verschijnt.

<!--more-->

Tekst die alleen op de volledige postpagina verschijnt.
```
