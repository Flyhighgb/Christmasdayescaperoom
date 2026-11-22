"""Occasion pages: Christmas Eve, Boxing Day, New Year's Eve, 10-minute, no printer, KS2 classroom."""
from games_lib import printable_game, online_game, pig_word, pig_key, ALPHA
from pages_games import shift, spaced, AZ_TABLE
from layout import page, faq_html, faq_schema, spec_table, DOMAIN, byline, PERSON_ID, article_schema


def roman(n):
    vals = [(10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    out = ""
    for v, s in vals:
        while n >= v:
            out += s; n -= v
    return out


def build():
    # ============================================================ CHRISTMAS EVE
    printable_game(
        slug="christmas-eve", name="The Night Before Christmas Mission",
        h1="Christmas Eve escape room: a printable bedtime game for families",
        title="Christmas Eve Escape Room – Free Printable Family Game",
        description="A free printable Christmas Eve escape room that ends at bedtime. Ages 5–10, 20–30 minutes, 5 clue cards, the last one hidden under the pillow. Answers included.",
        answer="The Night Before Christmas Mission is a free printable Christmas Eve escape room for ages 5–10. Children help Santa get the house ready (pyjamas, Rudolph’s carrot, Santa’s mince pie) and the final clue is hidden under their pillow, so the game ends at bedtime. It takes 20–30 minutes.",
        spec=[("Ages", "5–10"), ("Players", "1–6"), ("Time", "20–30 minutes"), ("Set-up", "10 minutes"), ("Difficulty", "Easy"), ("Best time", "Christmas Eve, before bed"), ("You need", "Printer, 6 sheets of A4, a carrot, a mince pie, a small Christmas Eve gift (optional)"), ("Puzzles", "4 + final card")],
        story="Santa has sent a letter: before he can visit, the children must complete four Christmas Eve jobs. Each job leads to the next clue: into their pyjamas, out with Rudolph’s carrot, a mince pie for Santa, and finally into bed, where Santa’s ‘Nice List’ certificate is waiting under the pillow.",
        cards=[
            {"title": "A letter from Santa", "intro": "Read this aloud to start.", "type": "an A=1 number code inside Santa’s letter.",
             "html": '<p>Ho ho ho! It’s Christmas Eve and I’m nearly ready to fly. Before I can visit your house, you need to finish my <strong>Christmas Eve mission</strong>.</p><p>Your first job: get ready for bed! Crack my code to find your next clue.</p><div class="puzzle-box">16 · 25 · 10 · 1 · 13 · 1 · 19</div>' + AZ_TABLE + '<p style="text-align:right">Love, <strong>Santa</strong></p>',
             "hide": "Hand to the children to start.", "answer": "PYJAMAS", "explain": "P16 Y25 J10 A1 M13 A1 S19. Card 2 is with their pyjamas."},
            {"title": "Rudolph is hungry", "intro": "Rudolph has lost some letters. Fill in the gaps.", "type": "a missing-letters puzzle.",
             "html": '<div class="puzzle-box">C _ R R _ T</div><p>Find one in the kitchen and put it out for Rudolph. Your next clue is hiding next to it!</p>',
             "hide": "Folded inside or under their pyjamas.", "answer": "CARROT", "explain": "C A R R O T. Card 3 is in the fridge or veg drawer with the carrots."},
            {"title": "Santa’s favourite snack", "intro": "Santa wrote this back to front. Read it from right to left.", "type": "a backwards message.",
             "html": '<div class="puzzle-box">E I P &nbsp; E C N I M</div><p>Put one on a plate by the tree for Santa, and look for your next clue where they’re kept.</p>',
             "hide": "In the fridge or vegetable drawer, next to the carrots.", "answer": "MINCE PIE", "explain": "Read right to left. Card 4 is in the mince pie box or tin."},
            {"title": "Santa’s bedtime poem", "intro": "The first letter of each line spells where your last clue is.", "type": "an acrostic poem.",
             "html": '<div class="poem">Presents wait beneath the tree,<br>In the sky a sleigh flies free,<br>Lights are twinkling soft and low,<br>Little feet must sleep, you know.<br>Off to bed and dream tonight,<br>Wake up early, Christmas bright!</div>',
             "hide": "In the mince pie box or tin.", "answer": "PILLOW", "explain": "First letters: P-I-L-L-O-W. The final card is under their pillow."},
        ],
        finale={"title": "Mission complete!", "html": '<div class="pic">🎅⭐🛏️</div><p class="big-print" style="text-align:center">You did it! You’re officially on my <strong>Nice List</strong>.<br>Now close your eyes and go to sleep. I can’t come until you do!<br><strong>Santa</strong></p>',
                "hide": "Under the children’s pillow (with a small Christmas Eve gift, if you like).", "setup": "Put the final card, and a small Christmas Eve gift if you like, under the children’s pillow."},
        faq=[("What can we do on Christmas Eve with kids?", "A Christmas Eve escape room is a fun way to calm the excitement: The Night Before Christmas Mission takes 20–30 minutes and leads children through putting on pyjamas, leaving out Rudolph’s carrot and Santa’s mince pie, and ends with the last clue under their pillow."),
             ("What age is it for?", "Ages 5–10. Children aged 5–6 may need help with the number code; older children can play on their own."),
             ("When should we play it?", "About an hour before bed on Christmas Eve, so it ends with everyone in pyjamas and ready to sleep."),
             ("Can I use it with a Christmas Eve box?", "Yes. Put the Christmas Eve box under the pillow with the final card for a lovely finish.")],
        ages_min=5, players=(1, 6), minutes=30,
        easier="read each card aloud and help with the number code using the A–Z table.",
        harder="cover the A–Z table, and hide each card more carefully.",
        related=[("Escape room advent calendar", "printable/advent-calendar/", "for the run-up to Christmas"), ("The Great Pudding Heist", "printable/the-great-pudding-heist/", "for Christmas Day"), ("Boxing Day escape room", "printable/boxing-day/", "")],
        audience="Christmas Eve")

    # ============================================================ BOXING DAY
    printable_game(
        slug="boxing-day", name="The Leftovers Lockdown",
        h1="Boxing Day escape room: a printable game for the whole family",
        title="Boxing Day Escape Room – Free Printable Family Game",
        description="A free printable Boxing Day escape room for families with older kids and adults. Leftovers, board games, a Boxing Day walk and a sales maths lock. Ages 8+, 30–45 minutes.",
        answer="The Leftovers Lockdown is a free printable Boxing Day escape room for ages 8 to adult. Grandad has locked the chocolate tin; players crack a riddle, a Caesar code, a pigpen cipher and a Boxing Day sales maths lock to get it back. It takes 30–45 minutes for 2–8 players.",
        spec=[("Ages", "8+ and adults"), ("Players", "2–8"), ("Time", "30–45 minutes"), ("Set-up", "10 minutes"), ("Difficulty", "Medium"), ("You need", "Printer, 6 sheets of A4, a tin or box of chocolates, optional 3-digit padlock"), ("Puzzles", "4 + final lock")],
        story="It’s Boxing Day. Everyone is full of turkey, but Grandad has locked the last tin of chocolates away ‘to stop you lot eating it all’. He’s left a trail of clues through the leftovers, the board games and the coat hooks. Solve them to win the tin.",
        cards=[
            {"title": "Grandad’s note", "intro": "Hand this to the players to start.", "type": "a riddle about leftovers.",
             "html": '<p>Right, you greedy lot. The chocolates are locked away. If you want them, you’ll have to earn them. Start here:</p><div class="poem">For turkey sandwiches you’ll need me,<br>I keep the loaf as fresh as can be.</div><p style="text-align:right">— Grandad</p>',
             "hide": "Hand to players at the start.", "answer": "BREAD BIN", "explain": "Riddle. Card 2 is in or by the bread bin."},
            {"title": "The family tradition", "intro": "Grandad moved every letter TWO places forward. Move each one back two.", "type": "a Caesar shift of two.",
             "html": f'<div class="puzzle-box">{spaced(shift("BOARD", 2))} &nbsp; {spaced(shift("GAMES", 2))}</div><p>Example: D becomes B.</p>',
             "hide": "In or by the bread bin.", "answer": "BOARD GAMES", "explain": "Shift each letter back two. Card 3 is in the board games cupboard or a game box."},
            {"title": "Time for a walk", "intro": "Grandad wrote this in secret pigpen code. Use the key.", "type": "a pigpen cipher with key.",
             "html": pig_word("COATS") + '<h4 style="margin:18px 0 8px">The key</h4>' + pig_key(28),
             "hide": "Inside a board game box.", "answer": "COATS", "explain": "Pigpen cipher. Card 4 is in a coat pocket on the coat hooks."},
            {"title": "The Boxing Day sales", "intro": "Grandad went to the sales. Work out what he spent.", "type": "a percentages maths lock.",
             "html": '<div class="poem">A jumper cost <strong>£40</strong>, with <strong>25% off</strong>.<br>A scarf cost <strong>£12</strong>, at <strong>half price</strong>.<br><br>How much did Grandad spend in total?<br>Write the answer as <strong>three digits</strong> (for example, £7 would be 007).</div>',
             "hide": "In a coat pocket.", "answer": "036", "explain": "£40 − 25% = £30; £12 ÷ 2 = £6; total £36 → 036. It opens the chocolate tin."},
        ],
        finale={"title": "The chocolates are yours!", "html": '<div class="pic">🍫🎉🍫</div><p style="text-align:center;font-size:1.2rem">Fine, fine, you win. Share them nicely.<br>And save me a strawberry cream.<br><strong>Grandad</strong></p>',
                "hide": "With the tin of chocolates, locked with a 3-digit padlock set to 036, or checked by the host.", "setup": "Put the final card with the chocolate tin. Lock it with a 3-digit padlock set to 036, or have the host check the code."},
        faq=[("What can families do on Boxing Day?", "A Boxing Day escape room gets everyone off the sofa without leaving the house. The Leftovers Lockdown takes 30–45 minutes, suits ages 8 to adult, and ends with a tin of chocolates."),
             ("Do I need a padlock?", "No. A 3-digit padlock set to 036 adds drama, but the host can simply check the answer."),
             ("Can grandparents play?", "Yes. The puzzles use leftovers, board games and the Boxing Day sales, so every generation can help."),
             ("Is there an answer key?", "Yes, at the bottom of this page.")],
        ages_min=8, players=(2, 8), minutes=45,
        easier="tell players that card 2 moves letters back two, and let them use a calculator for the sales.",
        harder="remove the pigpen key and hide it under the Christmas tree, and set a 25-minute limit.",
        related=[("New Year’s Eve escape room", "printable/new-years-eve/", ""), ("Scrooge’s Safe", "printable/scrooges-safe/", "harder, for adults"), ("Escape room builder", "tools/escape-room-builder/", "make your own")],
        audience="Boxing Day")

    # ============================================================ NEW YEAR'S EVE
    printable_game(
        slug="new-years-eve", name="Countdown to Midnight",
        h1="New Year’s Eve escape room: a printable countdown game",
        title="New Year’s Eve Escape Room – Free Printable Game",
        description="A free printable New Year’s Eve escape room for families, teens and adults. Roman numeral clock code, backwards message, number code and a countdown maths lock. 30–45 minutes.",
        answer="Countdown to Midnight is a free printable New Year’s Eve escape room for ages 10 to adult. Players crack a Roman numeral clock code, a backwards message, a number code and a countdown maths lock to find the party poppers before midnight. It takes 30–45 minutes.",
        spec=[("Ages", "10+ and adults"), ("Players", "2–8"), ("Time", "30–45 minutes"), ("Set-up", "10 minutes"), ("Difficulty", "Medium"), ("Best time", "Start around 11pm on 31 December"), ("You need", "Printer, 6 sheets of A4, party poppers or a small prize"), ("Puzzles", "4 + final lock")],
        story="The party poppers have been locked away and midnight is coming. Follow the clues from the clock to the sideboard and the fridge, crack the countdown code and find the poppers in time to see in the New Year.",
        cards=[
            {"title": "Time is ticking", "intro": "Each Roman numeral is a letter: I = A, II = B, III = C…", "type": "a Roman numeral code.",
             "html": '<div class="puzzle-box">' + " · ".join(roman(ALPHA.index(c) + 1) for c in "CLOCK") + '</div><p>Hint: X = 10 = J.</p>',
             "hide": "Hand to players at the start.", "answer": "CLOCK", "explain": "III=C, XII=L, XV=O, III=C, XI=K. Card 2 is by a clock."},
            {"title": "Out of order", "intro": "This message is back to front. Read it from right to left.", "type": "a backwards message.",
             "html": '<div class="puzzle-box">D R A O B E D I S</div>',
             "hide": "Next to or behind a clock.", "answer": "SIDEBOARD", "explain": "Read right to left. Card 3 is on or in the sideboard (or a shelf unit)."},
            {"title": "Keep it chilled", "intro": "Each number is a letter. A = 1, B = 2…", "type": "an A=1 number code.",
             "html": '<div class="puzzle-box">6 · 18 · 9 · 4 · 7 · 5</div>' + AZ_TABLE,
             "hide": "On or in the sideboard.", "answer": "FRIDGE", "explain": "F6 R18 I9 D4 G7 E5. Card 4 is in the fridge."},
            {"title": "The countdown", "intro": "Everyone counts down from ten at midnight.", "type": "a maths lock.",
             "html": '<div class="poem">10, 9, 8, 7, 6, 5, 4, 3, 2, 1…<br><br>Add up every number in the countdown.<br>That’s the code for the party poppers.</div>',
             "hide": "In the fridge.", "answer": "55", "explain": "10 + 9 + … + 1 = 55. It opens the box of party poppers."},
        ],
        finale={"title": "Happy New Year!", "html": '<div class="pic">🎉🕛🥂</div><p style="text-align:center;font-size:1.2rem">You made it before midnight!<br>Pop those poppers and Happy New Year!</p>',
                "hide": "In a box with the party poppers, locked with code 55 (a 2-digit code, or 055 on a 3-digit padlock).", "setup": "Put the final card in a box with party poppers. Lock it with 055 on a 3-digit padlock, or have the host check the code."},
        faq=[("What can we do on New Year’s Eve at home?", "Play a New Year’s Eve escape room. Countdown to Midnight takes 30–45 minutes; start around 11pm and finish just in time to pop the party poppers at midnight."),
             ("Is it suitable for adults?", "Yes. Ages 10 to adult. For a harder adult version, take away the hints and set a 20-minute limit."),
             ("Do I need a padlock?", "No. A padlock set to 055 is fun, but the host can check the answer."),
             ("Can children play?", "Children aged 10+ can play alone; younger children can join a team with an adult.")],
        ages_min=10, players=(2, 8), minutes=45,
        easier="give the Roman numeral key: I=1, V=5, X=10.",
        harder="remove the A–Z table and the Roman numeral hint, and start at 11.30pm.",
        related=[("Boxing Day escape room", "printable/boxing-day/", ""), ("Escape room timer", "tools/escape-room-timer/", "count down to midnight"), ("Scrooge’s Safe", "printable/scrooges-safe/", "for adults")],
        audience="New Year’s Eve")

    # ============================================================ KS2 CLASSROOM
    printable_game(
        slug="ks2-classroom", name="The Elf Inspection",
        h1="KS2 Christmas escape room: free printable classroom game",
        title="KS2 Christmas Escape Room – Free Classroom Printable",
        description="A free KS2 Christmas escape room for Years 3–6: times tables code, adjectives acrostic and fractions lock. Teams of 4–6, 45–60 minutes, teacher answer key included.",
        answer="The Elf Inspection is a free Christmas escape room for KS2 classes (Years 3–6). Teams crack a times-tables code, an adjectives puzzle and a fractions and multiplication lock to pass Santa’s elf inspection. It takes 45–60 minutes for teams of 4–6, with a teacher answer key.",
        spec=[("Year groups", "KS2: Years 3–6 (ages 7–11)"), ("Teams", "4–6 pupils per team; print one set per team"), ("Time", "45–60 minutes"), ("Set-up", "10 minutes"), ("Subjects", "Maths (times tables, division, fractions), English (adjectives)"), ("You need", "Printer, 5 sheets per team, a prize or certificate"), ("Puzzles", "3 stations + final check")],
        story="Santa’s Head Elf is visiting your class to see who is clever enough to work in the toy workshop. Each team must pass three stations, maths, English and the toy count, to earn its elf badges before the end of the lesson.",
        cards=[
            {"title": "Station 1: The times tables code", "intro": "Work out each answer, then turn it into a letter (A = 1, B = 2…).", "type": "times tables and division, turned into letters.",
             "html": '<div class="poem">1) 4 × 5 = ___<br>2) 3 × 3 = ___<br>3) 7 × 2 = ___<br>4) 38 ÷ 2 = ___<br>5) 25 ÷ 5 = ___<br>6) 3 × 4 = ___</div>' + AZ_TABLE + '<p>What festive word do the letters spell?</p>',
             "hide": "Give to each team at the start (or place at station 1).", "answer": "TINSEL", "explain": "20=T, 9=I, 14=N, 19=S, 5=E, 12=L. Show the teacher to get station 2."},
            {"title": "Station 2: Adjective detectives", "intro": "Find the ADJECTIVE (describing word) in each sentence. The first letters spell a word.", "type": "an English grammar puzzle (adjectives).",
             "html": '<div class="poem">1) The sparkly bauble hung on the tree.<br>2) A tall snowman stood in the garden.<br>3) We ate an amazing Christmas dinner.<br>4) Rudolph has a red nose.</div><p>Adjectives: ________ &nbsp; Word: ________</p>',
             "hide": "Hand over when a team shows TINSEL (or place at station 2).", "answer": "STAR", "explain": "sparkly, tall, amazing, red → S-T-A-R. Show the teacher to get station 3."},
            {"title": "Station 3: The toy count", "intro": "Solve each problem. The three answers make the code for Santa’s toy box.", "type": "fractions and multiplication word problems.",
             "html": '<div class="poem">A) Santa has 24 presents. Half go to Year 6 and a quarter go to Year 5. How many are left for Year 4?<br><br>B) How many sides does a square present have?<br><br>C) An elf wraps 2 presents every 5 minutes. How many presents does she wrap in 20 minutes?</div><div class="puzzle-box">_ &nbsp; _ &nbsp; _</div>',
             "hide": "Hand over when a team shows STAR (or place at station 3).", "answer": "648", "explain": "A: 24 − 12 − 6 = 6. B: 4. C: 20 ÷ 5 = 4 lots of 2 = 8. Code 648."},
        ],
        finale={"title": "Inspection passed!", "html": '<div class="pic">🧝🏅🎄</div><p style="text-align:center;font-size:1.2rem">TINSEL ✓ STAR ✓ 648 ✓<br>Congratulations! Your team has passed the Elf Inspection and may now work in Santa’s workshop.</p>',
                "hide": "Teacher keeps it. Hand it to each team that gives TINSEL, STAR and 648.", "setup": "Keep the final card (one per team) and hand it over when a team gives all three answers. Print certificates with our certificate maker."},
        faq=[("Is there a free KS2 Christmas escape room?", "Yes. The Elf Inspection is free for Years 3–6, takes 45–60 minutes and covers times tables, division, adjectives and fractions, with a teacher answer key."),
             ("How do I run it with a whole class?", "Split the class into teams of 4–6 and print one set per team. Either give each team Station 1 and hand out the next station when they show you the right answer, or set up three tables as stations and rotate."),
             ("Which year groups is it for?", "Years 3–6. For Year 3, read the questions aloud and allow a times-table grid; Year 6 can play with a 30-minute limit."),
             ("Does it link to the curriculum?", "Yes: multiplication and division facts, fractions of amounts, word problems and identifying adjectives, all part of the KS2 maths and English programmes of study.")],
        ages_min=7, players=(4, 6), minutes=60,
        easier="allow a multiplication grid and read the word problems aloud (Year 3–4).",
        harder="set a 30-minute limit and remove the A–Z table (Year 6).",
        related=[("Escape room advent calendar", "printable/advent-calendar/", "a puzzle a day in December"), ("Certificate maker", "tools/certificate-maker/", "print certificates for every team"), ("Escape room builder", "tools/escape-room-builder/", "make your own classroom version")],
        audience="KS2 classroom")

    # ============================================================ 10-MINUTE ONLINE
    online_game(
        slug="ten-minute-christmas-escape-room", name="The 10-Minute Workshop Escape",
        h1="10-minute Christmas escape room: play free online",
        title="10-Minute Christmas Escape Room – Free to Play Online",
        description="A quick free Christmas escape room you can play online in about 10 minutes. Three festive puzzles, no download, works on phones. Ideal for classrooms, breaks and parties.",
        answer="The 10-Minute Workshop Escape is a free online Christmas escape room you can finish in about 10 minutes. Solve three quick festive puzzles in your browser to escape Santa’s workshop before the elves lock up. No download or sign-up; it works on phones. Suits ages 7 and up.",
        spec=[("Ages", "7+"), ("Players", "1–6"), ("Time", "About 10 minutes"), ("Difficulty", "Easy"), ("Prep", "None"), ("Works on", "Phone, tablet, laptop, classroom whiteboard"), ("Puzzles", "3")],
        intro_title="The elves are locking up in 10 minutes!",
        intro="You’ve been accidentally locked in Santa’s workshop. Solve three quick puzzles to get out before the elves go home for Christmas.",
        puzzles=[
            {"title": "Puzzle 1 · The jumbled toy", "type": "an anagram.",
             "story": "A label on a toy has its letters all mixed up.",
             "html": '<div class="puzzle-box">N O T S W A M</div><p>Unscramble it to find a wintry friend.</p>',
             "hint": "It has a carrot nose and melts in the sun.", "answers": ["SNOWMAN"], "explain": "anagram of NOTSWAM.",
             "found": "Inside the snowman toy is a number written on a gift tag."},
            {"title": "Puzzle 2 · The doubling elves", "type": "a number pattern.",
             "story": "The elves wrap twice as many presents every hour.",
             "html": '<div class="puzzle-box">3 · 6 · 12 · 24 · ?</div><p>What number comes next?</p>',
             "hint": "Each number is double the one before.", "answers": ["48"], "numeric": True, "explain": "24 × 2.",
             "found": "The workshop door has one last coded label."},
            {"title": "Puzzle 3 · The door label", "type": "a Caesar shift of one.",
             "story": "The elves moved every letter ONE place forward in the alphabet.",
             "html": f'<div class="puzzle-box">{spaced(shift("TINSEL", 1))}</div><p>Move each letter back one to read it.</p>',
             "hint": "U becomes T, J becomes I…", "answers": ["TINSEL"], "explain": "shift each letter back one."},
        ],
        win_html='<div style="font-size:3rem">🚪✨</div><h2>You escaped the workshop!</h2><p>Just in time. The elves wave goodbye as you run out into the snow.</p>',
        faq=[("Is there a quick Christmas escape room?", "Yes. The 10-Minute Workshop Escape has three puzzles and takes about 10 minutes online, so it fits a lesson starter, a work break or the gap between courses."),
             ("Can I use it in class?", "Yes. Put it on the interactive whiteboard and let the class solve it together, or let pairs play on tablets."),
             ("Want something longer?", "Try The Missing Sleigh Key (20–30 minutes online) or a printable game such as The Great Pudding Heist.")],
        ages_min=7, players=(1, 6), minutes=10,
        how_to_play="<li>Press <strong>Start the game</strong>.</li><li>Solve each puzzle and press <strong>Unlock</strong>.</li><li>Try to finish in under 10 minutes!</li>",
        related=[("The Missing Sleigh Key", "play-online/the-missing-sleigh-key/", "longer online game"), ("KS2 Christmas escape room", "printable/ks2-classroom/", "for a full lesson"), ("Escape room timer", "tools/escape-room-timer/", "")])

    # ============================================================ NO PRINTER
    path = "play-online/no-printer-christmas-escape-room/"
    clues = [
        ("Clue 1 (give this to the players)", "I have a face and two hands, but no arms or legs. I tell you when it’s bedtime.", "Put clue 2 next to a clock.", "CLOCK"),
        ("Clue 2 (next to a clock)", "Backwards alphabet code: Z = 1, Y = 2, X = 3 … A = 26.<br><strong>8 · 12 · 21 · 26</strong>", "Put clue 3 under a sofa cushion.", "SOFA"),
        ("Clue 3 (under a sofa cushion)", "Take the first letter of each word: <strong>Tinsel, Angel, Bauble, Lights, Elf</strong>.", "Put clue 4 under the table.", "TABLE"),
        ("Clue 4 (under the table)", "Last one! Where does Santa leave the presents? Look under the ____.", "Put the prize under the Christmas tree.", "TREE"),
    ]
    rows = "".join(f'<div class="clue-card" style="page-break-after:auto;break-after:auto"><div class="num">{t}</div><p style="font-size:1.15rem">{c}</p><p class="hide-where">🧑‍🎄 Host: {h} Answer: <strong>{a}</strong></p></div>' for t, c, h, a in clues)
    faq = [("Can you do a Christmas escape room without a printer?", "Yes. Either play one online, like The Missing Sleigh Key, on a phone or laptop, or copy four short clues onto scraps of paper by hand. Both take under 10 minutes to set up."),
           ("What do I need for the handwritten version?", "Four pieces of paper, a pen, and a small prize to hide under the Christmas tree."),
           ("How long does it take?", "About 5 minutes to write the clues and 15–20 minutes to play.")]
    body = f"""
<div class="wrap narrow">
<p class="eyebrow">No printer needed</p>
<h1>Christmas escape room without a printer</h1>
{byline()}
<p class="answer">You can run a Christmas escape room with no printer in two ways: play a free online game such as The Missing Sleigh Key on any phone or laptop, or copy the four short clues below onto paper by hand. The handwritten game takes 5 minutes to set up and 15–20 minutes to play.</p>
{spec_table([("Option 1", "Play online: no printer, no set-up"), ("Option 2", "Handwrite 4 clues: 5-minute set-up"), ("Ages", "6+"), ("Players", "2–8"), ("Time", "15–20 minutes (handwritten)"), ("You need", "Paper, a pen and a small prize")])}
<h2>Option 1: play online</h2>
<div class="grid">
<a class="card" href="{{R}}play-online/the-missing-sleigh-key/index.html"><span class="icon">🔑</span><h3>The Missing Sleigh Key</h3><p>20–30 minutes, ages 8+, works on phones and over Zoom.</p></a>
<a class="card" href="{{R}}play-online/ten-minute-christmas-escape-room/index.html"><span class="icon">⏱️</span><h3>10-Minute Workshop Escape</h3><p>Three quick puzzles, ages 7+.</p></a>
<a class="card" href="{{R}}play-online/office-party-escape/index.html"><span class="icon">🥧</span><h3>The Office Party Escape</h3><p>For work teams and adults.</p></a>
</div>
<h2>Option 2: write the clues by hand</h2>
<ol class="steps"><li>Copy each clue below onto its own scrap of paper.</li><li>Hide each one where the host note says.</li><li>Put a small prize under the Christmas tree.</li><li>Hand clue 1 to the players and start the <a href="{{R}}tools/escape-room-timer/index.html">timer</a>.</li></ol>
{rows}
<p>Want more puzzles to write out? Use the <a href="{{R}}how-to/christmas-riddles-with-answers/index.html">30 Christmas riddles</a> or the <a href="{{R}}tools/escape-room-builder/index.html">escape room builder</a>, then copy its clues by hand.</p>
{faq_html(faq)}
</div>"""
    page(path, "Christmas Escape Room Without a Printer – 2 Free Ways",
         "No printer? Play a free Christmas escape room online on any phone, or handwrite 4 simple clues in 5 minutes. Ages 6+, 15–20 minutes, answers included.",
         body, crumbs=[("Play online", "play-online/"), ("No printer needed", path)],
         schema=[article_schema(path, "Christmas escape room without a printer", "Two ways to run a Christmas escape room with no printer."), faq_schema(faq)],
         active="Play online", og_image="assets/og/no-printer-christmas-escape-room.png")
