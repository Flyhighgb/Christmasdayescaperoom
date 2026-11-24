"""Reindeer Rescue: Team Race — a free multi-team game for Microsoft Teams, Zoom and office parties.
No server: each team gets a signed finish code; the host pastes the chat into the leaderboard."""
import base64, json
from layout import page, faq_html, faq_schema, spec_table, DOMAIN, byline, PERSON_ID

SALT = "rr-2026-mistletoe"
SLUG = "reindeer-team-race"
PATH = f"play-online/{SLUG}/"
LB_PATH = f"play-online/{SLUG}/leaderboard/"


def b64(s):
    return base64.b64encode(s.encode()).decode()


def grid_html():
    path = {("C", 3): "L", ("C", 1): "I", ("E", 1): "C", ("E", 2): "H", ("B", 2): "E", ("B", 5): "N"}
    filler = iter("SRAOTMKUDPGWYBFVZJXQ")
    rows = ""
    for r in range(1, 6):
        rows += f"<tr><th>{r}</th>"
        for c in "ABCDE":
            rows += f"<td>{path.get((c, r)) or next(filler)}</td>"
        rows += "</tr>"
    return f'<table class="sheet"><tr><th></th><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th></tr>{rows}</table>'


PUZZLES = [
    {"t": "Puzzle 1 · The runaway", "type": "an anagram of a reindeer’s name",
     "s": "It’s the night before Christmas Eve and Santa’s reindeer have escaped from the stables! The first runaway left their name tag in the snow, but the letters are jumbled.",
     "h": '<div class="puzzle-box">T N B Z I L E</div><p>Which reindeer is it?</p>',
     "hint": "Their name means ‘lightning’ and is often paired with Donner.", "a": ["BLITZEN"], "explain": "anagram of TNBZILE."},
    {"t": "Puzzle 2 · The name tags", "type": "a counting puzzle",
     "s": "Blitzen says the others are hiding nearby. Santa needs new name tags for all eight of his original reindeer:",
     "h": '<div class="poem">DASHER · DANCER · PRANCER · VIXEN<br>COMET · CUPID · DONNER · BLITZEN</div><p>How many letters will Santa need to print <strong>in total</strong>? <em>Remember this number!</em></p>',
     "hint": "Count each name: DASHER = 6, DANCER = 6, PRANCER = 7… then add them up.", "a": ["47"], "n": True, "explain": "6+6+7+5+5+5+6+7 = 47."},
    {"t": "Puzzle 3 · Hoofprints in the snow", "type": "a grid-and-directions puzzle",
     "s": "The reindeer have left hoofprints across the snowy field. Follow them to find out what they’ve been eating.",
     "h": grid_html() + '<div class="poem">Start on <strong>C3</strong> and write down the letter.<br>Move <strong>up 2</strong> → write the letter.<br>Move <strong>right 2</strong> → write the letter.<br>Move <strong>down 1</strong> → write the letter.<br>Move <strong>left 3</strong> → write the letter.<br>Move <strong>down 3</strong> → write the letter.</div>',
     "hint": "Row 1 is at the top, so ‘up’ means a smaller row number. It’s a real reindeer food that grows on rocks.", "a": ["LICHEN"], "explain": "C3 L, C1 I, E1 C, E2 H, B2 E, B5 N."},
    {"t": "Puzzle 4 · The coded sign", "type": "a Caesar shift",
     "s": "A sign in the field is written in reindeer code. Each letter has moved forward by the number of reindeer in Santa’s original team (not counting Rudolph).",
     "h": '<div class="puzzle-box">A B I J T M</div><p>Move each letter <strong>back</strong> that many places.</p>',
     "hint": "There are 8 original reindeer. A goes back 8 to S.", "a": ["STABLE", "STABLES"], "explain": "shift each letter back 8."},
    {"t": "Puzzle 5 · Who’s in stall 1?", "type": "a logic puzzle",
     "s": "Five reindeer are back in the stable, sleeping in stalls 1 to 5 from left to right: Comet, Cupid, Dasher, Vixen and Dancer.",
     "h": '<ol class="poem" style="padding-left:2.2em"><li>Comet is in stall 3.</li><li>Cupid is next to Comet, on Comet’s left.</li><li>Dasher is in the last stall.</li><li>Vixen is not in stall 1.</li></ol><p>Which reindeer is in stall 1? <em>And which stall is Vixen in? You’ll need it.</em></p>',
     "hint": "Comet 3, Cupid 2, Dasher 5. That leaves stalls 1 and 4 for Vixen and Dancer.", "a": ["DANCER"], "explain": "Comet 3, Cupid 2, Dasher 5, Vixen 4, Dancer 1."},
    {"t": "Puzzle 6 · The stable lock", "type": "a final code using earlier answers",
     "s": "All the reindeer are home. Lock the stable door so they can’t escape again!",
     "h": '<div class="poem">The code is <strong>Vixen’s stall number</strong> followed by your answer to <strong>Puzzle 2</strong>.</div><div class="puzzle-box">_ &nbsp; _ &nbsp; _</div>',
     "hint": "Vixen is in stall 4. Puzzle 2’s answer was 47.", "a": ["447"], "n": True, "explain": "Vixen’s stall 4, then 47."},
]

