# Agent Log

This file tracks what was created, why it was created, and what each part does.

## 2026-06-02

### Goal

Create a mobile-first Jekyll theme for `alexx.fyi` that can be uploaded to GitHub Pages.

### Created

- `_config.yml`: central settings for title, author, navigation, social links, permalink structure, plugins, and defaults.
- `Gemfile`: uses the `github-pages` gem so local builds stay close to GitHub Pages.
- `_layouts/default.html`: base frame with head, header, main content, and footer.
- `_layouts/home.html`: homepage with intro block and the latest blog posts.
- `_layouts/archive.html`: blog archive for all posts.
- `_layouts/post.html`: blog template with date above the title and categories below the title.
- `_layouts/page.html`: template for regular pages.
- `_includes/header.html`: logo, site name, and main menu.
- `_includes/footer.html`: footer with Font Awesome icons for Threads, RSS, and mail.
- `_includes/post-card.html`: reusable block for post listings.
- `_sass/_alexx.scss`: all theme styling, mobile-first and commented by section.
- `assets/css/main.scss`: Jekyll entry file for SCSS.
- `assets/img/logo.svg`: simple editable sample logo.
- `index.md`: homepage using the home layout.
- `blog.md`: blog archive page.
- `_pages/about.md`: example regular page.
- Seven dummy blog posts in `_posts/`.
- `manual.md`: guide for editing, posting, and publishing.

### Why This Structure

The site is structured as a complete Jekyll site that also works as a reusable theme pattern. Layouts and includes keep structure and reusable parts separate. The SCSS is intentionally concentrated in one clear file so colors, fonts, spacing, and components are easy to find.

### What It Does

The homepage shows the logo at the top, the site name beside it, the menu below, an intro block, and then blog posts. Blog posts automatically show the date, title, and categories. Regular pages use a calm article layout. The footer shows social links with Font Awesome.

### Update: English, Dark Mode, and Dummy Content

- Changed the site language to English.
- Updated the regular page navigation to use `About`.
- Replaced the Dutch example page with `_pages/about.md`.
- Added seven total dummy blog posts.
- Changed the visual style to a centered, narrow dark mode layout.
- Added Tanker for headings, post titles, and the menu.
- Initially added DM Sans for page and blog content; later replaced it with the old Pika-style font stack.

### Update: GitHub Pages Visibility Fix

- Moved dummy post dates to dates on or before 2026-06-02, because Jekyll hides future-dated posts by default.
- Added a small inline dark fallback in `_layouts/default.html` so the page remains dark even before the compiled stylesheet loads.
- Added post excerpts to homepage cards so dummy post content is visible on the homepage.

### Update: GitHub Pages Project URL

- Set `url` to `https://alxndrrr.github.io` and `baseurl` to `/alexx.fyi`.
- This makes assets and internal links resolve correctly on the standard GitHub Pages project URL.

### Update: Old Pika Style

- Read the pasted old Pika CSS and translated its visual system to the Jekyll theme.
- Changed the palette to dark purple-black, neon pink, yellow, and purple.
- Added Jersey 10 for the site name, Space Grotesk for body content, and Pixelify Sans for metadata, tags, and footer details.
- Kept Tanker for headings, post titles, and the menu.
- Added the old pixel-style yellow site-name shadow, pink tags, purple metadata, yellow content links with purple underlines, and pink regular page titles.

### Update: Avatar Logo

- Changed `logo` in `_config.yml` from `/assets/img/logo.svg` to `/assets/img/avatar.png`.
- The header now uses the uploaded avatar image as the site logo.

### Update: CSS Cache Busting

- Added a build-time version query to the `main.css` link in `_layouts/default.html`.
- This helps GitHub Pages and browsers load the latest compiled CSS instead of a cached older stylesheet.

### Update: Layout Alignment

- Increased `--content-width` from `38rem` to `44rem`.
- Left-aligned the header brand, menu, homepage post titles, page titles, blog titles, tags, and intro block.
- Removed the `Latest posts` heading from the homepage.
- Removed homepage post excerpts so the line below tags no longer appears.

### Update: Microposts

- Added support for `type: micropost` in post front matter.
- Microposts render as full-content clickable blocks in the homepage post list.
- Micropost detail pages hide the title.
- Added one sample micropost at `_posts/2026-06-02-micro-note-after-rain.md`.
- Adjusted the sample micropost timestamp to the start of the day so Jekyll does not treat it as a future post during GitHub Pages builds.

### Update: Content Preview Post Type

- Added `excerpt_separator: "<!--more-->"` in `_config.yml`.
- Added support for `type: content` in post front matter, with `type: excerpt` kept as a backwards-compatible alias.
- Content preview posts render on the homepage as title, content before `<!--more-->`, optional continue reading link, categories, and date.
- Converted `_posts/2026-05-29-making-a-quieter-homepage.md` into an example content preview post.
- Switched the homepage preview for content posts from `post.excerpt` to `post.content` split on `<!--more-->`, so front matter excerpts do not override the visible preview.

### Update: Header Layout

- Changed the header to a two-column layout with avatar on the left and title/menu stacked on the right.
- Made the title slightly smaller.
- Increased the menu text size.
- Sized the avatar to visually match the height of the title plus menu.

### Update: Micropost Design

- Removed `<!--more-->` from the example content post so it shows fully on the homepage for now.
- Updated homepage micropost cards to show avatar on the left and tags/content on the right.
- Moved micropost date to the bottom-right of the box in muted grey.
- Removed hover border styling from micropost boxes.
- Applied the same micropost box layout to individual micropost pages.
- Removed underline hover styling from homepage blog title links.

### Update: Smaller Titles and Intro Box

- Made homepage post titles, blog page titles, and regular page titles smaller and consistent.
- Removed the avatar from the header/menu.
- Moved the avatar into the homepage intro box.
- Removed the visible `Intro` label from the homepage intro box.
- Changed the intro box to a blue/purple panel using the existing purple accent.

### Update: Archive and Header Row

- Made intro box text white.
- Changed the blog page into a yearly archive grouped by post year.
- Rendered archive posts as a compact bullet list with pixel-style square bullets.
- Changed the header to place the site name on the far left and the menu on the far right.
- Moved the nav outside the title wrapper and made the header a two-column grid so the menu can actually align right.
- Removed the small-screen stacking fallback and made the header/menu nowrap so the title and menu stay on one row.

### Update: Video Content Post

- Added `_posts/2026-06-02-youtube-embed-test.md` as a `type: content` post with full homepage content.
- Added responsive `.video-embed` styling for YouTube iframes.
