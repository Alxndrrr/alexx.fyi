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

## Change the Name and Social Links

Open `_config.yml` and edit:

```yml
title: alexx.fyi

author:
  name: Alexx
  email: "hello@example.com"
  threads: "https://www.threads.net/yourname"
```

## Change the Homepage Intro

Edit `_includes/intro.html`.

You can use regular HTML in that file:

```html
<p>Hi, I am Alexx.</p>
<p>This is <strong>my place</strong> for notes and projects.</p>
```

The homepage automatically loads that file into the intro box.

## Change the Currently Box

Edit `_includes/currently.md`.

This file controls the small currently box below the homepage intro. It uses a small label and one sentence with optional Font Awesome icons:

```markdown
{: .currently-label}
// currently

{: .currently-sentence}
<i class="fa-solid fa-book-open" aria-hidden="true"></i>
Currently reading **Ready Player One**.
```

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

For the mobile hamburger menu, edit `mobile_nav` in `_config.yml`. It can use the same items as `nav`, or a different list:

```yml
mobile_nav:
  - title: Blog
    url: /blog/
  - title: Colophon
    url: /colophon/
```

Social icons in the mobile menu and footer come from `social_links`:

```yml
social_links:
  - title: Threads
    url: "https://www.threads.net/"
    icon: "fa-brands fa-threads"
```

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
description: "A short SEO description for search results and social previews."
date: 2026-06-10
homepage_type: standard
blogpost_type: standard
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

Create a post in `_posts/` and add `homepage_type: micropost` and `blogpost_type: micropost` to the front matter:

```markdown
---
title: My Micropost Title
description: "A short summary for feeds, search engines and social previews."
date: 2026-06-02 00:01:00 +0000
homepage_type: micropost
blogpost_type: micropost
external_url: "https://www.threads.net/@yourname/post/example"
categories:
  - micro
  - note
excerpt: A short summary for feeds and search engines.
---

Your short text goes here.
```

The entire micropost block on the homepage links to the URL when `external_url:` is set. This is useful when the micropost also exists on Threads or somewhere else.

Threads and Bluesky URLs automatically show a subtle service icon in the micropost box.

If you leave `external_url:` out, the micropost block links to the full post page on this site.

Do not use `url:` for this. Jekyll already uses `url` internally for the post's own permalink.

The `title` is still useful for SEO, feeds, and browser titles, but the theme hides it visually for microposts.

## Create a Content Preview Post

Content preview posts use a different homepage list style:

1. Date
2. Title
3. Post content until the break marker
4. Continue reading link, only when a break marker is used
5. Categories

Add `homepage_type: content` to the front matter. Keep `blogpost_type: standard` for the regular post page design:

```markdown
---
title: My Content Preview Post
description: "A short SEO description for search results and social previews."
date: 2026-06-02
homepage_type: content
blogpost_type: standard
categories:
  - essay
  - notes
---

This part appears on the homepage.

<!--more-->

This part only appears after someone opens the full post.
```

The break marker is `<!--more-->`. If you leave it out, the full post content appears on the homepage and no continue reading link is shown. For `homepage_type: content` posts, do not use front matter `excerpt:` for the homepage preview; the preview comes from the post body.

## Embed a YouTube Video

Use the YouTube include inside any post:

```liquid
{% include youtube.html id="dQw4w9WgXcQ" %}
```

Use only the video ID, not the full YouTube URL. The theme makes the video responsive automatically.

The include also adds iframe loading improvements like lazy loading, fixed dimensions, low fetch priority, and a privacy-friendly `youtube-nocookie.com` embed URL.

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

## Add Favorites Posters

Edit `_pages/favorites.md`.

Use one section per group and one `favorite-card` per poster:

```html
<section class="favorites-section">
  <h2>Movies</h2>
  <div class="favorites-grid">
    <figure class="favorite-card">
      <div class="favorite-card__poster">
        <img src="/assets/img/favorites/movie-poster.jpg" alt="Movie title poster">
      </div>
      <figcaption>
        <strong>Movie Title</strong>
        <span>1999</span>
      </figcaption>
    </figure>
  </div>
</section>
```

The grid shows up to 3 posters per row on mobile and 5 per row on desktop.

## Change the Homepage

The homepage uses `_layouts/home.html`.

The intro text comes from `_includes/intro.html`.

The blog list is generated automatically from `_posts/`.

To limit how many posts appear on the homepage, edit this in `_config.yml`:

```yml
home_post_limit: 10
```

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