HASH_JS = "function rrHash(s){var h=2166136261;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619)>>>0}return h}" \
          f"function rrCheck(room,team,secs,hints){{return (rrHash(room+'|'+team+'|'+secs+'|'+hints+'|{SALT}')%46656).toString(36).toUpperCase().padStart(3,'0')}}"

GAME_JS = """
<script>
(function(){
__HASH__
var P=__DATA__, i=0, start=null, tick=null, hints=0, ROOM='', TEAM='';
var box=document.getElementById('game'), prog=document.getElementById('progress'), clock=document.getElementById('clock');
function norm(s){return (s||'').toUpperCase().replace(/[^A-Z0-9]/g,'')}
function fmt(s){return String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0')}
function el(){return Math.floor((Date.now()-start)/1000)}
function bar(){prog.innerHTML=P.map(function(_,k){return '<span class="'+(k<i?'done':k===i?'now':'')+'"></span>'}).join('')}
function show(){
  bar(); var p=P[i];
  box.innerHTML='<p class="eyebrow">'+p.t+'</p><p>'+p.s+'</p>'+p.h+
   '<form class="answer-row" id="f"><label class="skip" for="ans">Your answer</label><input id="ans" type="text" autocomplete="off" inputmode="'+(p.n?'numeric':'text')+'" placeholder="'+(p.n?'Enter the number':'Type your answer')+'"><button class="btn" type="submit">Unlock</button></form>'+
   '<div class="msg" id="m" aria-live="polite"></div><div class="hint" id="hint"><button type="button">Need a hint? (counts against your team)</button><p>'+p.hint+'</p></div>';
  document.querySelector('#hint button').onclick=function(){var h=document.getElementById('hint');if(!h.classList.contains('open')){hints++}h.classList.add('open')};
  document.getElementById('f').onsubmit=function(e){e.preventDefault();
    var v=norm(document.getElementById('ans').value), m=document.getElementById('m');
    if(!v){m.className='msg bad';m.textContent='Type an answer first.';return}
    if(p.a.indexOf(btoa(v))>-1){m.className='msg good';m.textContent='Correct!';setTimeout(function(){i++; if(i<P.length){show()}else{win()}},500)}
    else{m.className='msg bad';m.textContent='Not quite. Try again.'}
  };
}
function win(){
  clearInterval(tick); bar(); var secs=el(), h=Math.min(hints,9);
  var code='RR-'+ROOM+'-'+TEAM+'-'+secs+'-'+h+'-'+rrCheck(ROOM,TEAM,secs,h);
  try{localStorage.setItem('cer-last',JSON.stringify({game:'Reindeer Rescue: Team Race',time:fmt(secs)}))}catch(e){}
  box.innerHTML='<div class="win"><div style="font-size:3rem">🦌🏁</div><h2>All reindeer rescued!</h2><p><span class="timer-chip">Time: '+fmt(secs)+'</span> <span class="timer-chip">Hints: '+h+'</span></p>'+
   '<p><strong>Your team’s finish code:</strong></p><div class="puzzle-box" id="code" style="font-size:1.1rem;letter-spacing:.06em;user-select:all">'+code+'</div>'+
   '<p>Paste it into your <strong>Teams or Zoom chat</strong>, or send it to your host.</p>'+
   '<div class="btn-row" style="justify-content:center"><button class="btn" id="copy">Copy finish code</button><a class="btn ghost" href="../../tools/certificate-maker/">Make a certificate</a></div></div>';
  document.getElementById('copy').onclick=function(){var b=this;try{navigator.clipboard.writeText(code).then(function(){b.textContent='Copied!'},function(){b.textContent='Select the code above and copy it'})}catch(e){b.textContent='Select the code above and copy it'}};
}
document.getElementById('setup').onsubmit=function(e){e.preventDefault();
  var r=norm(document.getElementById('room').value).replace(/[^A-Z]/g,'').slice(0,4), t=norm(document.getElementById('team').value).slice(0,14), m=document.getElementById('sm');
  if(r&&r.length!==4){m.className='msg bad';m.textContent='Room codes are 4 letters. Check with your host, or leave it blank to play just for fun.';return}
  if(!t){m.className='msg bad';m.textContent='Give your team a name.';return}
  ROOM=r||'OPEN'; TEAM=t;
  document.getElementById('intro').hidden=true; box.hidden=false; start=Date.now();
  document.getElementById('teamchip').textContent='Team '+TEAM+' · Room '+ROOM;
  tick=setInterval(function(){clock.textContent=fmt(el())},500); document.getElementById('clockwrap').hidden=false; show();
};
var q=(location.hash||'').replace('#','').toUpperCase(); if(/^[A-Z]{4}$/.test(q)){document.getElementById('room').value=q}
document.getElementById('reveal').onclick=function(){document.getElementById('ans-list').hidden=false;this.hidden=true};
})();
</script>"""

