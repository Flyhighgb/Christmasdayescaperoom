from layout import page, faq_html, faq_schema, spec_table, DOMAIN


def app_schema(name, path, desc):
    return {"@type": "WebApplication", "name": name, "url": DOMAIN + "/" + path, "description": desc,
            "applicationCategory": "GameApplication", "operatingSystem": "Any (web browser)",
            "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "GBP"},
            "publisher": {"@id": DOMAIN + "/#org"}}


def build():
    # ================= CIPHER MAKER =================
    path = "tools/christmas-cipher-maker/"
    faq = [
        ("What is a pigpen cipher?", "A pigpen cipher swaps each letter for a shape taken from a noughts-and-crosses grid or an X, with or without a dot. It looks like secret symbols but is easy to decode with the key, which makes it ideal for children’s escape rooms."),
        ("What is a Caesar cipher?", "A Caesar cipher moves every letter a set number of places along the alphabet. With a shift of 3, A becomes D and CHIMNEY becomes FKLPQHB."),
        ("Which code is best for young children?", "The number code (A=1, B=2) is easiest for ages 5–7. Pigpen suits ages 7+, and a Caesar shift suits ages 9+."),
        ("Can I print the codes?", "Yes. Press ‘Print code and key’ to print the coded message together with a decoding key for the players."),
    ]
    tool_js = r"""
<script>
(function(){
var A='ABCDEFGHIJKLMNOPQRSTUVWXYZ';
var msg=document.getElementById('msg'), mode=document.getElementById('mode'), shift=document.getElementById('shift'), out=document.getElementById('out'), keyEl=document.getElementById('key'), sw=document.getElementById('shiftwrap');
function caesar(t,n){return t.toUpperCase().replace(/[A-Z]/g,function(c){return A[(A.indexOf(c)+n)%26]})}
function nums(t){return t.toUpperCase().split(/\s+/).filter(Boolean).map(function(w){return w.replace(/[^A-Z]/g,'').split('').map(function(c){return A.indexOf(c)+1}).join('-')}).join(' / ')}
function pig(c,size){
  var i=A.indexOf(c); if(i<0) return '';
  var s=size||34, m=4, e=s-m, h=s/2, L='', dot=false, st='stroke="#0c2a22" stroke-width="3" fill="none" stroke-linecap="round"';
  if(i<18){ dot=i>=9; var k=i%9, r=Math.floor(k/3), col=k%3;
    if(r>0) L+='<line x1="'+m+'" y1="'+m+'" x2="'+e+'" y2="'+m+'" '+st+'/>';
    if(r<2) L+='<line x1="'+m+'" y1="'+e+'" x2="'+e+'" y2="'+e+'" '+st+'/>';
    if(col>0) L+='<line x1="'+m+'" y1="'+m+'" x2="'+m+'" y2="'+e+'" '+st+'/>';
    if(col<2) L+='<line x1="'+e+'" y1="'+m+'" x2="'+e+'" y2="'+e+'" '+st+'/>';
  } else { var k2=i-18; dot=k2>=4; var q=k2%4, pts;
    if(q===0) pts=[[m,m],[h,e],[e,m]];        // S: V
    else if(q===1) pts=[[m,m],[e,h],[m,e]];   // T: >
    else if(q===2) pts=[[e,m],[m,h],[e,e]];   // U: <
    else pts=[[m,e],[h,m],[e,e]];             // V: ^
    L+='<polyline points="'+pts.map(function(p){return p.join(',')}).join(' ')+'" '+st+'/>';
  }
  if(dot) L+='<circle cx="'+h+'" cy="'+h+'" r="3.2" fill="#b3263a"/>';
  return '<svg width="'+s+'" height="'+s+'" viewBox="0 0 '+s+' '+s+'" role="img" aria-label="pigpen symbol">'+L+'</svg>';
}
function pigLine(t){return t.toUpperCase().split(/\s+/).filter(Boolean).map(function(w){return '<span style="display:inline-flex;gap:4px;margin:0 14px 10px 0">'+w.replace(/[^A-Z]/g,'').split('').map(function(c){return pig(c)}).join('')+'</span>'}).join('')}
function key(){
  var v=mode.value, n=+shift.value;
  if(v==='pigpen') return '<div style="display:flex;flex-wrap:wrap;gap:8px">'+A.split('').map(function(c){return '<div style="text-align:center;font-weight:600;font-size:.8rem">'+pig(c,30)+c+'</div>'}).join('')+'</div>';
  if(v==='numbers') return '<p>'+A.split('').map(function(c,i){return c+'='+(i+1)}).join(' · ')+'</p>';
  if(v==='caesar') return '<p>Move every letter <strong>back '+n+'</strong> place'+(n>1?'s':'')+' to decode. '+A.slice(0,5).split('').map(function(c){return caesar(c,n)+'→'+c}).join(', ')+'…</p>';
  return '<p>Read the message from right to left.</p>';
}
function render(){
  var t=msg.value||'', v=mode.value; sw.hidden=(v!=='caesar');
  var html, text='';
  if(v==='pigpen'){html='<div>'+pigLine(t)+'</div>'}
  else { if(v==='caesar') text=caesar(t,+shift.value); else if(v==='numbers') text=nums(t); else text=t.toUpperCase().split('').reverse().join('');
    html='<div class="puzzle-box" style="text-align:left">'+text.replace(/</g,'&lt;')+'</div>'; }
  out.innerHTML=html; out.dataset.text=text; keyEl.innerHTML=key();
  document.getElementById('copy').hidden=(v==='pigpen');
}
[msg,mode,shift].forEach(function(el){el.addEventListener('input',render)});
document.querySelectorAll('[data-phrase]').forEach(function(b){b.onclick=function(){msg.value=b.dataset.phrase;render()}});
document.getElementById('copy').onclick=function(){var b=this;try{navigator.clipboard.writeText(out.dataset.text).then(function(){b.textContent='Copied!';setTimeout(function(){b.textContent='Copy code'},1500)},function(){b.textContent='Select and copy the text above'})}catch(e){b.textContent='Select and copy the text above'}};
var s='';for(var i=1;i<26;i++){s+='<option value="'+i+'"'+(i===3?' selected':'')+'>'+i+'</option>'} shift.innerHTML=s;
render();
})();
</script>"""
    phrases = ["LOOK UNDER THE TREE", "CHECK YOUR STOCKING", "THE KEY IS IN THE FRIDGE", "MERRY CHRISTMAS", "SANTA IS COMING"]
    phrase_btns = "".join(f'<button type="button" class="btn ghost small" data-phrase="{p}">{p.title()}</button>' for p in phrases)
    body = f"""
<div class="wrap narrow">
<p class="eyebrow">Free tool</p>
<h1>Christmas cipher maker: pigpen, Caesar and number codes</h1>
<p class="answer">Type a message and this free tool turns it into a pigpen cipher, Caesar shift, A=1 number code or backwards message, with a decoding key to print for players. Ideal for making your own Christmas escape room clues.</p>
<div class="game no-print-border">
<div class="field"><label for="msg">Your secret message</label><textarea id="msg" rows="2">LOOK UNDER THE TREE</textarea></div>
<div class="btn-row" style="margin:0 0 14px">{phrase_btns}</div>
<div class="row">
<div class="field"><label for="mode">Code type</label><select id="mode"><option value="pigpen">Pigpen cipher (ages 7+)</option><option value="numbers">Number code A=1 (ages 5+)</option><option value="caesar">Caesar shift (ages 9+)</option><option value="reverse">Backwards message (ages 6+)</option></select></div>
<div class="field" id="shiftwrap"><label for="shift">Shift by</label><select id="shift"></select></div>
</div>
<h3>Coded message</h3>
<div id="out" aria-live="polite"></div>
<h3>Decoding key for players</h3>
<div id="key"></div>
<div class="btn-row no-print"><button class="btn" data-print>Print code and key</button><button class="btn ghost" id="copy">Copy code</button></div>
<p id="print-note" class="callout no-print" hidden>If nothing happened, press <strong>Ctrl + P</strong> or <strong>⌘ + P</strong> to print.</p>
</div>
<div class="no-print">
<h2>How to use codes in a Christmas escape room</h2>
<ol class="steps">
<li>Decide where the next clue is hidden, for example “under the tree”.</li>
<li>Type it above and choose a code that suits your players’ age.</li>
<li>Print the code. Hide the decoding key somewhere players must find first, or hand it over with the clue.</li>
</ol>
<p>Need the rest of the game? Read <a href="../../how-to/make-a-christmas-escape-room/index.html">how to make a Christmas escape room</a>, or use a ready-made <a href="../../printable/index.html">printable game</a>.</p>
{faq_html(faq)}
</div>
</div>
{tool_js}"""
    page(path, "Christmas Cipher Maker – Free Pigpen, Caesar & Number Code Generator",
         "Free Christmas cipher maker: turn any message into a pigpen cipher, Caesar shift or A=1 number code, with a printable key. Perfect for escape room clues.",
         body, crumbs=[("Tools", "tools/"), ("Christmas cipher maker", path)],
         schema=[app_schema("Christmas Cipher Maker", path, "Free pigpen, Caesar and number code generator for Christmas escape rooms."), faq_schema(faq)], active="Tools")

    # ================= TIMER =================
    path = "tools/escape-room-timer/"
    faq = [
        ("How long should a Christmas escape room timer be?", "Set 30 minutes for children under 8, 45 minutes for families and 60 minutes for teenagers and adults."),
        ("Can I show the timer on the TV?", "Yes. Open this page on a laptop connected to the TV, or cast your browser tab, then press Full screen."),
        ("How do hint penalties work?", "Each time a team uses a hint, press ‘Hint used’. You can choose to add a 2-minute penalty, which takes time off the clock."),
    ]
    timer_js = r"""
<script>
(function(){
var left=45*60, total=left, run=false, last=0, iv=null, hints=0;
var d=document.getElementById('tdisp'), st=document.getElementById('tstart'), hc=document.getElementById('hcount'), wrap=document.getElementById('tbox'), pen=document.getElementById('pen');
function fmt(s){s=Math.max(0,Math.ceil(s));return String(Math.floor(s/60)).padStart(2,'0')+':'+String(s%60).padStart(2,'0')}
function draw(){d.textContent=fmt(left); wrap.style.background= left<=60? 'var(--berry-2)':'var(--pine-2)'; document.title=fmt(left)+' · Escape Room Timer'}
function chime(){try{var c=new (window.AudioContext||window.webkitAudioContext)();[784,988,1175,1568].forEach(function(f,i){var o=c.createOscillator(),g=c.createGain();o.frequency.value=f;o.type='sine';o.connect(g);g.connect(c.destination);var t=c.currentTime+i*.22;g.gain.setValueAtTime(.0001,t);g.gain.exponentialRampToValueAtTime(.3,t+.02);g.gain.exponentialRampToValueAtTime(.0001,t+.6);o.start(t);o.stop(t+.65)})}catch(e){}}
function step(){var now=Date.now();left-=(now-last)/1000;last=now;if(left<=0){left=0;stop();d.textContent="TIME'S UP!";chime();return}draw()}
function start(){if(left<=0)return;run=true;last=Date.now();iv=setInterval(step,200);st.textContent='Pause'}
function stop(){run=false;clearInterval(iv);st.textContent='Start'}
st.onclick=function(){run?stop():start()};
document.getElementById('treset').onclick=function(){stop();left=total;hints=0;hc.textContent=0;draw()};
document.querySelectorAll('[data-min]').forEach(function(b){b.onclick=function(){stop();total=left=+b.dataset.min*60;draw()}});
document.getElementById('tcustom').onchange=function(){var v=+this.value;if(v>0&&v<=180){stop();total=left=v*60;draw()}};
document.getElementById('hint').onclick=function(){hints++;hc.textContent=hints;if(pen.checked){left=Math.max(0,left-120);draw()}};
document.getElementById('full').onclick=function(){try{var p=wrap.requestFullscreen?wrap.requestFullscreen():null;if(p&&p.catch)p.catch(function(){})}catch(e){}};
draw();
})();
</script>"""
    body = f"""
<div class="wrap narrow">
<p class="eyebrow">Free tool</p>
<h1>Christmas escape room timer</h1>
<p class="answer">A free countdown timer for escape rooms and party games. Pick 15, 30, 45 or 60 minutes, put it on the TV in full screen, track hints used, and hear a festive chime when time runs out.</p>
</div>
<div class="wrap">
<div id="tbox" style="background:var(--pine-2);color:#fff;border-radius:22px;padding:34px 20px;text-align:center;transition:background .4s">
<div id="tdisp" style="font:700 clamp(4rem,18vw,11rem)/1 ui-monospace,Menlo,Consolas,monospace;letter-spacing:.04em" aria-live="off">45:00</div>
<p style="color:#e9e1cf;margin:14px 0">Hints used: <strong id="hcount">0</strong></p>
<div class="btn-row" style="justify-content:center"><button class="btn gold" id="tstart">Start</button><button class="btn ghost" style="color:#fff" id="treset">Reset</button><button class="btn ghost" style="color:#fff" id="hint">Hint used</button><button class="btn ghost" style="color:#fff" id="full">Full screen</button></div>
</div>
<div class="row" style="margin-top:18px;align-items:end">
<div><label>Quick set</label><div class="btn-row" style="margin:0"><button class="btn ghost small" data-min="15">15 min</button><button class="btn ghost small" data-min="30">30 min</button><button class="btn ghost small" data-min="45">45 min</button><button class="btn ghost small" data-min="60">60 min</button></div></div>
<div class="field" style="margin:0"><label for="tcustom">Custom minutes</label><input id="tcustom" type="number" min="1" max="180" placeholder="e.g. 20"></div>
<div class="field" style="margin:0"><label style="font-weight:400"><input type="checkbox" id="pen"> Each hint costs 2 minutes</label></div>
</div>
</div>
<div class="wrap narrow">
<p style="margin-top:24px">Need a game to time? Try <a href="../../play-online/the-missing-sleigh-key/index.html">The Missing Sleigh Key</a> online or <a href="../../printable/the-great-pudding-heist/index.html">The Great Pudding Heist</a> printable.</p>
{faq_html(faq)}
</div>
{timer_js}"""
    page(path, "Escape Room Timer – Free Christmas Countdown Clock with Hints",
         "Free escape room countdown timer for Christmas party games. 15–60 minute presets, full screen for the TV, hint counter with penalties and a festive chime.",
         body, crumbs=[("Tools", "tools/"), ("Escape room timer", path)],
         schema=[app_schema("Christmas Escape Room Timer", path, "Free countdown timer with hint counter for escape room games."), faq_schema(faq)], active="Tools")

    # ================= CERTIFICATE =================
    path = "tools/certificate-maker/"
    faq = [
        ("Is the certificate free to print?", "Yes. Type the names and press Print. It prints on one A4 page in landscape."),
        ("Can I use it for any escape room game?", "Yes. Type your game’s name, or pick one of ours. It works for parties, classrooms and work events."),
    ]
    cert_js = r"""
<script>
(function(){
var f={names:document.getElementById('cn'),game:document.getElementById('cg'),time:document.getElementById('ct'),date:document.getElementById('cd')};
try{var l=JSON.parse(localStorage.getItem('cer-last')||'null');if(l){f.game.value=l.game;f.time.value=l.time}}catch(e){}
if(!f.date.value){f.date.value=new Date().toLocaleDateString('en-GB',{day:'numeric',month:'long',year:'numeric'})}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function draw(){
  document.getElementById('xn').innerHTML=esc(f.names.value||'Your names here');
  document.getElementById('xg').innerHTML=esc(f.game.value||'a Christmas escape room');
  document.getElementById('xt').innerHTML=f.time.value?'in a time of <strong>'+esc(f.time.value)+'</strong>':'';
  document.getElementById('xd').innerHTML=esc(f.date.value);
}
Object.keys(f).forEach(function(k){f[k].addEventListener('input',draw)}); draw();
})();
</script>"""
    extra = "<style>@media print{@page{size:A4 landscape;margin:10mm}.cert{border-width:10px!important;min-height:180mm}}</style>\n"
    body = f"""
<div class="wrap narrow no-print">
<p class="eyebrow">Free tool</p>
<h1>Christmas escape room certificate maker</h1>
<p class="answer">Make a free ‘You saved Christmas!’ certificate for your escape room winners. Add the team’s names, the game and their finishing time, then print it on A4.</p>
<div class="row">
<div class="field"><label for="cn">Names</label><input id="cn" type="text" placeholder="e.g. Amelia, Jack and Grandma"></div>
<div class="field"><label for="cg">Game</label><input id="cg" type="text" list="games" placeholder="e.g. The Missing Sleigh Key"><datalist id="games"><option value="The Missing Sleigh Key"><option value="The Great Pudding Heist"></datalist></div>
<div class="field"><label for="ct">Time (optional)</label><input id="ct" type="text" placeholder="e.g. 24:15"></div>
<div class="field"><label for="cd">Date</label><input id="cd" type="text"></div>
</div>
<div class="btn-row"><button class="btn" data-print>Print certificate</button></div>
<p id="print-note" class="callout" hidden>If nothing happened, press <strong>Ctrl + P</strong> or <strong>⌘ + P</strong> and choose landscape.</p>
<h2>Preview</h2>
</div>
<div class="wrap">
<div class="cert" style="background:#fffdf8;border:8px double var(--gold);border-radius:18px;padding:44px 30px;text-align:center;outline:2px solid var(--pine);outline-offset:-20px">
<div style="font-size:2.6rem">🎄🔑🎄</div>
<p class="eyebrow" style="margin-top:8px">Certificate of Christmas Rescue</p>
<h2 style="font-size:clamp(2rem,6vw,3.4rem);margin:.2em 0;color:var(--berry)">You saved Christmas!</h2>
<p style="font-size:1.1rem">This is to certify that</p>
<p id="xn" style="font-family:var(--serif);font-size:clamp(1.6rem,4vw,2.4rem);color:var(--pine-2);font-weight:700;margin:.2em 0"></p>
<p style="font-size:1.1rem">escaped <strong id="xg"></strong> <span id="xt"></span></p>
<p style="color:var(--muted)"><span id="xd"></span> · Signed, Santa Claus 🎅</p>
<p style="font-size:.8rem;color:var(--muted);margin:16px 0 0">christmasescaperoom.co.uk</p>
</div>
</div>
<div class="wrap narrow no-print">{faq_html(faq)}</div>
{cert_js}"""
    page(path, "Free Christmas Escape Room Certificate Maker – ‘You Saved Christmas!’",
         "Make and print a free ‘You saved Christmas!’ certificate for your escape room winners. Add names, game and finishing time. A4 landscape.",
         body, crumbs=[("Tools", "tools/"), ("Certificate maker", path)],
         schema=[app_schema("Christmas Escape Room Certificate Maker", path, "Free printable certificate for escape room winners."), faq_schema(faq)], active="Tools", extra_head=extra)
