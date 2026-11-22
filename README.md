# christmasescaperoom.co.uk

Free Christmas escape rooms to play online or print at home: games, tools and guides built to rank in Google and be cited by AI answers. Created by Paul.

## Folders

| Folder | What it is |
| --- | --- |
| `docs/` | **The live website.** Plain static HTML/CSS/JS, so any static host can serve it. |
| `build/` | Python page generator. Edit the content here, then rebuild. |
| `scripts/` | Make social and Pinterest images, and the Gumroad PDFs (needs Playwright). |
| `GUMROAD-LISTINGS.md` | Text for the six Gumroad product listings. |

## Publish

**GitHub Pages (free):** Settings → Pages → Source: *Deploy from a branch* → Branch `main`, folder `/docs`. `docs/CNAME` already points to christmasescaperoom.co.uk. In your domain registrar, add the DNS records GitHub shows you, then tick *Enforce HTTPS*.

**Cloudflare Pages or Netlify:** connect this repo, leave the build command empty and set the output directory to `docs`.

Then submit `https://christmasescaperoom.co.uk/sitemap.xml` in Google Search Console and Bing Webmaster Tools.

## Edit and rebuild

```bash
python3 build/build.py                 # regenerates every page, sitemap.xml, robots.txt, llms.txt
python3 scripts/make_images.py         # social + Pinterest images (pip install playwright && playwright install chromium)
python3 scripts/make_gumroad_pdfs.py   # print-ready PDFs into gumroad/ (git-ignored)
```

## Gumroad buttons

Paste each product URL into `GUMROAD` at the top of `build/games_lib.py` and rebuild. A "Get the print-ready PDF" button then appears on that game's page. The PDFs are git-ignored because this repo is public.