LB_JS = """
<script>
(function(){
__HASH__
var L='BCDFGHJKLMNPQRSTVWXZ', roomEl=document.getElementById('roomcode'), ROOM='';
function newRoom(){ROOM='';for(var i=0;i<4;i++){ROOM+=L[Math.floor(Math.random()*L.length)]}roomEl.textContent=ROOM;
  document.getElementById('joinline').textContent='🦌 Reindeer Rescue team race! Open https://christmasescaperoom.co.uk/play-online/reindeer-team-race/#'+ROOM+' · Room code: '+ROOM+' · Enter your team name and wait for GO!';
  try{sessionStorage.setItem('rr-room',ROOM)}catch(e){} }
try{ROOM=sessionStorage.getItem('rr-room')||''}catch(e){}
if(ROOM){roomEl.textContent=ROOM;document.getElementById('joinline').textContent='🦌 Reindeer Rescue team race! Open https://christmasescaperoom.co.uk/play-online/reindeer-team-race/#'+ROOM+' · Room code: '+ROOM+' · Enter your team name and wait for GO!'}else{newRoom()}
document.getElementById('newroom').onclick=newRoom;
document.getElementById('copyjoin').onclick=function(){var b=this,t=document.getElementById('joinline').textContent;try{navigator.clipboard.writeText(t).then(function(){b.textContent='Copied!'},function(){b.textContent='Select the text and copy it'})}catch(e){b.textContent='Select the text and copy it'}};
function fmt(s){return String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0')}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
document.getElementById('score').onclick=function(){
  var txt=document.getElementById('paste').value.toUpperCase(), pen=+document.getElementById('pen').value, only=document.getElementById('onlyroom').checked;
  var re=/RR-([A-Z]{4})-([A-Z0-9]{1,14})-(\\d{1,5})-(\\d)-([A-Z0-9]{3})/g, m, ok={}, bad=[], other=0;
  while((m=re.exec(txt))){
    var room=m[1],team=m[2],secs=+m[3],h=+m[4],chk=m[5];
    if(rrCheck(room,team,secs,h)!==chk){bad.push(m[0]);continue}
    if(only&&ROOM&&room!==ROOM){other++;continue}
    var key=room+'|'+team, total=secs+h*pen*60;
    if(!ok[key]||total<ok[key].total){ok[key]={team:team,room:room,secs:secs,h:h,total:total}}
  }
  var list=Object.keys(ok).map(function(k){return ok[k]}).sort(function(a,b){return a.total-b.total});
  var out=document.getElementById('results');
  if(!list.length){out.innerHTML='<p class="msg bad">No valid finish codes found'+(other?' for room '+ROOM+' ('+other+' from other rooms)':'')+'. Codes look like RR-SNOW-SPROUTS-1455-2-K7Q.</p>';return}
  var medals=['🥇','🥈','🥉'];
  var pod='<div class="grid" style="margin:10px 0 20px">'+list.slice(0,3).map(function(r,k){return '<div class="card" style="text-align:center"><div style="font-size:2.6rem">'+medals[k]+'</div><h3>'+esc(r.team)+'</h3><p>'+fmt(r.total)+'</p></div>'}).join('')+'</div>';
  var rows=list.map(function(r,k){return '<tr><td>'+(k+1)+'</td><td><strong>'+esc(r.team)+'</strong></td><td>'+fmt(r.secs)+'</td><td>'+r.h+'</td><td><strong>'+fmt(r.total)+'</strong></td></tr>'}).join('');
  out.innerHTML='<h2>Results</h2>'+pod+'<table class="compare"><thead><tr><th>#</th><th>Team</th><th>Time</th><th>Hints</th><th>Final time'+(pen?' (+'+pen+' min per hint)':'')+'</th></tr></thead><tbody>'+rows+'</tbody></table>'+
   (bad.length?'<p class="msg bad">'+bad.length+' code(s) didn’t check out and were ignored (typed wrongly or edited).</p>':'')+
   (other?'<p style="color:#5d574d">'+other+' code(s) from other rooms were ignored.</p>':'')+
   '<div class="btn-row"><a class="btn" href="../../../tools/certificate-maker/">Print winners’ certificates</a></div>';
  try{out.scrollIntoView({behavior:'smooth'})}catch(e){}
};
})();
</script>"""


