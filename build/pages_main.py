from layout import byline, page, faq_html, faq_schema, spec_table, article_schema, DOMAIN

GAMES = [
    {"name": "The Missing Sleigh Key", "path": "play-online/the-missing-sleigh-key/", "format": "Play online", "icon": "🔑", "for": "Families",
     "ages": "8+", "players": "1–6", "time": "20–30 min", "prep": "None",
     "blurb": "Santa has lost his sleigh key on Christmas Eve. Crack five festive locks in your browser. Works on phones and over Zoom."},
    {"name": "The Office Party Escape", "path": "play-online/office-party-escape/", "format": "Play online", "icon": "🥧", "for": "Work teams",
     "ages": "Adults", "players": "Teams of 2–6", "time": "20–30 min", "prep": "None",
     "blurb": "A free online team game for office Christmas parties and remote teams. No host, no booking: just send the link."},
    {"name": "The Great Pudding Heist", "path": "printable/the-great-pudding-heist/", "format": "Printable", "icon": "🍮", "for": "Families",
     "ages": "6+", "players": "2–8", "time": "30–45 min", "prep": "10 min",
     "blurb": "Mischief the elf has hidden the Christmas pudding. Hide five clue cards round the house and race to find it."},
    {"name": "Scrooge’s Safe", "path": "printable/scrooges-safe/", "format": "Printable", "icon": "🗝️", "for": "Adults",
     "ages": "14+", "players": "2–6", "time": "45–60 min", "prep": "15 min",
     "blurb": "A properly tricky game for adults: pigpen cipher, mirror writing and a Christmas Carol logic lock."},
    {"name": "Elf Academy Final Exam", "path": "printable/elf-academy-final-exam/", "format": "Printable", "icon": "🎓", "for": "Teenagers",
     "ages": "11–16", "players": "2–6", "time": "30–45 min", "prep": "10 min",
     "blurb": "Old-phone texting, Morse code and a Twelve Days maths lock. Built for teens who think they’re too old for kids’ games."},
    {"name": "Rudolph’s Lost Bells", "path": "printable/rudolphs-lost-bells/", "format": "Printable", "icon": "🔔", "for": "Ages 3–5",
     "ages": "3–5", "players": "1–4", "time": "15–20 min", "prep": "5 min",
     "blurb": "A picture-only escape room for toddlers and preschoolers. No reading needed: match, count and find the bells."},
    {"name": "Christmas Memory Lane", "path": "printable/christmas-memory-lane/", "format": "Printable", "icon": "☕", "for": "Care homes",
     "ages": "Older adults", "players": "3–10 seated", "time": "20–30 min", "prep": "5 min",
     "blurb": "A seated, large-print escape room for care homes and older relatives, full of gentle Christmas memories."},
    {"name": "Escape Room Advent Calendar", "path": "printable/advent-calendar/", "format": "Printable", "icon": "📅", "for": "Advent",
     "ages": "5–9", "players": "1–4", "time": "2 min a day", "prep": "Print",
     "blurb": "One tiny puzzle a day from 1–24 December. The letters spell a secret message by Christmas Eve."},
]


def game_cards(r):
    out = []
    for g in GAMES:
        out.append(f'<a class="card" href="{r}{g["path"]}index.html"><span class="icon" aria-hidden="true">{g["icon"]}</span>'
                   f'<h3>{g["name"]}</h3><p>{g["blurb"]}</p><div class="tags"><span class="tag {"green" if g["format"]=="Play online" else "red"}">{g["format"]}</span>'
                   f'<span class="tag">Ages {g["ages"]}</span><span class="tag">{g["players"]} players</span><span class="tag">{g["time"]}</span></div></a>')
    return "".join(out)


