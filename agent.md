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

### Update: GitHub Pages Custom Domain

- Set `url` to `https://www.alexx.fyi` and `baseurl` to an empty string.
- Added a root `CNAME` file with `www.alexx.fyi` so GitHub Pages keeps the custom domain attached to the repository.

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
- Moved the YouTube embed markup into `_includes/youtube.html` so posts can embed videos with a clean Liquid include.
- Changed the video post timestamp to the start of the day so Jekyll does not hide it as a future post.

### Update: Visual Simplification

- Simplified YouTube embed styling by removing colored borders and shadows.
- Made tag labels smaller across mobile and desktop.
- Removed the border around the homepage intro box.
- Removed the line underneath the header/menu.
- Added `_includes/date.html` for written English dates with ordinal suffixes.
- Removed circular borders/backgrounds around footer social icons.

### Update: YouTube Loading

- Added `loading="lazy"`, `fetchpriority="low"`, fixed width/height, and `referrerpolicy` to `_includes/youtube.html`.
- Added preconnect hints for YouTube embed/static hosts in `_layouts/default.html`.
- Removed the optional YouTube `title` parameter from post/manual examples; the include keeps a default iframe title internally.

### Update: Intro Include

- Moved homepage intro content from `_config.yml` to `_includes/intro.html`.
- Updated `_layouts/home.html` to include `_includes/intro.html`.
- Updated the manual to explain that intro content can use regular HTML.

### Update: Homepage Post Rhythm

- Increased the homepage post list gap slightly.
- Added extra top spacing when a micropost is followed by a regular/content post, so short boxed updates feel visually separate from longer blog entries.

### Update: Colophon Page

- Added `_pages/colophon.md` with the hardware, software, apps, author, and gaming colophon content from the old static page.
- Added colophon-specific two-column definition list styling to `_sass/_alexx.scss`, adapted to the current alexx.fyi color, font, and spacing variables.

### Update: Avatar Variants

- Added the 2025 avatar variants for the theme colors `#2e2c37`, `#ff0073`, and `#5200ff` to `assets/img/`.
- Added `micro_logo` to `_config.yml` and set micropost cards/pages to use the purple `#5200ff` avatar variant.
- Made micropost avatar crops explicitly square and circular so the non-round source images render as round avatars.

### Update: Micropost Typography and Layout

- Added Roboto Mono to the Google Fonts import and exposed it as `--font-micro`.
- Updated micropost cards and micropost pages so the text sits on the left, the smaller avatar sits on the right, and the categories/date sit together at the bottom-left.

### Update: Micropost External Links

- Added optional external-link support for homepage micropost cards.
- A micropost front matter `external_url` value links the homepage box to the external source, such as Threads; without it, the box links to the local micropost page.
- Avoided using `url` for this because Jekyll reserves `url` for each post's generated permalink.

### Update: Currently Box

- Added `_includes/currently.md` for editable homepage "currently" items.
- Added a dark pink currently box below the intro block with Font Awesome icons and one squared-off lower-left corner.
- Changed the currently content to a single sentence with a small `// currently` system-style label.
- Updated the homepage to render the currently include through `markdownify`, so Markdown formatting works inside the currently content.
- Adjusted the intro/currently corner radii so the intro has a squared lower-right corner and the currently box has a squared upper-right corner.

### Update: Mobile Menu and Micropost Sources

- Added configurable `mobile_nav` and `social_links` entries to `_config.yml`.
- Added a mobile-only hamburger menu that slides in full-width from the right and includes configured social links.
- Reused `social_links` for the footer icons.
- Added automatic Threads/Bluesky source icons for micropost cards when `external_url` points to those services.
- Added a `1.5rem` lower-right cut corner to micropost boxes.

### Update: Homepage Limit, Article Content, and Footer

