# OxARCA website

The website for **OxARCA — AI for Research, Collections and Archives**, University of Oxford,
and for **Archos**, our epistemically grounded LLM system for archival exploration.

Live at <https://oxarca.github.io>. Built with [oxie](https://pypi.org/project/oxie/).

## How it fits together

```
source/          content — this is what you edit
  index.md         home page prose
  page/*.md        Archos, People, Publications, Your collection, Collaborate
  post/*.md        news items
  image/           images, copied to /image/
  static/          files copied to the site root
src/             templates, site metadata, styles
  meta_data.json   site title, links, run figures, constitution, nav
  *.html           Jinja2 templates
  styles.css       Tailwind v4 tokens
docs/            generated output — not committed, rebuilt by CI
build.py         site configuration
```

Pushing to `main` rebuilds and redeploys the site automatically
(`.github/workflows/static.yml`). You never commit `docs/`.

## Editing content

**Most changes are just Markdown.** Every file under `source/page/` and `source/post/` needs
all five frontmatter fields — `Title`, `Summary`, `Authors`, `Date`, `Category`. oxie parses
them in one block, so if one is missing the fields after it are silently dropped and the page
renders half-empty. `source/index.md` is the one exception: it uses bare `Key: value` lines
with no `---` fences.

Internal links are written from the site root, e.g. `[our people](/page/people.html)`.

### Add a news item

Create `source/post/YYYY-MM-slug.md`:

```markdown
---
Title: Something happened
Summary: One sentence, used on the news index and in the RSS feed.
Authors: OxARCA
Date: 2026-09-01
Category: News
Tags: [tag one, tag two]
---

Your text here.
```

Keep `Category: News` — categories become `blog_<Category>.html`, so a category with a space
in it produces a URL with a space in it.

### Change the run figures, the constitution, or the nav

These live in `src/meta_data.json`, not in markup: `archos_stats.tiles` (the four numbers on
the home page), `comparison.rows`, `constitution`, and `nav`. Edit the JSON and rebuild.

### Publish the contact email

`contact_email` in `src/meta_data.json` is empty, so no address is shown anywhere. Setting it
turns on three things at once: the footer line, the "Email the team" button on the home page,
and the line on the 404 page. Each is guarded, so emptying it again removes all three cleanly.

### Add the Evidence Report figure

Drop the image at `source/image/archos-evidence-report.png` and replace the placeholder
`<figure>` block in `source/page/archos.md`.

## Building locally

Needs Python 3.10+ and Node 20+.

```bash
python -m venv .venv && .venv/bin/pip install -r requirements.txt
npm install
.venv/bin/python build.py
python3 -m http.server -d docs 8000     # then open http://localhost:8000
```

`npm run watch:css` rebuilds the stylesheet on change while you work.

Builds are deterministic — the same content produces byte-identical output — so an unexpected
diff means something actually changed.

## Moving the site

The site is served from the organisation root, so internal links are root-absolute. To move it
to a project page or a subpath, set `BASE_PATH` in `build.py` (e.g. `"/oxarca"`) and update
`link` in `src/meta_data.json`. Templates read that prefix; nothing else needs to change. For a
custom domain, add a `CNAME` file in `source/static/` and set `link` to the new origin.
