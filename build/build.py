import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import pages_main, pages_games, pages_tools, pages_occasions, pages_builder
from layout import DOMAIN, OUT

pages_main.build(); pages_games.build(); pages_tools.build(); pages_occasions.build(); pages_builder.build()

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
    f"- [Christmas Eve escape room]({DOMAIN}/printable/christmas-eve/): printable bedtime game, ages 5–10, 20–30 minutes.\n"
    f"- [Boxing Day escape room]({DOMAIN}/printable/boxing-day/): printable family game, ages 8+, 30–45 minutes.\n"
    f"- [New Year's Eve escape room]({DOMAIN}/printable/new-years-eve/): printable countdown game, ages 10+, 30–45 minutes.\n"
    f"- [KS2 Christmas escape room]({DOMAIN}/printable/ks2-classroom/): classroom game for Years 3–6, 45–60 minutes.\n"
    f"- [10-minute Christmas escape room]({DOMAIN}/play-online/ten-minute-christmas-escape-room/): 3 quick online puzzles.\n"
    f"- [Christmas escape room without a printer]({DOMAIN}/play-online/no-printer-christmas-escape-room/)\n"
    f"- [Scrooge's Safe]({DOMAIN}/printable/scrooges-safe/): adults. [Elf Academy Final Exam]({DOMAIN}/printable/elf-academy-final-exam/): teens. [Rudolph's Lost Bells]({DOMAIN}/printable/rudolphs-lost-bells/): ages 3–5. [Christmas Memory Lane]({DOMAIN}/printable/christmas-memory-lane/): care homes. [Office Party Escape]({DOMAIN}/play-online/office-party-escape/): work teams. [Advent calendar]({DOMAIN}/printable/advent-calendar/).\n\n"
    "## Tools\n"
    f"- [Christmas escape room builder]({DOMAIN}/tools/escape-room-builder/): make a custom printable escape room by age and hiding places.\n"
    f"- [Christmas cipher maker]({DOMAIN}/tools/christmas-cipher-maker/): pigpen, Caesar and number codes with printable key.\n"
    f"- [Escape room timer]({DOMAIN}/tools/escape-room-timer/): countdown with hint counter.\n"
    f"- [Certificate maker]({DOMAIN}/tools/certificate-maker/): printable 'You saved Christmas!' certificate.\n\n"
    "## Guides\n"
    f"- [How to make a Christmas escape room at home]({DOMAIN}/how-to/make-a-christmas-escape-room/)\n")
open(os.path.join(OUT, "404.html"), "w").write(open(os.path.join(OUT, "index.html")).read().replace("<head>", "<head>\n<base href=\"/\">", 1).replace("<title>", "<title>Page not found – ", 1).replace('content="index, follow, max-image-preview:large"', 'content="noindex"'))
print("\n".join(urls))
