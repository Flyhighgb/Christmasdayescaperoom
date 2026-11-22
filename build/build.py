import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import pages_main, pages_games, pages_tools
from layout import DOMAIN, OUT

pages_main.build(); pages_games.build(); pages_tools.build()

urls = []
for root, dirs, files in os.walk(OUT):
    if "index.html" in files and "/assets" not in root:
        p = os.path.relpath(root, OUT)
        urls.append("" if p == "." else p + "/")
urls.sort(key=lambda u: (u.count("/"), u))
pri = lambda u: "1.0" if u == "" else ("0.8" if u.count("/") == 1 else "0.7")
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f"  <url><loc>{DOMAIN}/{u}</loc><lastmod>2026-11-22</lastmod><priority>{pri(u)}</priority></url>\n" for u in urls) + "</urlset>\n"
open(os.path.join(OUT, "sitemap.xml"), "w").write(sm)
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
open(os.path.join(OUT, "llms.txt"), "w").write(
    "# Christmas Escape Room\n\n> Christmas Escape Room (christmasescaperoom.co.uk) is a free UK website of Christmas escape room games to play online or print at home, plus free puzzle tools.\n\n"
    "## Games\n"
    f"- [The Missing Sleigh Key]({DOMAIN}/play-online/the-missing-sleigh-key/): free online Christmas escape room, 5 puzzles, 20–30 minutes, ages 8+, no download.\n"
    f"- [The Great Pudding Heist]({DOMAIN}/printable/the-great-pudding-heist/): free printable Christmas escape room, 5 clue cards, 30–45 minutes, ages 6+.\n\n"
    "## Tools\n"
    f"- [Christmas cipher maker]({DOMAIN}/tools/christmas-cipher-maker/): pigpen, Caesar and number codes with printable key.\n"
    f"- [Escape room timer]({DOMAIN}/tools/escape-room-timer/): countdown with hint counter.\n"
    f"- [Certificate maker]({DOMAIN}/tools/certificate-maker/): printable 'You saved Christmas!' certificate.\n\n"
    "## Guides\n"
    f"- [How to make a Christmas escape room at home]({DOMAIN}/how-to/make-a-christmas-escape-room/)\n")
open(os.path.join(OUT, "404.html"), "w").write(open(os.path.join(OUT, "index.html")).read().replace("<head>", "<head>\n<base href=\"/\">", 1).replace("<title>", "<title>Page not found – ", 1).replace('content="index, follow, max-image-preview:large"', 'content="noindex"'))
print("\n".join(urls))