def build():
    data = [{"t": p["t"], "s": p["s"], "h": p["h"], "hint": p["hint"], "a": [b64(a) for a in p["a"]], "n": p.get("n", False)} for p in PUZZLES]
    js = GAME_JS.replace("__HASH__", HASH_JS).replace("__DATA__", json.dumps(data, ensure_ascii=False))
    answers = "".join(f"<li><strong>{p['t'].split(' · ')[0]}:</strong> {p['a'][0]} ({p['explain']})</li>" for p in PUZZLES)
    breakdown = "".join(f"<li><strong>{p['t'].split(' · ')[1]}:</strong> {p['type']}.</li>" for p in PUZZLES)
    faq = [
        ("Is there a free Christmas team game for Microsoft Teams?", "Yes. Reindeer Rescue: Team Race is free and made for Teams and Zoom. The host shares a 4-letter room code, teams play in breakout rooms on their own laptops, and each team pastes its finish code into the meeting chat. The host pastes the chat into the free leaderboard to rank every team."),
        ("How many teams can play?", "As many as you like. There’s no server and no sign-up, so 3 teams or 300 teams works the same."),
        ("How long does it take?", "Most teams finish in 20–30 minutes, so with instructions and results it fits a 45-minute slot."),
        ("Do players need to install anything or sign up?", "No. Everyone just opens the link in a browser on a laptop, tablet or phone."),
        ("Can teams cheat?", "Each finish code includes a check, so a typed-in or edited time is rejected by the leaderboard. Codes only count for the room code the host shares, so old codes can’t be reused."),
        ("Does it work in the office, without Teams?", "Yes. Give each table a laptop, start together, and have teams read or message their finish codes to the host."),
        ("Is it free for companies?", "Yes, it’s free for any office, school or club. A link back to the site is always appreciated."),
    ]
    body = f"""
<div class="wrap narrow">
<p class="eyebrow">Play online · Free · Work teams</p>
<h1>Reindeer Rescue: free virtual Christmas team game for Teams and Zoom</h1>
{byline()}
<p class="answer">Reindeer Rescue: Team Race is a free Christmas team game for work parties on Microsoft Teams, Zoom or in the office. Teams of 2–6 race through six reindeer puzzles in 20–30 minutes, paste a finish code into the meeting chat, and the host’s free leaderboard ranks every team. Any number of teams can play, with no sign-up and no booking.</p>
{spec_table([("Players", "Teams of 2–6; any number of teams"), ("Time", "20–30 minutes (45 minutes with intro and results)"), ("Works on", "Microsoft Teams, Zoom, Google Meet, or in the office"), ("Difficulty", "Medium"), ("You need", "One laptop, tablet or phone per team"), ("Host needs", "The free leaderboard page"), ("Cost", "Free, no sign-up")])}
<div class="btn-row"><a class="btn gold" href="leaderboard/">I’m the host: get a room code</a><a class="btn ghost" href="#play">I’m a player</a></div>

<section class="game" id="play" style="margin-top:28px" aria-label="Game">
<p id="clockwrap" hidden><span class="timer-chip">⏱ <span id="clock">00:00</span></span> <span class="timer-chip" id="teamchip"></span></p>
<div class="progress" id="progress" aria-hidden="true"></div>
<div id="intro">
<h2 style="margin-top:0">Ready to rescue the reindeer?</h2>
<p>Santa’s reindeer have escaped the night before Christmas Eve. Your team has six puzzles to round them up. Enter the room code from your host (leave it blank to play just for fun) and your team name, then wait for the host to say <strong>“Go!”</strong></p>
<form id="setup" autocomplete="off"><div class="row">
<div class="field"><label for="room">Room code (4 letters)</label><input id="room" type="text" maxlength="4" placeholder="e.g. SNWX" style="text-transform:uppercase;letter-spacing:.2em"></div>
<div class="field"><label for="team">Team name</label><input id="team" type="text" maxlength="20" placeholder="e.g. The Sprouts"></div>
</div><button class="btn" type="submit">Start the race</button><div class="msg" id="sm" aria-live="polite"></div></form>
</div>
<div id="game" hidden></div>
</section>

<h2>How to run it on Microsoft Teams</h2>
<ol class="steps">
<li><strong>Host:</strong> open the <a href="leaderboard/">leaderboard page</a> and copy the join message. It includes your 4-letter room code.</li>
<li>Paste the join message into the <strong>Teams meeting chat</strong> and split everyone into <strong>breakout rooms</strong> of 2–6.</li>
<li>In each breakout room, one person opens the link and shares their screen while the team solves the puzzles together.</li>
<li>Say <strong>“Go!”</strong>. When a team finishes, they paste their <strong>finish code</strong> into the main meeting chat.</li>
<li>Bring everyone back, copy the whole meeting chat into the leaderboard page and press <strong>Show results</strong>. Share your screen for the podium.</li>
</ol>
<div class="callout">On Zoom or Google Meet it works the same way. In the office, give each table a laptop and ask teams to message or read out their codes.</div>
<p>Want it pinned in a Teams channel? Select <strong>+</strong> on the channel’s tab bar, choose <strong>Website</strong>, and paste this page’s address. Some company setups open website tabs in a browser window, which works just as well.</p>

<h2>What’s in the game</h2>
<ol>{breakdown}</ol>
<p>Puzzles build on each other: teams need answers from earlier puzzles to open the final lock, so everyone has to work together.</p>

<h2>Answers (for hosts)</h2>
<button class="btn ghost small" id="reveal">Show answers</button>
<ol id="ans-list" hidden>{answers}</ol>
{faq_html(faq)}
<h2>Try next</h2>
<ul><li><a href="../office-party-escape/">The Office Party Escape</a>: another free online game for work teams</li><li><a href="../../tools/escape-room-timer/">Escape room timer</a> for the big screen</li><li><a href="../../tools/certificate-maker/">Certificate maker</a> for the winners</li></ul>
</div>
{js}"""
    schema = {"@type": ["Game", "CreativeWork"], "name": "Reindeer Rescue: Team Race", "url": DOMAIN + "/" + PATH,
              "description": "Free multi-team Christmas game for Microsoft Teams, Zoom and office parties, with a free leaderboard.",
              "isAccessibleForFree": True, "inLanguage": "en-GB", "typicalAgeRange": "14-",
              "numberOfPlayers": {"@type": "QuantitativeValue", "minValue": 2},
              "timeRequired": "PT30M", "author": {"@id": PERSON_ID}, "publisher": {"@id": DOMAIN + "/#org"},
              "image": f"{DOMAIN}/assets/og/{SLUG}.png", "dateModified": "2026-11-24"}
    page(PATH, "Free Virtual Christmas Team Game for Microsoft Teams & Zoom",
         "Free Christmas team game for work: teams race through 6 reindeer puzzles on Microsoft Teams, Zoom or in the office. Unlimited teams, free leaderboard, no sign-up.",
         body, crumbs=[("Play online", "play-online/"), ("Reindeer Rescue: Team Race", PATH)],
         schema=[schema, faq_schema(faq)], active="Play online", og_image=f"assets/og/{SLUG}.png")

    # ---------------- Leaderboard (host) ----------------
    lbjs = LB_JS.replace("__HASH__", HASH_JS)
    body = f"""
<div class="wrap narrow">
<p class="eyebrow">Host tools</p>
<h1>Reindeer Rescue host leaderboard</h1>
<p class="answer">Share the room code below with your teams. When they finish, they post finish codes in the chat. Paste the whole chat here and press <strong>Show results</strong> to rank every team.</p>
<section class="game">
<h2 style="margin-top:0">1. Share your room code</h2>
<div class="puzzle-box" id="roomcode" style="font-size:2.6rem;letter-spacing:.3em">····</div>
<p id="joinline" style="background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px 14px"></p>
<div class="btn-row" style="margin-top:6px"><button class="btn" id="copyjoin" type="button">Copy join message</button><button class="btn ghost small" id="newroom" type="button">New room code</button></div>
<p style="font-size:.9rem;color:var(--muted)">Paste the join message into your Teams, Zoom or Slack chat. Players open the link, type the room code and their team name, then wait for you to say “Go!”.</p>
</section>
<section class="game" style="margin-top:20px">
<h2 style="margin-top:0">2. Paste the finish codes</h2>
<div class="field"><label for="paste">Paste the whole chat, or just the codes</label><textarea id="paste" rows="7" placeholder="e.g.&#10;Sam: we're out!! RR-SNWX-SPROUTS-1455-2-K7Q&#10;Priya: RR-SNWX-ELFSQUAD-1610-0-3ZD"></textarea></div>
<div class="row">
<div class="field"><label for="pen">Hint penalty</label><select id="pen"><option value="0">No penalty</option><option value="1" selected>+1 minute per hint</option><option value="2">+2 minutes per hint</option></select></div>
<div class="field" style="align-self:end"><label style="font-weight:400"><input type="checkbox" id="onlyroom" checked> Only count codes for this room</label></div>
</div>
<button class="btn gold" id="score" type="button">Show results</button>
</section>
<div id="results" style="margin-top:20px"></div>
<p style="margin-top:24px"><a href="../">← Back to the game page and host instructions</a></p>
</div>
{lbjs}"""
    page(LB_PATH, "Reindeer Rescue Leaderboard – Host Page",
         "Host page for Reindeer Rescue: Team Race. Get a room code, paste your Teams or Zoom chat, and rank every team’s finish code.",
         body, crumbs=[("Play online", "play-online/"), ("Reindeer Rescue", PATH), ("Leaderboard", LB_PATH)],
         active="Play online", og_image=f"assets/og/{SLUG}.png",
         robots="noindex, follow")
