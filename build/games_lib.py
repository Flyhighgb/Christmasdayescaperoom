"""Reusable builders for printable and online escape room game pages."""
import base64, json
from layout import page, faq_html, faq_schema, spec_table, DOMAIN, byline, PERSON_ID

# Paste each Gumroad product URL here once listed; the button appears automatically.
GUMROAD = {
    "the-great-pudding-heist": "",
    "scrooges-safe": "",
    "elf-academy-final-exam": "",
    "rudolphs-lost-bells": "",
    "christmas-memory-lane": "",
    "advent-calendar": "",
    "christmas-eve": "",
    "boxing-day": "",
    "new-years-eve": "",
    "ks2-classroom": "",
}

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def b64(s):
    return base64.b64encode(s.encode()).decode()


def pig(c, s=40):
    i = ALPHA.index(c)
    m, e, h = 4, s - 4, s / 2
    st = 'stroke="#0c2a22" stroke-width="3.2" fill="none" stroke-linecap="round"'
    out, dot = "", False
    if i < 18:
        dot = i >= 9
        k = i % 9; r, col = divmod(k, 3)
        if r > 0: out += f'<line x1="{m}" y1="{m}" x2="{e}" y2="{m}" {st}/>'
        if r < 2: out += f'<line x1="{m}" y1="{e}" x2="{e}" y2="{e}" {st}/>'
        if col > 0: out += f'<line x1="{m}" y1="{m}" x2="{m}" y2="{e}" {st}/>'
        if col < 2: out += f'<line x1="{e}" y1="{m}" x2="{e}" y2="{e}" {st}/>'
    else:
        k = i - 18; dot = k >= 4; q = k % 4
        pts = [[(m, m), (h, e), (e, m)], [(m, m), (e, h), (m, e)], [(e, m), (m, h), (e, e)], [(m, e), (h, m), (e, e)]][q]
        out += '<polyline points="' + " ".join(f"{x},{y}" for x, y in pts) + f'" {st}/>'
    if dot: out += f'<circle cx="{h}" cy="{h}" r="3.4" fill="#b3263a"/>'
    return f'<svg width="{s}" height="{s}" viewBox="0 0 {s} {s}" aria-hidden="true">{out}</svg>'


def pig_word(w, s=40):
    return '<div style="display:flex;gap:6px;justify-content:center;flex-wrap:wrap;background:#fff;padding:14px;border-radius:12px;border:2px solid #e6dccb">' + "".join(pig(c, s) for c in w) + "</div>"


def pig_key(s=30):
    cells = "".join(f'<div style="text-align:center;font-weight:700;font-size:.8rem">{pig(c, s)}{c}</div>' for c in ALPHA)
    return f'<div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center">{cells}</div>'


def gumroad_button(slug, label="Get the print-ready PDF"):
    url = GUMROAD.get(slug, "")
    if not url:
        return ""
    return f'<a class="btn gold" href="{url}" rel="nofollow">{label}</a>'