- Added `home_post_limit` to `_config.yml` and applied it to the homepage post loop.
- Styled headings, bullet lists, numbered lists, and blockquotes inside post/page content.
- Reworked the footer into two layers: a yellow pixel-font tagline above a copyright/social row.

### Update: Favorites Poster Grid

- Added reusable favorites sections and poster cards to `_pages/favorites.md`.
- Styled favorites grids with 3 columns on mobile and 5 columns on desktop.
- Added bottom-aligned posters, rounded poster corners, ellipsis titles, and metadata styling.

### Update: Post Type Split

- Replaced the overloaded post `type` concept with `homepage_type` for homepage card rendering and `blogpost_type` for individual post page rendering.
- `_includes/post-card.html` now reads `homepage_type`, with old `type` kept as a fallback.
- `_layouts/post.html` now reads `blogpost_type`, with old `type` kept as a fallback.
- Added default `homepage_type: standard` and `blogpost_type: standard` for posts in `_config.yml`.

### Update: Basic SEO Metadata

- Added `jekyll-sitemap` to `_config.yml` so GitHub Pages can generate `/sitemap.xml`.
- Added `robots.txt` with a sitemap reference generated through `absolute_url`.
- Added `description` front matter to existing pages and posts for better snippets and social metadata through `jekyll-seo-tag`.

### Update: Configurable Intro Box

- Added an `intro_box` block to `_config.yml` for controlling homepage intro visibility, avatar visibility/image, background color, text color, link color, hover link color, and clipped-corner color.
- Updated `_layouts/home.html` to pass those settings to the intro block as CSS custom properties, while keeping the old `show_intro_box` flag as a backwards-compatible fallback.
- Updated `_sass/_alexx.scss` so the intro box reads its colors from those CSS custom properties.
- Updated `manual.md` with the new intro box configuration example.

### Update: Intro Box Link and Auto Text Color

- Removed the visible border from the homepage intro avatar.
- Added `link_url` and `link_label` to `intro_box` so the whole intro box can link to a configured page while preserving links inside the intro text.
- Added `text_color: "auto"` support through a small homepage script that picks dark or light intro text based on the configured box background color.
- Updated the intro box focus/cursor styles for keyboard and pointer users.

### Update: Micropost Emphasis and Intro Auto Link Colors

- Made bold text inside homepage and individual microposts much heavier so Markdown emphasis is clearly visible.
- Changed the `Micropost...` label color to yellow `#ffbd37` on both homepage cards and individual micropost pages.
- Added `link_color: "auto"` and `link_hover_color: "auto"` support for the homepage intro box so link colors respond to the configured background color.
- Removed the focus outline from the clickable intro box so clicks no longer leave a temporary border.

### Update: Shorter Homepage Intro Copy

- Replaced the homepage intro copy in `_includes/intro.html` with a shorter, more scannable English paragraph based on the About page.
- Updated the intro copy to bold Alex's name.

### Update: Favorites Homepage Games

- Added Grand Theft Auto V, Red Dead Redemption 2, Pokemon Red Version, and Tony Hawk's Pro Skater 2 to the games section on the main Favorites page.
- Copied the supplied game cover images into `assets/img/favorites/`.

### Update: Favorite Games Subpage

- Reworked `_pages/favorites/games.md` into console sections for PlayStation, PlayStation 4, Nintendo Gameboy, and Mac.
- Added Tony Hawk's Pro Skater 2, Grand Theft Auto V, Red Dead Redemption 2, Pokemon Red Version, and Stardew Valley to their requested console sections.
- Added more favorite games to the games subpage, including Minecraft, Need for Speed: Underground, Pokemon Silver Version, Cyberpunk 2077, Call of Duty, Tekken 3, Medal of Honor, Marvel's Spider-Man: Miles Morales, Hogwarts Legacy, Crash Team Racing, Age of Empires II: Definitive Edition, and Dino Crisis.
- Added PlayStation 2, PlayStation 5, and PC sections to keep the expanded game list grouped by platform.
