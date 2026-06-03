---
title: Markdown Style Preview
date: 2026-06-03 12:00:00 +0200
type: content
categories:
  - Blog
  - Design
---

This is a dummy post to preview the full blog styling. It includes **bold text**, *italic text*, ***bold italic text***, `inline code`, [a regular link](https://example.com), and a little bit of text that should wrap naturally across multiple lines.

![A baseball field with a dust storm in the background, from Interstellar]({{ '/assets/img/posts/interstellar-back.jpg' | relative_url }})

## Heading Level Two

This paragraph lives under an H2. It is here to test spacing, line-height, link styling, and how the content feels when it starts to become a real article instead of a tiny note.

### Heading Level Three

This paragraph lives under an H3. It includes a longer sentence so you can judge whether the width, rhythm, and color feel comfortable for reading.

#### Heading Level Four

This is a smaller heading. It should feel useful without yelling.

## Bullet List

- First bullet item with a short sentence.
- Second bullet item with **bold text** inside it.
- Third bullet item with [a link inside the list](https://example.com).
- Fourth bullet item with `inline code` inside it.

## Numbered List

1. First numbered item.
2. Second numbered item with *italic text*.
3. Third numbered item with a little more copy to test wrapping on mobile screens.
4. Fourth numbered item with `code`.

## Blockquote

> This is a blockquote. It should feel like a highlighted aside, not just a regular paragraph with a line next to it.
>
> This second paragraph inside the quote checks whether multiple paragraphs still look good together.

## Highlighted Text

This sentence uses the default <mark>pink highlight</mark>. You can also use <span class="highlight-purple">purple highlight</span> or <span class="highlight-yellow">yellow highlight</span> when you want a different emphasis.

```html
<mark>Pink highlight</mark>
<span class="highlight-purple">Purple highlight</span>
<span class="highlight-yellow">Yellow highlight</span>
```

## Code Block

```html
<article class="tiny-transmission">
  <h2>Do not go gentle into that good blog post.</h2>
  <p>Preview everything before calling it done.</p>
</article>
```

## Table

| Element | Purpose | Status |
| --- | --- | --- |
| Headings | Structure the post | Testing |
| Lists | Scan-friendly content | Testing |
| Blockquotes | Highlight a thought | Testing |
| Images | Visual rhythm | Testing |

## Horizontal Rule

Text before the rule.

---

Text after the rule.

## Mixed Markdown

Here is a final paragraph with **bold**, *italic*, `code`, and [another link](https://example.com). It is followed by a small checklist-style list, even though regular GitHub-flavored checkboxes may or may not be styled separately by Jekyll:

- [x] Write a dummy post
- [x] Add an image
- [ ] Adjust the design after previewing

And that is the end of the test post.
