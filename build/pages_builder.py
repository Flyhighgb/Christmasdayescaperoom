"""Escape room builder: generates a custom printable Christmas escape room."""
from layout import page, faq_html, faq_schema, DOMAIN, byline
from pages_tools import app_schema

PLACES = [
    # key, label, emoji, answer word, riddle (easy), riddle (hard)
    ("tree", "Christmas tree", "🎄", "TREE", "I have needles but never sew. I wear lights and baubles in a row.", "I have bark but never bite, and in December I’m dressed in light."),
    ("stocking", "Stocking", "🧦", "STOCKING", "I hang by the fire and wait to be filled on Christmas Eve.", "I’m empty all year, then full overnight, hung where the fire is glowing bright."),
    ("fridge", "Fridge", "🧊", "FRIDGE", "I hum all day and I’m cold inside, where the milk and butter hide.", "I keep the turkey cold for days, and my light goes off when you walk away."),
    ("sofa", "Sofa", "🛋️", "SOFA", "I have cushions and arms but no hands.", "I have arms but cannot hug, and four feet but I never move."),
    ("bed", "Bed", "🛏️", "BED", "You sleep in me every night.", "I have a head and a foot but no body, and you’re in me every night."),
    ("bath", "Bath", "🛁", "BATH", "Fill me with water and bubbles to get clean.", "I hold water but I’m not a cup, and I gurgle when the plug comes up."),
    ("cupboard", "Kitchen cupboard", "🗄️", "CUPBOARD", "I have doors but no house. I keep the plates and tins.", "I guard the tins and hide the jam, and Old Mother Hubbard found me bare."),
    ("crackers", "Box of crackers", "🎉", "CRACKERS", "Pull me and I go BANG! Inside there’s a hat and a joke.", "Two people pull, one wins the prize: a paper crown and a joke that’s not wise."),
    ("door", "Front door", "🚪", "DOOR", "Everyone comes in and out through me.", "I have a handle and a letterbox mouth, and Santa doesn’t need me."),
    ("bookshelf", "Bookshelf", "📚", "BOOKSHELF", "I’m full of stories but I can’t read.", "I hold many tales but tell none, with spines in rows, every one."),
    ("remote", "TV remote", "📺", "REMOTE", "Press my buttons to change the channel.", "I’m always lost down the sofa, and I control the Christmas film."),
    ("pillow", "Pillow", "😴", "PILLOW", "Rest your head on me at night.", "I’m soft and white and filled with fluff; I hold your dreams but not much stuff."),
    ("shoes", "Shoe rack", "👟", "SHOES", "You wear us on your feet.", "We have tongues but cannot talk, and we go everywhere you walk."),
    ("coats", "Coat hooks", "🧥", "COATS", "Hang me up when you come in from the cold.", "I’m worn in the snow and hung by the door, with pockets for gloves and maybe more."),
    ("oven", "Next to the oven (not inside!)", "🍗", "OVEN", "The turkey cooks inside me.", "I get hot on Christmas Day, but please don’t open me. Look beside me instead."),
    ("washing", "Washing machine", "🫧", "WASHING MACHINE", "I spin your clothes round and round.", "I eat dirty socks and give them back clean, but one always goes missing."),
]

THEMES = {
    "key": ("Santa’s Lost Sleigh Key", "Santa", "Santa has lost his sleigh key on Christmas Eve! Follow my clues to find it before midnight.", "You found the sleigh key! Christmas is saved."),
    "pudding": ("The Great Christmas Pudding Rescue", "Mischief the Elf", "I’ve hidden the Christmas pudding. Ha! Follow my clues if you want it back.", "Curses! You found the pudding. Merry Christmas!"),
    "bells": ("Rudolph’s Missing Bells", "Rudolph", "I’ve lost my jingle bells and I can’t fly without them! Please help me find them.", "Jingle jingle! You found my bells. Thank you!"),
    "presents": ("The Grinchy Elf’s Present Heist", "Grumble the Elf", "I’ve hidden the presents and I’m not giving them back… unless you can solve my clues.", "Fine. You win. The presents are yours."),
}

