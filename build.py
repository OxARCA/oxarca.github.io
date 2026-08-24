"""Build script for the OxARCA site.

    python build.py        # writes docs/

Requires:  pip install -r requirements.txt  &&  npm install
"""
from oxie import Site, SiteConfig

#: Path prefix every internal link is written against.
#:
#: The site is served from the organisation root (https://oxarca.github.io/),
#: so the prefix is empty and oxie's root-absolute links are already correct.
#: Moving to a project page would make this "/oxarca"; a custom domain leaves
#: it "". Templates concatenate it as `{{ base }}/index.html`, so this is the
#: single place that has to change.
BASE_PATH = ""

config = SiteConfig(
    # source/, src/ and docs/ are the defaults.
    collect_dirs={
        # Everything in source/image is copied to docs/image ...
        "source/image": "docs/image",
        # ... and source/static lands at the site root, next to index.html.
        "source/static": "docs",
    },
    timezone="Europe/London",
    # Syntax highlighting stylesheet written to docs/pygments.css.
    pygments_style="github-dark",
    # Compiles src/styles.css into docs/styles.css with Tailwind.
    css_build_command=("npm", "run", "build:css"),
)

if __name__ == "__main__":
    site = Site(config)
    # Site builds its Jinja environment in __init__, so the global is added
    # here rather than through SiteConfig, which has no hook for it.
    site.env.globals["base"] = BASE_PATH
    site.build()
