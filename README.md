# Yilei Fu's personal website

A small Jekyll website hosted at https://fu-yilei.github.io. The site uses the approved, restrained academic layout with plain HTML, CSS, and a little JavaScript for the mobile menu, publication search and filters, and citation copying. All content remains readable without JavaScript.

## Local preview

Use Ruby 3.3 or later, Bundler, and Python 3:

```sh
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve --livereload
```

Open http://127.0.0.1:4000. On macOS with Homebrew's Ruby 3.3, add `/opt/homebrew/opt/ruby@3.3/bin` to `PATH` first.

## Updating content

- `index.md`: short biography and homepage sections.
- `about.md`: education, experience, and talks.
- `research.html` and `software.html`: research descriptions and software links.
- `_data/publications.json`: publication metadata, DOI links, and verification sources. Keep `status` as `journal` or `preprint`; the homepage shortlist and its order are defined in `index.md`.
- `_posts/`: the original blog posts. Keep filenames and categories unchanged to preserve URLs.
- `assets/css/main.css`: the shared style sheet.
- `_includes/publication.html`: the shared citation layout and full author lists.
- `assets/js/main.js`: mobile navigation, publication filtering, and citation copying.

The Notes & talks page includes recorded talks and all six original blog posts. GitHub Pages builds and deploys the Jekyll source from `main`. The separate local `sites/` checkout is excluded from this repository and its builds.

After editing publications, run `python3 scripts/generate_bibtex.py` to refresh the downloadable bibliography. There are no email addresses or email contact links in the current page templates or configuration.

## Validation

```sh
python3 scripts/generate_bibtex.py
JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter
python3 scripts/check_site.py
```

The check verifies generated pages, internal links, anchors, legacy post URLs, feeds, and the absence of email contact links. For deployment, GitHub Pages builds the repository's Jekyll source. Generated `_site/` output and local dependencies are ignored.