BUILDER_JS = r"""
<script>
(function(){
var PLACES=__PLACES__, THEMES=__THEMES__, A='ABCDEFGHIJKLMNOPQRSTUVWXYZ';
var TYPES={
  '3-5':['picture'],
  '6-8':['riddle','scramble','numbers','backwards'],
  '9-12':['riddle','scramble','numbers','caesar','pigpen','backwards'],
  'teen':['caesar','pigpen','numbers','vowels','backwards','riddle'],
  'adult':['caesar','pigpen','vowels','reverseAZ','numbers','riddle']
};
var NAMES={picture:'Picture clue',riddle:'Riddle',scramble:'Word scramble',numbers:'Number code (A=1)',backwards:'Backwards message',caesar:'Caesar shift',pigpen:'Pigpen cipher',vowels:'Missing vowels',reverseAZ:'Backwards alphabet code (Z=1)'};
var seed=1;
function rnd(){seed=(seed*16807)%2147483647;return (seed-1)/2147483646}
function pick(a){return a[Math.floor(rnd()*a.length)]}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function shuffleWord(w){var a=w.split(''),t=0;do{for(var i=a.length-1;i>0;i--){var j=Math.floor(rnd()*(i+1));var x=a[i];a[i]=a[j];a[j]=x}t++}while(a.join('')===w&&t<10);return a.join(' ')}
function pig(c,s){var i=A.indexOf(c);if(i<0)return '<span style="display:inline-block;width:'+(s/2)+'px"></span>';var m=4,e=s-4,h=s/2,L='',dot=false,st='stroke="#0c2a22" stroke-width="3" fill="none" stroke-linecap="round"';
 if(i<18){dot=i>=9;var k=i%9,r=Math.floor(k/3),col=k%3;if(r>0)L+='<line x1="'+m+'" y1="'+m+'" x2="'+e+'" y2="'+m+'" '+st+'/>';if(r<2)L+='<line x1="'+m+'" y1="'+e+'" x2="'+e+'" y2="'+e+'" '+st+'/>';if(col>0)L+='<line x1="'+m+'" y1="'+m+'" x2="'+m+'" y2="'+e+'" '+st+'/>';if(col<2)L+='<line x1="'+e+'" y1="'+m+'" x2="'+e+'" y2="'+e+'" '+st+'/>'}
 else{var k2=i-18;dot=k2>=4;var q=k2%4,P=[[[m,m],[h,e],[e,m]],[[m,m],[e,h],[m,e]],[[e,m],[m,h],[e,e]],[[m,e],[h,m],[e,e]]][q];L+='<polyline points="'+P.map(function(p){return p.join(',')}).join(' ')+'" '+st+'/>'}
 if(dot)L+='<circle cx="'+h+'" cy="'+h+'" r="3.2" fill="#b3263a"/>';return '<svg width="'+s+'" height="'+s+'" viewBox="0 0 '+s+' '+s+'" aria-hidden="true">'+L+'</svg>'}
function pigKey(){return '<div style="display:flex;flex-wrap:wrap;gap:6px;justify-content:center">'+A.split('').map(function(c){return '<div style="text-align:center;font-weight:700;font-size:.75rem">'+pig(c,26)+c+'</div>'}).join('')+'</div>'}
function azTable(rev){return '<table class="compare" style="font-size:.8rem"><tr>'+A.split('').map(function(c,i){return '<td>'+c+' '+(rev?26-i:i+1)+'</td>'+((i+1)%9===0?'</tr><tr>':'')}).join('')+'</tr></table>'}
function puzzle(type,place,age){
  var w=place.word, box=function(t){return '<div class="puzzle-box">'+t+'</div>'};
  if(type==='picture') return {i:'Look at the picture. Where should you look next?',h:'<div class="pic">'+place.emoji+'</div>'};
  if(type==='riddle') return {i:'Solve the riddle to find the next hiding place.',h:'<div class="poem">'+esc(age==='6-8'?place.easy:place.hard)+'</div>'};
  if(type==='scramble') return {i:'Unscramble the letters.',h:box(w.split(' ').map(shuffleWord).join(' &nbsp; '))};
  if(type==='numbers') return {i:'Each number is a letter: A = 1, B = 2, C = 3…',h:box(w.split(' ').map(function(x){return x.split('').map(function(c){return A.indexOf(c)+1}).join(' · ')}).join(' &nbsp;/&nbsp; '))+(age==='adult'||age==='teen'?'':azTable(false))};
  if(type==='reverseAZ') return {i:'Backwards alphabet: Z = 1, Y = 2 … A = 26.',h:box(w.split(' ').map(function(x){return x.split('').map(function(c){return 26-A.indexOf(c)}).join(' · ')}).join(' &nbsp;/&nbsp; '))};
  if(type==='backwards') return {i:'Read this message from right to left.',h:box(('LOOK BY THE '+w).split('').reverse().join(' ').replace(/   /g,' &nbsp; '))};
  if(type==='caesar'){var n=age==='9-12'?1+Math.floor(rnd()*2):2+Math.floor(rnd()*4);
    return {i:'Every letter has moved <strong>'+n+' place'+(n>1?'s':'')+' forward</strong> in the alphabet. Move each one back '+n+'.',h:box(w.split('').map(function(c){return c===' '?' &nbsp; ':A[(A.indexOf(c)+n)%26]+' '}).join(''))}}
  if(type==='pigpen') return {i:'Use the pigpen key to decode the symbols.',h:'<div style="display:flex;gap:6px;justify-content:center;flex-wrap:wrap;background:#fff;padding:12px;border-radius:12px;border:2px solid #e6dccb">'+w.split('').map(function(c){return pig(c,38)}).join('')+'</div>'+(age==='adult'?'':'<h4 style="margin:14px 0 6px">Key</h4>'+pigKey())};
  if(type==='vowels') return {i:'All the vowels have been stolen. What does it say?',h:box(('LOOK BY THE '+w).replace(/[AEIOU]/g,'').replace(/ +/g,' &nbsp; '))};
}
var form=document.getElementById('bform'), out=document.getElementById('bout');
function build(reseed){
  var age=form.age.value, th=THEMES[form.theme.value], from=form.from.value.trim()||th[1], kids=form.kids.value.trim();
  var chosen=[].slice.call(form.querySelectorAll('input[name=place]:checked')).map(function(c){return PLACES.filter(function(p){return p.key===c.value})[0]});
  var msg=document.getElementById('bmsg');
  if(chosen.length<3){msg.textContent='Pick at least 3 hiding places.';msg.className='msg bad';return}
  if(chosen.length>8){msg.textContent='Pick 8 hiding places or fewer.';msg.className='msg bad';return}
  msg.textContent='';if(reseed){seed=Math.floor(Math.random()*2147483646)+1}
  var types=TYPES[age], pool=[], cards='', rows='';
  var used=[];
  chosen.forEach(function(place,i){
    if(!pool.length) pool=types.slice().sort(function(){return rnd()-.5});
    var t=pool.pop(); used.push(t);
    var p=puzzle(t,place,age);
    var intro = i===0 ? '<p>'+(kids?'Dear '+esc(kids)+',':'Dear players,')+'</p><p>'+esc(th[2])+'</p><p>Here is your first clue:</p>' : '';
    var sign = i===0 ? '<p style="text-align:right">— <strong>'+esc(from)+'</strong></p>' : '';
    cards+='<article class="clue-card"><div class="num">'+(i===0?'Card 1 · Start here':'Card '+(i+1))+'</div><h3>'+esc(th[0])+'</h3>'+intro+'<p><em>'+p.i+'</em></p>'+p.h+sign+'</article>';
    rows+='<tr><td>Card '+(i+1)+'</td><td>'+(i===0?'Give to players':'Hide at: <strong>'+esc(chosen[i-1].label)+'</strong>')+'</td><td>'+NAMES[t]+'</td><td><strong>'+place.word+'</strong> → '+esc(place.label)+'</td></tr>';
  });
  var last=chosen[chosen.length-1];
  cards+='<article class="clue-card"><div class="num">Final card</div><h3>'+esc(th[0])+'</h3><div class="pic">🎉🎄🎁</div><p style="text-align:center;font-size:1.25rem">'+esc(th[3])+'</p><p style="text-align:right">— <strong>'+esc(from)+'</strong></p></article>';
  rows+='<tr><td>Final card</td><td>Hide at: <strong>'+esc(last.label)+'</strong> with the prize</td><td>–</td><td>Players win!</td></tr>';
  out.innerHTML='<div class="callout no-print"><strong>Your game is ready.</strong> '+chosen.length+' puzzles · about '+(chosen.length*(age==='3-5'?3:age==='6-8'?6:8))+' minutes to play. Print it, cut along the dashed lines and hide each card as the host sheet says.</div>'+
   '<section class="host-sheet"><h2>Host sheet <small style="font-size:.6em;color:#5d574d">(keep this; don’t give it to players)</small></h2><table class="compare"><thead><tr><th>Card</th><th>Where to put it</th><th>Puzzle</th><th>Answer → leads to</th></tr></thead><tbody>'+rows+'</tbody></table><p>Set-up tip: hide the cards in reverse order, starting with the final card and the prize.</p></section>'+
   '<h2 class="no-print">Clue cards</h2>'+cards;
  document.getElementById('bactions').hidden=false;
  try{out.scrollIntoView({behavior:'smooth',block:'start'})}catch(e){}
}
form.addEventListener('submit',function(e){e.preventDefault();build(true)});
document.getElementById('reshuffle').onclick=function(){build(true)};
form.age.addEventListener('change',function(){var y=this.value==='3-5';document.getElementById('agenote').hidden=!y});
})();
</script>"""