def compare_table(r):
    rows = "".join(f'<tr><td><a href="{r}{g["path"]}index.html">{g["name"]}</a></td><td>{g["for"]}</td><td>{g["format"]}</td><td>{g["ages"]}</td><td>{g["players"]}</td><td>{g["time"]}</td><td>{g["prep"]}</td></tr>' for g in GAMES)
    return ('<table class="compare"><thead><tr><th>Game</th><th>Best for</th><th>Format</th><th>Ages</th><th>Players</th><th>Time</th><th>Prep</th></tr></thead>'
            f'<tbody>{rows}</tbody></table>')


TOOLS = [
    ("🔐", "Christmas cipher maker", "tools/christmas-cipher-maker/", "Turn any message into a pigpen, Caesar or number code. Print it or copy it into your own clues."),
    ("⏱️", "Escape room timer", "tools/escape-room-timer/", "A big countdown clock for the TV or laptop, with a hint counter and a chime when time runs out."),
    ("🏅", "Certificate maker", "tools/certificate-maker/", "Make a ‘You saved Christmas!’ certificate with your team’s names and finishing time."),
]


def tool_cards(r):
    return "".join(f'<a class="card" href="{r}{p}index.html"><span class="icon" aria-hidden="true">{i}</span><h3>{n}</h3><p>{d}</p><div class="tags"><span class="tag green">Free tool</span></div></a>' for i, n, p, d in TOOLS)


