"""Shared layout for christmasescaperoom.co.uk static pages."""
import json, os, re

DOMAIN = "https://christmasescaperoom.co.uk"
SITE = "Christmas Escape Room"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs")
PERSON_ID = DOMAIN + "/about/#paul"


def byline():
    return ('<p class="byline">By <a href="' + '{R}' + 'about/index.html" rel="author">Paul</a>, creator of Christmas Escape Room · '
            'Updated <time datetime="2026-11-22">22 November 2026</time></p>')

LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true"><rect x="5" y="13" width="22" height="16" rx="3" fill="#b3263a"/>'
        '<path d="M10 13V9a6 6 0 0 1 12 0v4" fill="none" stroke="#c9a24a" stroke-width="3"/>'
        '<circle cx="16" cy="20" r="2.4" fill="#fbf6ec"/><rect x="15" y="21" width="2" height="4" fill="#fbf6ec"/></svg>')

NAV = [("Play online", "play-online/index.html"), ("Printable", "printable/index.html"),
       ("Tools", "tools/index.html"), ("How to", "how-to/make-a-christmas-escape-room/index.html"),
       ("About", "about/index.html")]


def rel(depth):
    return "../" * depth


def page(path, title, description, body, crumbs=None, schema=None, active=None, extra_head="", og_image="assets/og/default.png", robots="index, follow, max-image-preview:large"):
    """path like 'tools/timer/' ('' for home). crumbs: list of (name, path)."""
    depth = path.count("/")
    r = rel(depth)
    body = body.replace("{R}", r)
    canonical = DOMAIN + "/" + path
    nav = "".join(
        f'<a href="{r}{href}"{" aria-current=\"page\"" if active == name else ""}>{name}</a>' for name, href in NAV)
    graph = [{
        "@type": "Organization", "@id": DOMAIN + "/#org", "name": SITE, "url": DOMAIN + "/",
        "description": "Christmas Escape Room (christmasescaperoom.co.uk) is a free UK site of Christmas escape room games to play online or print at home, plus puzzle tools.",
        "email": "hello@christmasescaperoom.co.uk", "founder": {"@id": PERSON_ID}, "logo": DOMAIN + "/assets/favicon.svg"
    }, {"@type": "Person", "@id": PERSON_ID, "name": "Paul", "url": DOMAIN + "/about/", "jobTitle": "Creator and puzzle writer, Christmas Escape Room",
        "worksFor": {"@id": DOMAIN + "/#org"}}, {"@type": "WebSite", "@id": DOMAIN + "/#site", "name": SITE, "url": DOMAIN + "/", "publisher": {"@id": DOMAIN + "/#org"}, "inLanguage": "en-GB"}]
    crumb_html = ""
    if crumbs:
        items = [("Home", "")] + crumbs
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + "/" + p} for i, (n, p) in enumerate(items)]})
        lis = "".join(
            f'<li><a href="{r}{p}index.html">{n}</a></li>' if i < len(items) - 1 else f'<li aria-current="page">{n}</li>'
            for i, (n, p) in enumerate(items))
        crumb_html = f'<nav class="crumbs wrap" aria-label="Breadcrumb"><ol>{lis}</ol></nav>'
    if schema:
        graph.extend(schema if isinstance(schema, list) else [schema])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    html = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="en_GB">
<meta property="og:image" content="{DOMAIN}/{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{DOMAIN}/{og_image}">
<meta name="author" content="Paul">
<meta name="theme-color" content="#0c2a22">
<link rel="icon" href="{r}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/style.css">
{extra_head}<script type="application/ld+json">
{ld}
</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="logo" href="{r}index.html">{LOGO}<span>Christmas Escape Room</span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
<nav class="nav" id="nav" aria-label="Main">{nav}</nav>
</div></header>
{crumb_html}
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><h4>Christmas Escape Room</h4><p>Free Christmas escape room games for families, classrooms, care homes and office parties. Made in the UK.</p></div>
<div><h4>Play</h4><ul><li><a href="{r}play-online/index.html">Play online free</a></li><li><a href="{r}play-online/the-missing-sleigh-key/index.html">The Missing Sleigh Key</a></li><li><a href="{r}play-online/reindeer-team-race/index.html">Team game for Microsoft Teams</a></li><li><a href="{r}play-online/office-party-escape/index.html">Office party escape room</a></li><li><a href="{r}printable/index.html">Printable games</a></li><li><a href="{r}printable/scrooges-safe/index.html">For adults</a> · <a href="{r}printable/elf-academy-final-exam/index.html">Teens</a></li><li><a href="{r}printable/rudolphs-lost-bells/index.html">Toddlers</a> · <a href="{r}printable/christmas-memory-lane/index.html">Care homes</a></li><li><a href="{r}printable/advent-calendar/index.html">Advent</a> · <a href="{r}printable/christmas-eve/index.html">Christmas Eve</a></li><li><a href="{r}printable/boxing-day/index.html">Boxing Day</a> · <a href="{r}printable/new-years-eve/index.html">New Year’s Eve</a></li><li><a href="{r}printable/ks2-classroom/index.html">KS2 classroom</a> · <a href="{r}play-online/ten-minute-christmas-escape-room/index.html">10-minute game</a></li></ul></div>
<div><h4>Tools</h4><ul><li><a href="{r}tools/escape-room-builder/index.html">Escape room builder</a></li><li><a href="{r}tools/christmas-cipher-maker/index.html">Christmas cipher maker</a></li><li><a href="{r}tools/escape-room-timer/index.html">Escape room timer</a></li><li><a href="{r}tools/certificate-maker/index.html">Certificate maker</a></li></ul></div>
<div><h4>Guides</h4><ul><li><a href="{r}how-to/make-a-christmas-escape-room/index.html">How to make a Christmas escape room</a></li><li><a href="{r}how-to/christmas-riddles-with-answers/index.html">30 Christmas riddles with answers</a></li><li><a href="{r}about/index.html">About Paul</a></li><li>hello@christmasescaperoom.co.uk</li></ul></div>
</div>
<p class="copyright">© <span id="year">2026</span> Christmas Escape Room · christmasescaperoom.co.uk · Free to use at home, school and work.</p>
</div></footer>
<script src="{r}assets/site.js" defer></script>
</body>
</html>
"""
    html = re.sub(r'href="([^"#:]*?)index\.html', lambda m: 'href="' + (m.group(1) or './'), html)
    d = os.path.join(OUT, path)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w") as f:
        f.write(html)
    return canonical


def faq_schema(qas):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qas]}


def faq_html(qas):
    items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in qas)
    return f'<section class="faq"><h2>Frequently asked questions</h2>{items}</section>'


def spec_table(rows):
    trs = "".join(f"<tr><th scope=\"row\">{k}</th><td>{v}</td></tr>" for k, v in rows)
    return f'<table class="spec"><tbody>{trs}</tbody></table>'


def article_schema(path, headline, description):
    return {"@type": "Article", "headline": headline, "description": description,
            "url": DOMAIN + "/" + path, "inLanguage": "en-GB", "datePublished": "2026-11-22", "dateModified": "2026-11-22",
            "author": {"@id": DOMAIN + "/#org"}, "publisher": {"@id": DOMAIN + "/#org"}}