def printable_game(*, slug, name, h1, title, description, answer, spec, story, cards, finale, faq, ages_min,
                   players, minutes, extra_sections="", easier="", harder="", related=(), audience=""):
    """cards: list of dict(title, intro, html, hide, answer, explain)."""
    path = f"printable/{slug}/"
    cards_html = "".join(
        f'<article class="clue-card"><div class="num">Card {i+1}</div><h3>{c["title"]}</h3>'
        f'<p><em>{c["intro"]}</em></p>{c["html"]}<p class="hide-where no-print">🧑‍🎄 Host: {c["hide"]}</p></article>'
        for i, c in enumerate(cards))
    cards_html += (f'<article class="clue-card"><div class="num">Final card</div><h3>{finale["title"]}</h3>{finale["html"]}'
                   f'<p class="hide-where no-print">🧑‍🎄 Host: {finale["hide"]}</p></article>')
    key_rows = "".join(f"<tr><td>Card {i+1}</td><td><strong>{c['answer']}</strong></td><td>{c['explain']}</td></tr>" for i, c in enumerate(cards))
    breakdown = "".join(f"<li><strong>{c['title']}:</strong> {c.get('type', '')}</li>" for c in cards)
    gb = gumroad_button(slug)
    rel = "".join(f'<li><a href="../../{p}index.html">{n}</a>{": " + d if d else ""}</li>' for n, p, d in related)
    body = f"""
<div class="wrap narrow">
<p class="eyebrow">Printable · Free{(' · ' + audience) if audience else ''}</p>
<h1>{h1}</h1>
{byline()}
<p class="answer">{answer}</p>
{spec_table(spec)}
<div class="btn-row no-print"><button class="btn" data-print>Print the clue cards</button>{gb}<a class="btn ghost" href="#answer-key">Answer key</a></div>
<p id="print-note" class="callout no-print" hidden>If nothing happened, press <strong>Ctrl + P</strong> (Windows) or <strong>⌘ + P</strong> (Mac). Each card prints on its own page; host notes don’t print.</p>
<div class="no-print" id="guide">
<h2>The story</h2>
<p>{story}</p>
<h2>What’s in the game</h2>
<ol>{breakdown}</ol>
<h2>How to set it up</h2>
<ol class="steps">
<li>Print the cards below. Each card prints on its own sheet and the host notes are left off.</li>
<li>Hide each card in the place shown in its host note and in the answer key. Start from the last card and work backwards.</li>
<li>{finale['setup']}</li>
<li>Start the <a href="../../tools/escape-room-timer/index.html">escape room timer</a> and hand Card 1 to the players.</li>
</ol>
{extra_sections}
<h2>The clue cards</h2>
</div>
<div class="print-only"><h1>{name}</h1><p>christmasescaperoom.co.uk · free printable Christmas escape room</p></div>
{cards_html}
<section id="answer-key" class="no-print">
<h2>Answer key</h2>
<table class="compare"><thead><tr><th>Card</th><th>Answer</th><th>How it works</th></tr></thead><tbody>{key_rows}</tbody></table>
<h3>Make it easier or harder</h3>
<ul><li><strong>Easier:</strong> {easier}</li><li><strong>Harder:</strong> {harder}</li></ul>
</section>
<div class="no-print">
{faq_html(faq)}
<h2>Try next</h2>
<ul>{rel}</ul>
</div>
</div>"""
    schema = {"@type": ["Game", "CreativeWork"], "name": name, "url": DOMAIN + "/" + path, "description": description,
              "isAccessibleForFree": True, "inLanguage": "en-GB", "typicalAgeRange": f"{ages_min}-",
              "numberOfPlayers": {"@type": "QuantitativeValue", "minValue": players[0], "maxValue": players[1]},
              "timeRequired": f"PT{minutes}M", "author": {"@id": PERSON_ID}, "publisher": {"@id": DOMAIN + "/#org"},
              "image": f"{DOMAIN}/assets/og/{slug}.png", "dateModified": "2026-11-22"}
    page(path, title, description, body, crumbs=[("Printable", "printable/"), (name, path)],
         schema=[schema, faq_schema(faq)], active="Printable", og_image=f"assets/og/{slug}.png")
    return path


ONLINE_JS = """
<script>
(function(){
var P=__DATA__, NAME=__NAME__, i=0, start=null, tick=null, hints=0;
var box=document.getElementById('game'), prog=document.getElementById('progress'), clock=document.getElementById('clock');
function norm(s){return (s||'').toUpperCase().replace(/[^A-Z0-9]/g,'')}
function fmt(ms){var s=Math.floor(ms/1000);return String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0')}
function bar(){prog.innerHTML=P.map(function(_,k){return '<span class="'+(k<i?'done':k===i?'now':'')+'"></span>'}).join('')}
function show(){
  bar(); var p=P[i];
  box.innerHTML='<p class="eyebrow">'+p.t+'</p><p>'+p.s+'</p>'+p.h+
   '<form class="answer-row" id="f"><label class="skip" for="ans">Your answer</label><input id="ans" type="text" autocomplete="off" inputmode="'+(p.n?'numeric':'text')+'" placeholder="'+(p.n?'Enter the code':'Type your answer')+'"><button class="btn" type="submit">Unlock</button></form>'+
   '<div class="msg" id="m" aria-live="polite"></div><div class="hint" id="hint"><button type="button">Need a hint?</button><p>'+p.hint+'</p></div>';
  document.querySelector('#hint button').onclick=function(){var h=document.getElementById('hint');if(!h.classList.contains('open')){hints++}h.classList.add('open')};
  document.getElementById('f').onsubmit=function(e){e.preventDefault();
    var v=norm(document.getElementById('ans').value), m=document.getElementById('m');
    if(!v){m.className='msg bad';m.textContent='Type an answer first.';return}
    if(p.a.indexOf(btoa(v))>-1){ if(p.f){m.className='msg good';m.textContent='Unlocked! '+p.f;}
      setTimeout(function(){i++; if(i<P.length){show()}else{win()}}, p.f?1600:300);
    } else {m.className='msg bad';m.textContent='Not quite – try again.';}
  };
}
function win(){
  clearInterval(tick); bar(); var t=fmt(Date.now()-start);
  try{localStorage.setItem('cer-last',JSON.stringify({game:NAME,time:t}))}catch(e){}
  box.innerHTML='<div class="win">'+__WIN__+'<p><span class="timer-chip">Your time: '+t+'</span> <span class="timer-chip">Hints used: '+hints+'</span></p><div class="btn-row" style="justify-content:center"><a class="btn" href="../../tools/certificate-maker/index.html">Make your certificate</a><a class="btn ghost" href="../index.html">More games</a></div></div>';
}
document.getElementById('begin').onclick=function(){
  document.getElementById('intro').hidden=true; box.hidden=false; start=Date.now();
  tick=setInterval(function(){clock.textContent=fmt(Date.now()-start)},500); document.getElementById('clockwrap').hidden=false; show();
};
document.getElementById('reveal').onclick=function(){document.getElementById('ans-list').hidden=false;this.hidden=true};
})();
</script>"""