def build():
    import json
    path = "tools/escape-room-builder/"
    places = [{"key": k, "label": l, "emoji": e, "word": w, "easy": r1, "hard": r2} for k, l, e, w, r1, r2 in PLACES]
    default_on = {"tree", "stocking", "fridge", "sofa", "crackers"}
    checks = "".join(f'<label style="font-weight:400;display:flex;gap:8px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:10px;padding:8px 10px"><input type="checkbox" name="place" value="{k}"{" checked" if k in default_on else ""}> {e} {l}</label>' for k, l, e, w, r1, r2 in PLACES)
    theme_opts = "".join(f'<option value="{k}">{v[0]}</option>' for k, v in THEMES.items())
    js = BUILDER_JS.replace("__PLACES__", json.dumps(places, ensure_ascii=False)).replace("__THEMES__", json.dumps(THEMES, ensure_ascii=False))
    faq = [("How do I make my own Christmas escape room?", "Use the free escape room builder: choose the players’ age, a story and 3–8 hiding places in your home. It creates printable clue cards where each answer leads to the next hiding place, plus a host sheet with every answer."),
           ("What puzzles does the builder use?", "It picks puzzles that suit the age you choose: picture clues for ages 3–5; riddles, word scrambles, number codes and backwards messages for 6–8; plus Caesar shifts and pigpen ciphers for older children; and missing-vowel and backwards-alphabet codes for teens and adults."),
           ("Can I get different puzzles?", "Yes. Press ‘Shuffle puzzles’ to make a new version with the same hiding places, which is handy if you play more than once or run two teams."),
           ("Is it free?", "Yes, completely free with no sign-up. Print as many games as you like for home, school or work."),
           ("How long will the game take?", "Roughly 3 minutes per clue for ages 3–5, 6 minutes per clue for ages 6–8 and 8 minutes per clue for older players. Five hiding places makes a 30–40-minute game for most families.")]
    body = f"""
<div class="wrap narrow no-print">
<p class="eyebrow">Free tool</p>
<h1>Christmas escape room builder: make your own in 2 minutes</h1>
{byline()}
<p class="answer">The free Christmas escape room builder makes a custom printable escape room for your home. Choose the players’ age, a story and 3–8 hiding places (tree, stocking, fridge…). It creates a clue card for each one, with puzzles that suit the age, plus a host sheet with every answer. It takes about 2 minutes.</p>
</div>
<div class="wrap narrow">
<form id="bform" class="game no-print" autocomplete="off">
<div class="row">
<div class="field"><label for="age">Players’ age</label><select id="age" name="age"><option value="3-5">3–5 (picture clues)</option><option value="6-8" selected>6–8</option><option value="9-12">9–12</option><option value="teen">Teenagers</option><option value="adult">Adults</option></select></div>
<div class="field"><label for="theme">Story</label><select id="theme" name="theme">{theme_opts}</select></div>
</div>
<p id="agenote" class="callout" hidden>For ages 3–5, every clue is a big picture of the next hiding place. Read the cards aloud.</p>
<div class="row">
<div class="field"><label for="kids">Players’ names (optional)</label><input type="text" id="kids" name="kids" placeholder="e.g. Amelia and Jack"></div>
<div class="field"><label for="from">Letter signed by (optional)</label><input type="text" id="from" name="from" placeholder="e.g. Santa"></div>
</div>
<fieldset style="border:0;padding:0;margin:0 0 14px"><legend style="font-weight:600;margin-bottom:8px">Hiding places, in the order players will find them (pick 3–8)</legend>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:8px">{checks}</div>
<p style="font-size:.9rem;color:var(--muted);margin-top:8px">The last place you tick is where the prize goes. Cards follow the list order above.</p></fieldset>
<button class="btn" type="submit">Make my escape room</button>
<div class="msg" id="bmsg" aria-live="polite"></div>
</form>
<div class="btn-row no-print" id="bactions" hidden><button class="btn" data-print>Print the game</button><button class="btn ghost" id="reshuffle" type="button">Shuffle puzzles</button></div>
<p id="print-note" class="callout no-print" hidden>If nothing happened, press <strong>Ctrl + P</strong> or <strong>⌘ + P</strong>. The host sheet prints first, then one clue card per page.</p>
<div id="bout"></div>
<div class="no-print">
<h2>How the escape room builder works</h2>
<ol class="steps">
<li><strong>Choose the age.</strong> The builder only uses puzzles that suit it, from picture clues for toddlers to pigpen ciphers for adults.</li>
<li><strong>Pick a story and hiding places.</strong> Each clue’s answer is the next hiding place, so players move around your home.</li>
<li><strong>Print and hide.</strong> The host sheet tells you exactly where each card goes and every answer.</li>
<li><strong>Play.</strong> Hand over Card 1, start the <a href="{{R}}tools/escape-room-timer/index.html">timer</a>, and finish with a <a href="{{R}}tools/certificate-maker/index.html">certificate</a>.</li>
</ol>
<h2>Puzzles by age</h2>
<table class="compare"><thead><tr><th>Age</th><th>Puzzle types</th></tr></thead><tbody>
<tr><td>3–5</td><td>Picture clues</td></tr>
<tr><td>6–8</td><td>Riddles, word scrambles, A=1 number codes, backwards messages</td></tr>
<tr><td>9–12</td><td>Adds Caesar shifts (1–2 places) and pigpen cipher with key</td></tr>
<tr><td>Teenagers</td><td>Caesar shifts (2–5 places), pigpen, missing vowels, number codes</td></tr>
<tr><td>Adults</td><td>Pigpen without a key, backwards alphabet code, missing vowels, harder riddles</td></tr>
</tbody></table>
<p>Prefer a ready-made game? Try <a href="{{R}}printable/the-great-pudding-heist/index.html">The Great Pudding Heist</a> or browse all <a href="{{R}}printable/index.html">printable Christmas escape rooms</a>.</p>
{faq_html(faq)}
</div>
</div>
<style>@media print{{.host-sheet{{break-after:page;page-break-after:always}}}}</style>
{js}"""
    page(path, "Christmas Escape Room Builder – Make Your Own Free",
         "Make your own Christmas escape room in 2 minutes. Pick an age, story and hiding places, and get printable clue cards and a host answer sheet. Free, no sign-up.",
         body, crumbs=[("Tools", "tools/"), ("Escape room builder", path)],
         schema=[app_schema("Christmas Escape Room Builder", path, "Free generator for custom printable Christmas escape rooms."), faq_schema(faq)],
         active="Tools", og_image="assets/og/escape-room-builder.png")