def build():
    # ---------- HOME ----------
    home_faq = [
        ("What is a Christmas escape room?", "A Christmas escape room is a festive puzzle game where players solve a chain of clues, codes and riddles against the clock to complete a mission, such as finding Santa’s lost key. At home you play with printed clue cards or online in a browser, with no real locked room."),
        ("Are the games on this site free?", "Yes. Every game, printable and tool on christmasescaperoom.co.uk is free to play at home, in school or at work. There is no sign-up and no email needed to download."),
        ("How long does a Christmas escape room take?", "Most of our games take 20–45 minutes. The online games take 20–30 minutes, family printables 30–45 minutes, the adults’ game Scrooge’s Safe 45–60 minutes, and the toddler game 15–20 minutes."),
        ("What age is a Christmas escape room for?", "We have games for every age: Rudolph’s Lost Bells for ages 3–5, The Great Pudding Heist for 6+, Elf Academy Final Exam for 11–16, Scrooge’s Safe for adults, and Christmas Memory Lane for older adults in care homes."),
        ("Can I play a Christmas escape room without a printer?", "Yes. The Missing Sleigh Key is played entirely online on a phone, tablet or laptop, so you don’t need a printer, props or a download."),
    ]
    body = f"""
<section class="hero"><div class="snow"></div><div class="wrap">
<p class="eyebrow">Free · No sign-up · Made in the UK</p>
<h1>Free Christmas escape rooms to play online or print at home</h1>
<p class="lead">Festive puzzle games for families, classrooms, care homes and office parties. Play in your browser in seconds, or print the clue cards and hide them round the house.</p>
<div class="btn-row"><a class="btn gold" href="play-online/the-missing-sleigh-key/index.html">Play online now</a><a class="btn ghost" href="printable/index.html">Get a printable game</a></div>
</div></section>

<div class="wrap">
<section><h2>Pick a game</h2>
<p>Every game below is free, has a full answer key and works without buying any props.</p>
<div class="grid">{game_cards('')}</div>
</section>

<section><h2>Find a game for…</h2>
<div class="grid aud-grid">
<a class="card" href="printable/rudolphs-lost-bells/index.html"><h3>Toddlers &amp; preschoolers</h3><p>Picture clues, no reading. Ages 3–5.</p></a>
<a class="card" href="printable/the-great-pudding-heist/index.html"><h3>Kids &amp; families</h3><p>Hide clues round the house. Ages 6+.</p></a>
<a class="card" href="printable/elf-academy-final-exam/index.html"><h3>Teenagers</h3><p>Morse, phone codes and maths. Ages 11–16.</p></a>
<a class="card" href="printable/scrooges-safe/index.html"><h3>Adults</h3><p>A hard Christmas Carol puzzle hunt.</p></a>
<a class="card" href="play-online/office-party-escape/index.html"><h3>Office parties</h3><p>Free online team game, no host.</p></a>
<a class="card" href="printable/christmas-memory-lane/index.html"><h3>Care homes</h3><p>Seated, large print, gentle.</p></a>
<a class="card" href="play-online/the-missing-sleigh-key/index.html"><h3>Zoom &amp; far-away family</h3><p>Play together online on any device.</p></a>
<a class="card" href="printable/advent-calendar/index.html"><h3>Advent</h3><p>A puzzle a day, 1–24 December.</p></a>
</div></section>

<section><h2>Compare the games</h2>{compare_table('')}</section>

<section><h2>Free tools to build your own escape room</h2>
<p>Making your own game? These tools do the fiddly parts for you.</p>
<div class="grid">{tool_cards('')}</div>
</section>

<section class="narrow"><h2>How a home escape room works</h2>
<ol class="steps">
<li><strong>Choose a game</strong> to suit your group’s age and how much time you have.</li>
<li><strong>Play online</strong> straight away, or <strong>print and hide</strong> the clue cards (about 10 minutes).</li>
<li><strong>Start the timer</strong> and read the story out loud.</li>
<li><strong>Solve each clue</strong>. Every answer points to the next hiding place.</li>
<li><strong>Crack the final code</strong> to save Christmas, then print your certificate.</li>
</ol>
<p>Want to make your own? Read <a href="how-to/make-a-christmas-escape-room/index.html">how to make a Christmas escape room at home</a>.</p>
</section>

<div class="narrow">{faq_html(home_faq)}</div>
</div>
"""
    page("", "Free Christmas Escape Rooms – Play Online or Print at Home | Christmas Escape Room",
         "Free Christmas escape room games for kids, families, adults and office parties. Play online with no download, or print clue cards. Plus free cipher, timer and certificate tools.",
         body, schema=[faq_schema(home_faq)])

    # ---------- PLAY ONLINE HUB ----------
    online = [g for g in GAMES if g["format"] == "Play online"]
    hub_faq = [
        ("Do I need to download anything to play?", "No. Our online Christmas escape rooms run in any modern web browser on a phone, tablet or computer. There’s nothing to install and no account to make."),
        ("Can we play together over Zoom or FaceTime?", "Yes. One person shares their screen and everyone shouts out answers, or each household opens the same game and races to finish first."),
        ("Can I use it at an office Christmas party?", "Yes. Split into teams of 2–6, give each team the link and compare finishing times. It takes about 20–30 minutes and costs nothing."),
    ]
    cards = "".join(f'<a class="card" href="../{g["path"]}index.html"><span class="icon">{g["icon"]}</span><h3>{g["name"]}</h3><p>{g["blurb"]}</p><div class="tags"><span class="tag">Ages {g["ages"]}</span><span class="tag">{g["time"]}</span></div></a>' for g in online)
    body = f"""
<div class="wrap narrow">
<p class="eyebrow">Play online</p>
<h1>Free online Christmas escape room – no download</h1>
<p class="answer">Play a free Christmas escape room in your browser right now. It needs no download, sign-up or printer, works on phones, and takes 20–30 minutes for 1–6 players aged 8 and up.</p>
<h2>Online games</h2>
<div class="grid">{cards}</div>
<h2>Playing with family far away or at work</h2>
<p>Share your screen on a video call and solve the clues together, or send the link to each household and compare times. For a work party, split into teams of 2–6 and use our <a href="../tools/escape-room-timer/index.html">escape room timer</a> on the big screen.</p>
<p>Prefer paper and hiding clues around the house? Try our <a href="../printable/index.html">printable Christmas escape rooms</a>.</p>
{faq_html(hub_faq)}
</div>"""
    page("play-online/", "Free Online Christmas Escape Room – No Download | Christmas Escape Room",
         "Play a free Christmas escape room online with no download or sign-up. Works on phones, great over Zoom and for office parties. 20–30 minutes, ages 8+.",
         body, crumbs=[("Play online", "play-online/")], schema=[faq_schema(hub_faq)], active="Play online")

    # ---------- PRINTABLE HUB ----------
    printable = [g for g in GAMES if g["format"] == "Printable"]
    pfaq = [
        ("What do I need for a printable Christmas escape room?", "A printer, A4 paper, scissors and a few hiding places around the house. Our printables don’t need padlocks or special props."),
        ("Can adults play a printable Christmas escape room?", "Yes. Adults can play the standard version against the clock, or use the ‘make it harder’ tips on each game page to add a time limit and remove hints."),
        ("Is there an answer key?", "Yes. Every printable has a full answer key on its own page so the host can help if players get stuck."),
    ]
    cards = "".join(f'<a class="card" href="../{g["path"]}index.html"><span class="icon">{g["icon"]}</span><h3>{g["name"]}</h3><p>{g["blurb"]}</p><div class="tags"><span class="tag">Ages {g["ages"]}</span><span class="tag">{g["players"]} players</span><span class="tag">{g["time"]}</span></div></a>' for g in printable)
    body = f"""
<div class="wrap narrow">
<p class="eyebrow">Printable</p>
<h1>Free printable Christmas escape rooms</h1>
<p class="answer">Print five clue cards, hide them around your home and let players follow the trail. Our printable Christmas escape rooms are free, need no padlocks or props, take about 10 minutes to set up and 30–45 minutes to play.</p>
<h2>Printable games</h2>
<div class="grid">{cards}</div>
<h2>Tips for hosting</h2>
<ul>
<li>Print on card if you can. Clue cards survive little hands better.</li>
<li>Put the <a href="../tools/escape-room-timer/index.html">timer</a> on the TV for atmosphere.</li>
<li>Give each team three hint tokens; spending one costs two minutes.</li>
<li>Finish with a <a href="../tools/certificate-maker/index.html">printable certificate</a>.</li>
</ul>
{faq_html(pfaq)}
</div>"""
    page("printable/", "Free Printable Christmas Escape Room Games | Christmas Escape Room",
         "Free printable Christmas escape room games for kids, families and adults. Print the clue cards, hide them round the house and save Christmas. Answer key included.",
         body, crumbs=[("Printable", "printable/")], schema=[faq_schema(pfaq)], active="Printable")

    # ---------- TOOLS HUB ----------
    body = f"""
<div class="wrap narrow">
<p class="eyebrow">Tools</p>
<h1>Free Christmas escape room tools</h1>
<p class="answer">Three free tools for anyone making or hosting a Christmas escape room: a cipher maker for secret codes, a big-screen countdown timer, and a certificate maker for the winners.</p>
</div>
<div class="wrap"><div class="grid">{tool_cards('../')}</div></div>"""
    page("tools/", "Free Christmas Escape Room Tools – Cipher Maker, Timer, Certificates",
         "Free tools for making a Christmas escape room: pigpen and Caesar cipher maker, countdown timer with hints, and a printable certificate maker.",
         body, crumbs=[("Tools", "tools/")], active="Tools")

    # ---------- ABOUT ----------
    body = """
<div class="wrap narrow">
<h1>About Christmas Escape Room</h1>
{BYL}
<p class="answer">Christmas Escape Room (christmasescaperoom.co.uk) is a free UK website of Christmas escape room games you can play online or print at home, plus tools for making your own.</p>
<h2>Who makes the games</h2>
<p>I’m <strong>Paul</strong>, the creator of Christmas Escape Room. I write and test every puzzle on the site, from the picture clues for toddlers to the Christmas Carol cipher hunt for adults, and I keep the games free so any family, school, care home or office can use them.</p>
<h2>Why I made it</h2>
<p>Most Christmas escape rooms online are paid downloads or classroom packs. I wanted a place where any family, teacher, care home or office could find a good festive puzzle game in seconds, for free, with no sign-up.</p>
<h2>How the games are made</h2>
<ul>
<li>Every game has a full answer key and a hint for each clue.</li>
<li>Each game page lists the age range, player count, play time and prep time, so you can choose quickly.</li>
<li>We use UK spelling and British Christmas traditions: crackers, mince pies, Boxing Day.</li>
<li>No game needs padlocks or props you’d have to buy.</li>
</ul>
<h2>Using our games</h2>
<p>You’re welcome to use any game at home, in school, in a care home or at a work party. Please link to the page rather than re-uploading the files elsewhere.</p>
<h2>Contact</h2>
<p>Ideas for a new game, or spotted a mistake? Email Paul at <a href="mailto:hello@christmasescaperoom.co.uk">hello@christmasescaperoom.co.uk</a>.</p>
</div>"""
    body = body.replace("{BYL}", byline())
    page("about/", "About Christmas Escape Room | Free UK Christmas Puzzle Games",
         "Christmas Escape Room is a free UK website of Christmas escape room games to play online or print at home, plus tools for making your own.",
         body, crumbs=[("About", "about/")], schema=[{"@type": "AboutPage", "url": DOMAIN + "/about/", "about": {"@id": DOMAIN + "/#org"}, "mainEntity": {"@id": DOMAIN + "/about/#paul"}}], active="About")

    # ---------- HOW TO ----------
    howto_faq = [
        ("How long does it take to make a Christmas escape room?", "About 1–2 hours to plan and write five puzzles, and 10–15 minutes to hide the clues on the day. Using a ready-made printable cuts this to 10 minutes."),
        ("How many puzzles should a home escape room have?", "Five to seven puzzles suits most families and fills 30–60 minutes. Use four for children under 7 and up to ten for experienced adult teams."),
        ("Do I need padlocks for a home escape room?", "No. Each answer can simply name the next hiding place. If you want locks, a cheap 3- or 4-digit combination padlock on a box or bag adds drama."),
        ("What are good hiding places for Christmas escape room clues?", "Inside a stocking, under the Christmas tree, in a cracker box, under a sofa cushion, in the fridge door, inside a book or behind a picture frame."),
        ("How do I stop players getting stuck?", "Give each team three hint tokens, keep an answer sheet, and test every puzzle on one person before the game."),
    ]
    howto_steps = [
        ("Pick a story and a goal", "Choose a simple Christmas mission, such as ‘find Santa’s lost key before midnight’ or ‘rescue the stolen pudding’. The goal tells players what the final answer is."),
        ("Work backwards from the ending", "Decide where the final prize is hidden, then where the clue before it is hidden, and so on. Each answer should name the next hiding place."),
        ("Choose five to seven puzzle types", "Mix them up: a riddle, a word scramble, a number code (A=1), a backwards message, a cipher, a maths lock and a picture search."),
        ("Make the clues", "Write each clue on a card. Use our Christmas cipher maker for pigpen and Caesar codes, and print a copy of the answers for yourself."),
        ("Test it on one person", "Ask someone who isn’t playing to solve each card. If it takes longer than 10 minutes, make it easier or add a hint."),
        ("Hide the clues and set the scene", "Hide the cards in order, dim the lights, put on Christmas music and start a countdown timer on the TV."),
        ("Run the game", "Read the story aloud, hand over the first card and start the clock. Give a hint when a team is stuck for 3–5 minutes."),
        ("Celebrate the finish", "Reveal the prize, announce the time and hand out certificates."),
    ]
    steps_html = "".join(f"<li><strong>{t}.</strong> {d}</li>" for t, d in howto_steps)
    howto_schema = {"@type": "HowTo", "name": "How to make a Christmas escape room at home", "totalTime": "PT2H",
                    "supply": [{"@type": "HowToSupply", "name": n} for n in ["Paper or card", "Pen", "Envelopes", "Small prize"]],
                    "step": [{"@type": "HowToStep", "position": i + 1, "name": t, "text": d} for i, (t, d) in enumerate(howto_steps)]}
    path = "how-to/make-a-christmas-escape-room/"
    body = f"""
<div class="wrap narrow">
<p class="eyebrow">How to</p>
<h1>How to make a Christmas escape room at home</h1>
{byline()}
<p class="answer">To make a Christmas escape room at home, pick a festive mission, work backwards from where the prize is hidden, and write 5–7 clues whose answers each name the next hiding place. It takes 1–2 hours to plan and about 10 minutes to hide the clues.</p>
{spec_table([("Time to make", "1–2 hours"), ("Set-up on the day", "10–15 minutes"), ("Play time", "30–60 minutes"), ("Puzzles", "5–7 (4 for under-7s)"), ("You need", "Paper or card, a pen, envelopes, a small prize. Padlocks optional.")])}
<h2>Step by step</h2>
<ol class="steps">{steps_html}</ol>
<div class="callout">Short on time? Our <a href="../../printable/the-great-pudding-heist/index.html">Great Pudding Heist printable</a> is ready to print and hide in 10 minutes.</div>

<h2>Christmas escape room puzzle ideas</h2>
<ol>
<li><strong>Riddle:</strong> “I have needles but never sew” → the Christmas tree.</li>
<li><strong>Word scramble:</strong> GNIKCOTS → STOCKING.</li>
<li><strong>Number code (A=1, B=2):</strong> 19-15-6-1 → SOFA.</li>
<li><strong>Caesar shift:</strong> move each letter back three: FKLPQHB → CHIMNEY.</li>
<li><strong>Pigpen cipher:</strong> make one with our <a href="../../tools/christmas-cipher-maker/index.html">cipher maker</a>.</li>
<li><strong>Backwards message:</strong> DRAOBPUC → CUPBOARD.</li>
<li><strong>Acrostic poem:</strong> the first letter of each line spells the answer.</li>
<li><strong>Maths lock:</strong> reindeer (9) × days of Christmas (12) + Christmas Day (25) = 133.</li>
<li><strong>Count the baubles:</strong> the number of red baubles on the tree is the code.</li>
<li><strong>Cracker joke:</strong> the punchline’s first letters spell the next place.</li>
</ol>

<h2>Where to hide clues at Christmas</h2>
<table class="compare"><thead><tr><th>Hiding place</th><th>Clue that points to it</th></tr></thead><tbody>
<tr><td>Christmas tree</td><td>“I have needles but never sew.”</td></tr>
<tr><td>Stocking</td><td>Word scramble: GNIKCOTS</td></tr>
<tr><td>Fridge</td><td>“I’m cold inside and hum all day.”</td></tr>
<tr><td>Sofa cushion</td><td>Number code: 19-15-6-1</td></tr>
<tr><td>Box of crackers</td><td>Shifted code: DSBDLFST</td></tr>
<tr><td>Kitchen cupboard</td><td>Backwards: DRAOBPUC</td></tr>
</tbody></table>

<h2>Make it easier or harder</h2>
<ul>
<li><strong>Ages 4–6:</strong> use picture clues, read every card aloud and hide clues in plain sight.</li>
<li><strong>Teenagers and adults:</strong> add a 30-minute limit, a red herring or two, and a combination padlock on the final box.</li>
<li><strong>Big groups:</strong> make two copies of every clue and run two teams side by side.</li>
</ul>
{faq_html(howto_faq)}
</div>"""
    page(path, "How to Make a Christmas Escape Room at Home (Step by Step) | Christmas Escape Room",
         "How to make a Christmas escape room at home in 8 steps, with 10 puzzle ideas, clue hiding places and tips for kids, teens and adults. Free tools included.",
         body, crumbs=[("How to make a Christmas escape room", path)],
         schema=[article_schema(path, "How to make a Christmas escape room at home", "Step-by-step guide with puzzle ideas and hiding places."), howto_schema, faq_schema(howto_faq)],
         active="How to")