def online_game(*, slug, name, h1, title, description, answer, spec, intro_title, intro, puzzles, win_html, faq,
                ages_min, players, minutes, how_to_play, extra_sections="", related=(), audience=""):
    path = f"play-online/{slug}/"
    data = [{"t": p["title"], "s": p["story"], "h": p["html"], "hint": p["hint"], "a": [b64(a) for a in p["answers"]],
             "n": p.get("numeric", False), "f": p.get("found", "")} for p in puzzles]
    answers_list = "".join(f"<li><strong>{p['title'].split(' · ')[0]}:</strong> {p['answers'][0]} – {p.get('explain', '')}</li>" for p in puzzles)
    breakdown = "".join(f"<li><strong>{p['title'].split(' · ')[1]}:</strong> {p.get('type', '')}</li>" for p in puzzles)
    rel = "".join(f'<li><a href="../../{p}index.html">{n}</a>{": " + d if d else ""}</li>' for n, p, d in related)
    js = ONLINE_JS.replace("__DATA__", json.dumps(data, ensure_ascii=False)).replace("__NAME__", json.dumps(name)).replace("__WIN__", json.dumps(win_html, ensure_ascii=False))
    body = f"""
<div class="wrap narrow">
<p class="eyebrow">Play online · Free{(' · ' + audience) if audience else ''}</p>
<h1>{h1}</h1>
{byline()}
<p class="answer">{answer}</p>
{spec_table(spec)}
<section class="game" style="margin-top:28px" aria-label="Game">
<p id="clockwrap" hidden><span class="timer-chip">⏱ <span id="clock">00:00</span></span></p>
<div class="progress" id="progress" aria-hidden="true"></div>
<div id="intro"><h2 style="margin-top:0">{intro_title}</h2><p>{intro}</p><button class="btn" id="begin">Start the game</button></div>
<div id="game" hidden></div>
</section>
<h2>How to play</h2>
<ol class="steps">{how_to_play}</ol>
<h2>What’s in the game</h2>
<ol>{breakdown}</ol>
{extra_sections}
<h2>Answers</h2>
<p>Only peek if you’re really stuck.</p>
<button class="btn ghost small" id="reveal">Show answers</button>
<ol id="ans-list" hidden>{answers_list}</ol>
{faq_html(faq)}
<h2>Try next</h2>
<ul>{rel}</ul>
</div>
{js}"""
    schema = {"@type": ["Game", "CreativeWork"], "name": name, "url": DOMAIN + "/" + path, "description": description,
              "isAccessibleForFree": True, "inLanguage": "en-GB", "typicalAgeRange": f"{ages_min}-",
              "numberOfPlayers": {"@type": "QuantitativeValue", "minValue": players[0], "maxValue": players[1]},
              "timeRequired": f"PT{minutes}M", "author": {"@id": PERSON_ID}, "publisher": {"@id": DOMAIN + "/#org"},
              "image": f"{DOMAIN}/assets/og/{slug}.png", "dateModified": "2026-11-22"}
    page(path, title, description, body, crumbs=[("Play online", "play-online/"), (name, path)],
         schema=[schema, faq_schema(faq)], active="Play online", og_image=f"assets/og/{slug}.png")
    return path
