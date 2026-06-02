# alexx.fyi Manual

This Jekyll site is mobile-first, centered, dark styled, and ready for GitHub Pages.

## Preview Locally

Install Ruby and Bundler first if you do not already have them.

```powershell
bundle install
bundle exec jekyll serve
```

Then open `http://localhost:4000`.

## Key Files

- `_config.yml`: site title, author intro, navigation, social links, plugins, and general settings.
- `_sass/_alexx.scss`: all theme styling, including dark mode colors, width, layout, and typography.
- `_layouts/`: templates for the homepage, posts, archives, and regular pages.
- `_includes/`: reusable parts like the header, footer, and post cards.
- `_posts/`: all blog posts.
- `_pages/`: regular pages like `About`.
- `assets/img/avatar.png`: the avatar used as the logo.

## Change the Name, Intro, and Social Links

Open `_config.yml` and edit:

```yml
title: alexx.fyi

author:
  name: Alexx
  intro: "Your intro text."
  email: "hello@example.com"
  threads: "https://www.threads.net/yourname"
```

The intro appears automatically on the homepage.

## Change the Menu

Open `_config.yml` and edit `nav`:

```yml
nav:
  - title: Home
    url: /
  - title: Blog
    url: /blog/
  - title: About
    url: /about/
```

Add a new item when you want another page in the main menu.

## Change Colors, Fonts, and Width

Open `_sass/_alexx.scss`.

The main visual settings are at the top:

```css
:root {
  --color-paper: #18171c;
  --color-ink: #e8e8e8;
  --color-muted: #b7a7ff;
  --color-line: #2e2c37;
  --color-accent: #ff0073;
  --color-accent-yellow: #ffbd37;
  --color-accent-purple: #5200ff;
  --font-body: "Space Grotesk", sans-serif;
  --font-display: "Tanker", Impact, sans-serif;
  --font-site: "Jersey 10", "Pixelify Sans", monospace;
  --font-detail: "Pixelify Sans", monospace;
  --content-width: 44rem;
}
```

The site uses Jersey 10 for the site name, Tanker for menu items and headings, Space Grotesk for page and blog content, and Pixelify Sans for metadata, tags, and footer details.

To make the centered layout wider or narrower, change:

```css
--content-width: 44rem;
```

## Replace the Logo

Replace `assets/img/avatar.png` with your own file.

If the filename changes, update this in `_config.yml`:

```yml
logo: "/assets/img/avatar.png"
```

## Create a New Blog Post

Create a new Markdown file inside `_posts/`.

The filename must use this pattern:

```text
YYYY-MM-DD-title-of-your-post.md
```

Example:

```text
2026-06-10-my-new-post.md
```

Use this front matter:

```markdown
---
title: My New Post
date: 2026-06-10
categories:
  - notes
  - personal
excerpt: A short summary for feeds and search engines.
---

Your post starts here.
```

The layout automatically shows the date above the title and the categories below it.

Jekyll hides posts with future dates by default. If a post does not appear on the homepage, check that the `date` value is today or earlier.

## Create a Micropost

Microposts are short posts that appear in full on the homepage. They do not show a title in the post list or on the post page.

Create a post in `_posts/` and add `type: micropost` to the front matter:

```markdown
---
type: micropost
title: My Micropost Title
date: 2026-06-02 00:01:00 +0000
categories:
  - micro
  - note
excerpt: A short summary for feeds and search engines.
---

Your short text goes here.
```

The entire micropost block on the homepage links to the full post page.

The `title` is still useful for SEO, feeds, and browser titles, but the theme hides it visually for microposts.

## Create a Regular Page

Create a Markdown file inside `_pages/`.

Example `contact.md`:

```markdown
---
title: Contact
description: Where to find me.
---

Write your page here.
```

That page will be available at `/contact/`.

To add it to the menu, add it to `nav` in `_config.yml`.

## Change the Homepage

The homepage uses `_layouts/home.html`.

The intro text comes from `_config.yml`:

```yml
author:
  intro: "Your intro text."
```

The blog list is generated automatically from `_posts/`.

## Publish on GitHub Pages

1. Put these files in a GitHub repository.
2. Go to `Settings`.
3. Open `Pages`.
4. Choose the branch that contains the site, usually `main`.
5. Choose `/root` as the folder.
6. Save.

GitHub Pages will build the site automatically.

## GitHub Pages Project URL

This site is configured for the standard GitHub Pages project URL:

```yml
url: "https://alxndrrr.github.io"
baseurl: "/alexx.fyi"
```

That means the site is expected to load at:

```text
https://alxndrrr.github.io/alexx.fyi/
```

If you later use a custom domain like `https://alexx.fyi`, change it to:

```yml
url: "https://alexx.fyi"
baseurl: ""
```
