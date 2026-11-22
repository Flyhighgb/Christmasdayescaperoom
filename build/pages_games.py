from games_lib import printable_game, online_game, pig_word, pig_key, ALPHA
from layout import page, faq_html, faq_schema, spec_table, DOMAIN, byline, PERSON_ID


def shift(w, n):
    return "".join(ALPHA[(ALPHA.index(c) + n) % 26] if c in ALPHA else c for c in w)


def spaced(w):
    return " ".join(w)


AZ_TABLE = ('<table class="compare" style="font-size:.85rem"><tr>' + "".join(f"<td>{c} {i+1}</td>" + ("</tr><tr>" if (i + 1) % 9 == 0 else "") for i, c in enumerate(ALPHA)) + "</tr></table>")
KEYPAD = ('<table class="sheet"><tr><td>1</td><td>2<br><small>ABC</small></td><td>3<br><small>DEF</small></td></tr>'
          '<tr><td>4<br><small>GHI</small></td><td>5<br><small>JKL</small></td><td>6<br><small>MNO</small></td></tr>'
          '<tr><td>7<br><small>PQRS</small></td><td>8<br><small>TUV</small></td><td>9<br><small>WXYZ</small></td></tr></table>'
          '<p style="text-align:center"><small>Old phone texting: press a key once for its first letter, twice for the second, and so on.</small></p>')
MORSE = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--",
         "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--.."}
MORSE_KEY = '<table class="compare" style="font-size:.85rem"><tr>' + "".join(f"<td><b>{c}</b> {m}</td>" + ("</tr><tr>" if (i + 1) % 7 == 0 else "") for i, (c, m) in enumerate(MORSE.items())) + "</tr></table>"


def build():
    # ======================================================= ONLINE: SLEIGH KEY
    online_game(
        slug="the-missing-sleigh-key", name="The Missing Sleigh Key",
        h1="The Missing Sleigh Key: free online Christmas escape room",
        title="The Missing Sleigh Key – Free Online Christmas Escape Room (No Download)",
        description="Play a free online Christmas escape room. Crack 5 festive locks to find Santa’s sleigh key. 20–30 minutes, ages 8+, works on phones, no download or sign-up.",
        answer="The Missing Sleigh Key is a free Christmas escape room you play in your browser. Crack five festive locks to find Santa’s lost key on Christmas Eve. It takes 20–30 minutes, suits 1–6 players aged 8+, and needs no download, printer or sign-up.",
        spec=[("Ages", "8+ (5–7 with a grown-up)"), ("Players", "1–6, or teams over Zoom"), ("Time", "20–30 minutes"), ("Difficulty", "Easy–medium"), ("Prep", "None"), ("You need", "A phone, tablet or computer. Paper and pen help."), ("Puzzles", "5")],
        intro_title="Ready to save Christmas?",
        intro="Santa leaves at midnight, but his sleigh key is missing. The elves left a trail of five locked clues. Solve each one to unlock the next. Grab a pen and paper for working out.",
        puzzles=[
            {"title": "Lock 1 · Rudolph’s coded note", "type": "a Caesar shift code, where every letter has moved 3 places.",
             "story": "It’s 10pm on Christmas Eve and Santa can’t find his sleigh key. Rudolph left a note saying where the elves started looking, but he wrote it in code.",
             "html": f'<div class="puzzle-box">{spaced(shift("CHIMNEY", 3))}</div><p>Rudolph moved every letter <strong>3 places forward</strong> in the alphabet.</p>',
             "hint": "Move each letter back 3 places: F becomes C, K becomes H…", "answers": ["CHIMNEY"], "explain": "shift each letter back 3.",
             "found": "Up the chimney you find a bundle of gift tags with numbers on them."},
            {"title": "Lock 2 · Mrs Claus’s gift tags", "type": "a number code where A = 1, B = 2 and so on.",
             "story": "Mrs Claus numbered her gift tags instead of writing names. Together they spell where the elves looked next.",
             "html": '<div class="puzzle-box">19 · 20 · 15 · 3 · 11 · 9 · 14 · 7</div><p>Each number is a letter.</p>',
             "hint": "A = 1, B = 2, C = 3 … S = 19.", "answers": ["STOCKING", "STOCKINGS"], "explain": "A=1 number code.",
             "found": "Inside the stocking is a scrap of paper with a riddle in elf handwriting."},
            {"title": "Lock 3 · The elf’s riddle", "type": "a rhyming riddle.",
             "story": "Jingle the elf loves riddles. Solve this one to find the next hiding place.",
             "html": '<div class="poem">I’m dressed up just once every year,<br>with lights and baubles, tinsel and cheer.<br>I have plenty of needles but never sew.<br>Look under me where the presents go.</div>',
             "hint": "It stands in the living room and has a star or angel on top.", "answers": ["TREE", "CHRISTMASTREE"], "explain": "needles, baubles, presents underneath.",
             "found": "Under the tree is a toy box with a three-digit dial lock."},
            {"title": "Lock 4 · The toy box dial", "type": "a Christmas maths lock.",
             "story": "A label on the toy box reads: ‘Only someone who knows Christmas can open me.’",
             "html": '<div class="poem">Take the number of reindeer that pull Santa’s sleigh <em>(don’t forget Rudolph)</em>,<br>multiply it by the number of days in “The Twelve Days of Christmas”,<br>then add the date of Christmas Day in December.</div>',
             "hint": "9 reindeer × 12 days, then add 25.", "answers": ["133"], "numeric": True, "explain": "9 × 12 + 25.",
             "found": "The lid springs open. Inside is a poem from Santa himself."},
            {"title": "Lock 5 · Santa’s poem", "type": "an acrostic poem, where the first letters spell the answer.",
             "story": "Santa always hides things in plain sight. The first letter of each line tells you where he put the key.",
             "html": '<div class="poem">Candles flicker in the hall,<br>Ornaments hang on the wall,<br>Over the rooftops snowflakes fall,<br>Kettle’s on for one and all,<br>Ivy twists round every door,<br>Elves are napping on the floor,<br>Stockings wait for Santa’s call.</div>',
             "hint": "Read the first letter of each line from top to bottom. Santa gets left a plate of these.", "answers": ["COOKIES", "COOKIE"], "explain": "first letters of each line."},
        ],
        win_html='<div style="font-size:3rem">🎅🔑</div><h2>You saved Christmas!</h2><p>The key was next to the plate of cookies all along. Santa’s sleigh is on its way.</p>',
        faq=[("How long does The Missing Sleigh Key take?", "Most families finish in 20–30 minutes. Fast adult teams can finish in under 10 minutes; younger children may take 40 minutes with a grown-up helping."),
             ("What age is it for?", "Ages 8 and up can play on their own. Children aged 5–7 can play with an adult reading the clues and helping with the maths lock."),
             ("Is there an answer key?", "Yes. Each lock has a hint button, and the full answers are at the bottom of this page behind a ‘show answers’ button."),
             ("Can we play it on a phone?", "Yes. The game works in any modern browser on phones, tablets and computers. Nothing to download."),
             ("Can we play over Zoom?", "Yes. One person shares their screen and everyone calls out answers, or each household plays the link at the same time and compares finishing times.")],
        ages_min=8, players=(1, 6), minutes=30,
        how_to_play="<li>Press <strong>Start the game</strong>. The timer starts.</li><li>Read the story and solve the puzzle. Type the answer and press <strong>Unlock</strong>.</li><li>Stuck? Press <strong>Need a hint?</strong></li><li>Open all five locks, then make a <a href=\"../../tools/certificate-maker/index.html\">certificate</a> with your time.</li>",
        extra_sections='<h2>Playing over Zoom or FaceTime</h2><p>One person shares their screen and reads the story aloud; everyone else shouts answers. Or send the link to each household, start together and compare finishing times at the end. It works well for grandparents who can’t travel.</p>',
        related=[("The Office Party Escape", "play-online/office-party-escape/", "harder online game for teams"), ("The Great Pudding Heist", "printable/the-great-pudding-heist/", "printable, hide round the house"), ("Christmas riddles with answers", "how-to/christmas-riddles-with-answers/", "")])

    # ======================================================= ONLINE: OFFICE PARTY
    grid = {("B", 2): "M", ("D", 4): "I", ("A", 1): "N", ("E", 5): "C", ("C", 3): "E"}
    filler = "QWTRLKPHSDGAZOVXUBYFJ"
    k = 0; rows = ""
    for r in range(1, 6):
        rows += f"<tr><th>{r}</th>"
        for c in "ABCDE":
            if (c, r) in grid: rows += f"<td>{grid[(c, r)]}</td>"
            else: rows += f"<td>{filler[k % len(filler)]}</td>"; k += 1
        rows += "</tr>"
    sheet = f'<table class="sheet"><tr><th></th><th>A</th><th>B</th><th>C</th><th>D</th><th>E</th></tr>{rows}</table>'
    online_game(
        slug="office-party-escape", name="The Office Party Escape",
        h1="Free office Christmas party escape room (online, for teams)",
        title="Free Office Christmas Party Escape Room – Online Team Game | No Host Needed",
        description="Free online Christmas escape room for office parties and remote teams. 5 puzzles, 20–30 minutes, teams of 2–6, no host, no booking. Works on Zoom and Teams.",
        answer="The Office Party Escape is a free online Christmas escape room for work teams. Split into teams of 2–6, open the link on a laptop or over Zoom or Teams, and race to crack five office-themed puzzles in 20–30 minutes. No host, booking or payment needed.",
        spec=[("Players", "Teams of 2–6; any number of teams"), ("Ages", "Adults (14+)"), ("Time", "20–30 minutes"), ("Difficulty", "Medium"), ("Prep", "None. Send the link."), ("Works on", "Laptop, phone, Zoom, Teams, Google Meet"), ("Cost", "Free"), ("Puzzles", "5")],
        intro_title="It’s 4.55pm on the last day before Christmas…",
        intro="The office party is about to start, but someone has locked the meeting room where the mince pies are kept. Your team has five clues left by the office elf. Get in before the pies are gone.",
        puzzles=[
            {"title": "Puzzle 1 · The inbox", "type": "an acrostic hidden in email subject lines.",
             "story": "The office elf has sent five emails this morning. The subject lines hide one word.",
             "html": '<div class="poem">📧 Printer jammed again – please don’t touch<br>📧 Annual leave requests due Friday<br>📧 Reminder: Secret Santa limit is £10<br>📧 Tinsel found in the kitchen sink<br>📧 Year-end figures attached</div>',
             "hint": "Look at the first letter of each subject line.", "answers": ["PARTY"], "explain": "first letters of the subject lines.",
             "found": "A sticky note on the party poster says: ‘Ring the elf.’ Under it is a string of numbers."},
            {"title": "Puzzle 2 · The desk phone", "type": "a phone keypad (multi-tap) code.",
             "story": "The elf left a message typed the old way, on a phone keypad.",
             "html": '<div class="puzzle-box">7777 · 2 · 66 · 8 · 2</div>' + KEYPAD,
             "hint": "7777 = the 4th letter on key 7 (S). 2 = the 1st letter on key 2 (A).", "answers": ["SANTA"], "explain": "multi-tap phone code.",
             "found": "Santa’s name unlocks a shared spreadsheet called ‘Party Food’."},
            {"title": "Puzzle 3 · The spreadsheet", "type": "spreadsheet cell references.",
             "story": "The Party Food sheet is a jumble of letters. A comment says: ‘B2, D4, A1, E5, C3’.",
             "html": sheet,
             "hint": "Find column B, row 2 first. Then D4, A1, E5 and C3. Put the letters in that order.", "answers": ["MINCE", "MINCEPIE", "MINCEPIES"], "explain": "letters at B2, D4, A1, E5, C3.",
             "found": "‘Mince’ opens the food rota, but someone has mixed up who is bringing what."},
            {"title": "Puzzle 4 · The food rota", "type": "a short logic puzzle.",
             "story": "Amy, Ben, Cat and Dev are each bringing one thing: turkey, sprouts, crackers or the Christmas pudding. Whoever brings the pudding has the meeting room key.",
             "html": '<ol class="poem" style="padding-left:2.2em"><li>Ben hates sprouts and won’t bring them.</li><li>Cat is bringing the crackers.</li><li>The turkey is coming from Amy or Dev.</li><li>Dev is vegetarian, so he isn’t bringing the turkey.</li></ol><p>Who is bringing the pudding?</p>',
             "hint": "Dev can’t bring the turkey, so Amy does. That leaves sprouts and pudding for Ben and Dev.", "answers": ["BEN"], "explain": "Amy turkey, Cat crackers, Dev sprouts, Ben pudding.",
             "found": "Ben hands over the key, but the meeting room also has a 4-digit keypad."},
            {"title": "Puzzle 5 · The meeting room keypad", "type": "a code built from the answers so far.",
             "story": "A note on the door says: ‘The code is how many letters were in each of your answers, in order.’",
             "html": '<div class="puzzle-box">_ &nbsp; _ &nbsp; _ &nbsp; _</div><p>Your answers so far were to puzzles 1, 2, 3 and 4.</p>',
             "hint": "PARTY has 5 letters. Do the same for SANTA, MINCE and BEN.", "answers": ["5553"], "numeric": True, "explain": "PARTY 5, SANTA 5, MINCE 5, BEN 3."},
        ],
        win_html='<div style="font-size:3rem">🥧🎉</div><h2>You escaped to the party!</h2><p>The door clicks open and the mince pies are still warm. Merry Christmas from the office elf.</p>',
        faq=[("How do we run an office Christmas escape room for free?", "Split everyone into teams of 2–6, send each team the link to this page, start at the same time and compare finishing times. Put the escape room timer on the big screen for atmosphere. There’s no booking, host or cost."),
             ("Does it work for remote teams on Zoom or Teams?", "Yes. Use breakout rooms: each team shares one screen and works together, then everyone returns to the main room to compare times and hints used."),
             ("How long does it take?", "Most teams finish in 20–30 minutes, which fits a lunchtime or the start of a party."),
             ("Is it suitable for everyone in the office?", "Yes. The puzzles use everyday office things (emails, phones, spreadsheets) and need no Christmas knowledge beyond the basics. Nothing is religious or rude."),
             ("How do we pick a winner?", "Fastest time wins. Add 2 minutes for each hint used, and print certificates for the winning team with our certificate maker.")],
        ages_min=14, players=(2, 6), minutes=30,
        how_to_play="<li>Split into teams of 2–6 and send each team this page’s link.</li><li>Everyone presses <strong>Start</strong> at the same moment.</li><li>Each team notes its time and hints used when it escapes.</li><li>Fastest time wins (add 2 minutes per hint). Print a <a href=\"../../tools/certificate-maker/index.html\">certificate</a> for the winners.</li>",
        extra_sections='<h2>Hosting tips for work parties</h2><ul><li><strong>In the office:</strong> one laptop per team, timer on the meeting room screen.</li><li><strong>Hybrid or remote:</strong> breakout rooms of 3–5 people, one person shares their screen.</li><li><strong>Big groups (30+):</strong> run it as a race in rounds and play the final between the two fastest teams.</li><li><strong>Prizes:</strong> first choice from the Secret Santa pile goes down well.</li></ul>',
        related=[("Escape room timer", "tools/escape-room-timer/", "put it on the big screen"), ("The Missing Sleigh Key", "play-online/the-missing-sleigh-key/", "easier online game"), ("Scrooge’s Safe", "printable/scrooges-safe/", "printable game for adults")],
        audience="Work teams")

    # ======================================================= PRINTABLE: PUDDING HEIST
    printable_game(
        slug="the-great-pudding-heist", name="The Great Pudding Heist",
        h1="The Great Pudding Heist: free printable Christmas escape room",
        title="The Great Pudding Heist – Free Printable Christmas Escape Room for Kids & Families",
        description="Free printable Christmas escape room: 5 clue cards to hide round the house. Ages 6+, 30–45 minutes, 10-minute set-up, no padlocks. Answer key included.",
        answer="The Great Pudding Heist is a free printable Christmas escape room for ages 6 and up. Mischief the elf has hidden the Christmas pudding; players follow five clue cards hidden around the house to find it. It takes 10 minutes to set up and 30–45 minutes to play, with no padlocks needed.",
        spec=[("Ages", "6+ (4–5 with help)"), ("Players", "2–8"), ("Time", "30–45 minutes"), ("Set-up", "10 minutes"), ("Difficulty", "Easy"), ("You need", "Printer, 6 sheets of A4, pen, a prize (optional)"), ("Puzzles", "5")],
        story="Mischief, the cheekiest elf at the North Pole, has hidden the family’s Christmas pudding just before dinner. He’s left a trail of clues around the house, each one harder than the last. Players must follow the trail from the fridge to the stocking, the sofa and the cracker box to find the pudding in time.",
        cards=[
            {"title": "The letter", "intro": "Give this to the players to start.", "type": "a rhyming riddle inside Mischief’s letter.",
             "html": "<p>Dear detectives,</p><p>I’m Mischief, the cheekiest elf at the North Pole, and I’ve hidden your <strong>Christmas pudding</strong>! Ha!</p><p>Follow my clues to find it before Christmas dinner. Here’s the first one:</p><div class=\"poem\">I hum all day and I’m cold inside,<br>where the milk and butter like to hide.</div><p>Love (not really),<br><strong>Mischief the Elf</strong></p>",
             "hide": "Hand to players at the start.", "answer": "FRIDGE", "explain": "Rhyming riddle. Card 2 is on or in the fridge."},
            {"title": "The scramble", "intro": "Unscramble the letters to find where to look next.", "type": "a word scramble.",
             "html": '<div class="puzzle-box">G N I K C O T S</div><p>Hint from Mischief: “It hangs by the fireplace and Santa fills it.”</p>',
             "hide": "In or on the fridge.", "answer": "STOCKING", "explain": "Anagram of GNIKCOTS. Card 3 is in a stocking."},
            {"title": "The number code", "intro": "Each number is a letter. A = 1, B = 2, C = 3…", "type": "an A=1 number code.",
             "html": '<div class="puzzle-box">19 · 15 · 6 · 1</div>' + AZ_TABLE,
             "hide": "Inside a stocking.", "answer": "SOFA", "explain": "S19 O15 F6 A1. Card 4 is under a sofa cushion."},
            {"title": "The shifty code", "intro": "Mischief moved every letter ONE place forward. Move each one back to read it.", "type": "a Caesar shift of one.",
             "html": f'<div class="puzzle-box">{spaced(shift("CRACKERS", 1))}</div><p>Example: D becomes C.</p>',
             "hide": "Under a sofa cushion.", "answer": "CRACKERS", "explain": "Shift each letter back one. Card 5 is with the crackers."},
            {"title": "The backwards message", "intro": "Mischief wrote this clue back to front. Read it from right to left.", "type": "a backwards message.",
             "html": '<div class="puzzle-box">D R A O B P U C &nbsp; N E H C T I K</div><p>That’s where the pudding is!</p>',
             "hide": "In or under the box of Christmas crackers.", "answer": "KITCHEN CUPBOARD", "explain": "Read right to left. The pudding and final card are in a kitchen cupboard."},
        ],
        finale={"title": "You found the pudding!", "html": '<div class="pic">🎄🍮🎄</div><p style="text-align:center;font-size:1.2rem">Curses! You beat me this year, detectives.<br>Enjoy your pudding, and merry Christmas!<br><strong>Mischief the Elf</strong></p>',
                "hide": "In the kitchen cupboard with the pudding or a prize.", "setup": "Put the pudding (or a prize) and the final card in a kitchen cupboard."},
        faq=[("What do I need for The Great Pudding Heist?", "A printer, 6 sheets of A4 paper, a pen and the hiding places: fridge, a stocking, the sofa, a box of crackers and a kitchen cupboard."),
             ("How long does it take?", "Set-up takes about 10 minutes. Most families finish the trail in 30–45 minutes."),
             ("Can I play it without a printer?", "Yes. Copy the five clues by hand onto paper, or play our online game The Missing Sleigh Key, which needs no printer."),
             ("What if I don’t have one of the hiding places?", "Swap it for one you have and change the clue to match. Use our cipher maker to re-code the new word."),
             ("Is it suitable for adults?", "Yes. Add a 20-minute limit and remove the hints. For a properly hard adult game, try Scrooge’s Safe.")],
        ages_min=6, players=(2, 8), minutes=45,
        easier="read each card aloud and leave a corner poking out of each hiding place.",
        harder="set a 20-minute limit, cover the hints with sticky notes and put a combination padlock (code 133) on the prize.",
        related=[("Rudolph’s Lost Bells", "printable/rudolphs-lost-bells/", "for ages 3–5"), ("Elf Academy Final Exam", "printable/elf-academy-final-exam/", "for teenagers"), ("The Missing Sleigh Key", "play-online/the-missing-sleigh-key/", "play online")],
        audience="Families")

    # ======================================================= PRINTABLE: ADULTS
    printable_game(
        slug="scrooges-safe", name="Scrooge’s Safe",
        h1="Scrooge’s Safe: free printable Christmas escape room for adults",
        title="Free Printable Christmas Escape Room for Adults – Scrooge’s Safe",
        description="A properly tricky free printable Christmas escape room for adults and teens 14+. Pigpen cipher, mirror writing, Caesar shift and a Dickens logic lock. 45–60 minutes.",
        answer="Scrooge’s Safe is a free printable Christmas escape room for adults and teenagers 14+. Based on A Christmas Carol, players crack a Caesar shift, a pigpen cipher, mirror writing and a four-digit logic lock to open Scrooge’s safe. It takes 45–60 minutes for 2–6 players.",
        spec=[("Ages", "14+ and adults"), ("Players", "2–6"), ("Time", "45–60 minutes"), ("Set-up", "15 minutes"), ("Difficulty", "Hard"), ("You need", "Printer, 6 sheets of A4, a hand mirror, a box or bag for the ‘safe’, optional 4-digit padlock"), ("Puzzles", "4 + final lock")],
        story="It’s Christmas Eve, 1843. Ebenezer Scrooge has locked his fortune in a safe and gone to bed grumbling. Players must follow the clues left by the ghosts who will visit him that night, open the safe and give the money to the Cratchits before Christmas morning.",
        cards=[
            {"title": "A note from Marley", "intro": "Hand this to the players to start.", "type": "a Caesar shift where players must work out the shift from the story.",
             "html": f'<p>Ebenezer, you will be haunted tonight. Count every ghost who visits you, <em>including me</em>, and move each letter back that many places to find my next message.</p><div class="puzzle-box">{spaced(shift("BOOKSHELF", 4))}</div><p style="text-align:right">— Jacob Marley</p>',
             "hide": "Hand to players at the start.", "answer": "BOOKSHELF", "explain": "Marley + three spirits = 4 ghosts. Shift each letter back 4. Card 2 is on a bookshelf."},
            {"title": "The Ghost of Christmas Past", "intro": "These strange marks were scratched into Scrooge’s old school desk.", "type": "a pigpen cipher with the key included.",
             "html": pig_word("MIRROR") + '<h4 style="margin:18px 0 8px">The key</h4>' + pig_key(28),
             "hide": "Tucked into a book on a bookshelf.", "answer": "MIRROR", "explain": "Pigpen cipher. Card 3 is taped to a mirror."},
            {"title": "The Ghost of Christmas Present", "intro": "The ghost only speaks in reflections.", "type": "mirror writing.",
             "html": '<div class="puzzle-box" style="transform:scaleX(-1)">LOOK INSIDE THE BISCUIT TIN</div>',
             "hide": "Taped to a mirror (use a hand mirror if it’s easier).", "answer": "BISCUIT TIN", "explain": "Hold the card up to a mirror. Card 4 is in the biscuit tin."},
            {"title": "The Ghost of Christmas Yet to Come", "intro": "The silent ghost points at four numbers chalked on a gravestone.", "type": "a logic lock that needs knowledge of A Christmas Carol.",
             "html": '<table class="sheet"><tr><th>Ghost</th><th>Number</th></tr><tr><td>Christmas Yet to Come</td><td>1</td></tr><tr><td>Christmas Past</td><td>3</td></tr><tr><td>Christmas Present</td><td>7</td></tr><tr><td>Jacob Marley</td><td>9</td></tr></table><p>The safe code is these four numbers <strong>in the order the ghosts visit Scrooge</strong>.</p>',
             "hide": "Inside the biscuit tin.", "answer": "9371", "explain": "Marley visits first (9), then Past (3), Present (7) and Yet to Come (1). It opens the safe."},
        ],
        finale={"title": "Scrooge’s Safe is open!", "html": '<div class="pic">🗝️💷🦃</div><p style="text-align:center;font-size:1.2rem">“I will honour Christmas in my heart, and try to keep it all the year.”<br>You have saved the Cratchits’ Christmas. God bless us, every one!</p>',
                "hide": "Inside the ‘safe’ (a box or bag, padlocked with 9371 if you have one).", "setup": "Put the final card and a prize in a box or bag. Lock it with a 4-digit padlock set to 9371, or have the host check the code."},
        faq=[("Is there a free printable Christmas escape room for adults?", "Yes. Scrooge’s Safe is free, designed for adults and teens 14+, and takes 45–60 minutes. It uses a pigpen cipher, mirror writing, a Caesar shift and a logic lock based on A Christmas Carol."),
             ("Do I need to know A Christmas Carol?", "It helps for the final lock, but the story section gives players enough to work it out: Marley visits first, then the ghosts of Christmas Past, Present and Yet to Come."),
             ("Do I need a padlock?", "No. A 4-digit padlock set to 9371 adds drama, but the host can simply check the code and hand over the final card."),
             ("Can we play it at a Christmas dinner party?", "Yes. Set it up before guests arrive and play between courses. Teams of 2–3 work best; make two copies to race."),
             ("How hard is it?", "Harder than our family games. Most adult teams finish in 45–60 minutes with one or two hints.")],
        ages_min=14, players=(2, 6), minutes=60,
        easier="tell players there are four ghosts, and let them use the full pigpen key from the start.",
        harder="remove the pigpen key from card 2 and hide it somewhere else in the room, and set a 40-minute limit.",
        related=[("The Office Party Escape", "play-online/office-party-escape/", "online game for teams"), ("Christmas cipher maker", "tools/christmas-cipher-maker/", "make your own codes"), ("Elf Academy Final Exam", "printable/elf-academy-final-exam/", "for teenagers")],
        audience="Adults")

    # ======================================================= PRINTABLE: TEENS
    printable_game(
        slug="elf-academy-final-exam", name="Elf Academy Final Exam",
        h1="Elf Academy Final Exam: printable Christmas escape room for teenagers",
        title="Christmas Escape Room for Teenagers – Free Printable | Elf Academy Final Exam",
        description="Free printable Christmas escape room for teenagers (ages 11–16). Old-phone texting code, Morse code, missing vowels and a 12 Days of Christmas maths lock. 30–45 minutes.",
        answer="Elf Academy Final Exam is a free printable Christmas escape room for teenagers aged 11–16. Players crack an old-phone texting code, Morse code, a missing-vowels puzzle and a Twelve Days of Christmas maths lock to pass the exam. It takes 30–45 minutes for 2–6 players.",
        spec=[("Ages", "11–16 (adults welcome)"), ("Players", "2–6"), ("Time", "30–45 minutes"), ("Set-up", "10 minutes"), ("Difficulty", "Medium–hard"), ("You need", "Printer, 5 sheets of A4, a prize"), ("Puzzles", "4 + final code")],
        story="Every elf must pass the Elf Academy Final Exam before being allowed into Santa’s workshop. This year the head elf has hidden the exam papers around your house. Find them all and solve each one to earn your place and your prize.",
        cards=[
            {"title": "Exam paper 1: Ancient technology", "intro": "Before smartphones, people texted like this.", "type": "an old-phone multi-tap code.",
             "html": '<div class="puzzle-box">777 · 33 · 6 · 666 · 8 · 33</div>' + KEYPAD,
             "hide": "Hand to players at the start.", "answer": "REMOTE", "explain": "R=777, E=33, M=6, O=666, T=8, E=33. Card 2 is with the TV remote."},
            {"title": "Exam paper 2: Signals", "intro": "Santa’s sleigh sends messages in Morse code.", "type": "Morse code with the key included.",
             "html": '<div class="puzzle-box">' + " / ".join(MORSE[c] for c in "WARDROBE") + '</div>' + MORSE_KEY,
             "hide": "Under or taped to the TV remote.", "answer": "WARDROBE", "explain": "Morse code. Card 3 is in a wardrobe."},
            {"title": "Exam paper 3: Vowel thief", "intro": "Mischief the elf has stolen every vowel from this clue.", "type": "a missing-vowels puzzle.",
             "html": '<div class="puzzle-box">L K &nbsp; N &nbsp; T H &nbsp; S H &nbsp; R C K</div>',
             "hide": "Inside a wardrobe.", "answer": "SHOE RACK", "explain": "LOOK IN THE SHOE RACK. Card 4 is in the shoe rack or by the front door shoes."},
            {"title": "Exam paper 4: Festive maths", "intro": "In “The Twelve Days of Christmas”, the true love gives 1 gift on day 1, 1 + 2 gifts on day 2, 1 + 2 + 3 on day 3, and so on.", "type": "a maths puzzle (triangular numbers).",
             "html": '<div class="poem">How many gifts are given <strong>in total</strong> over all twelve days?<br><br>That number is the code for your prize.</div>',
             "hide": "In the shoe rack.", "answer": "364", "explain": "Day n gives 1+…+n. Adding days 1 to 12: 1+3+6+10+15+21+28+36+45+55+66+78 = 364."},
        ],
        finale={"title": "Exam passed!", "html": '<div class="pic">🎓🧝🎄</div><p style="text-align:center;font-size:1.2rem">Congratulations, graduate. You scored 364 out of 364.<br>Welcome to Santa’s workshop.</p>',
                "hide": "With the prize. Players get it by telling the host the code 364 (or opening a padlock set to 364).", "setup": "Put the prize and the final card in a bag or box. Lock it with a 3-digit padlock set to 364, or have the host check the code."},
        faq=[("What’s a good Christmas escape room for teenagers?", "Elf Academy Final Exam is a free printable game built for ages 11–16. It uses old-phone texting, Morse code, a missing-vowels puzzle and a maths lock, so it’s harder than kids’ games but not too long. It takes 30–45 minutes."),
             ("Can teenagers set it up themselves?", "Yes. One teen can host for younger siblings, or a parent can hide the cards in 10 minutes."),
             ("Can adults play too?", "Yes. Adults can join a teen team, or race them with a second copy."),
             ("What if they get stuck on the maths?", "Hint: work out how many gifts arrive each day (1, 3, 6, 10…) and add them up. The answer is 364.")],
        ages_min=11, players=(2, 6), minutes=45,
        easier="say the first card is a phone keypad code and let players use a calculator for the final puzzle.",
        harder="remove the Morse key and hide it in a different room, and set a 30-minute limit.",
        related=[("Scrooge’s Safe", "printable/scrooges-safe/", "harder, for adults"), ("The Missing Sleigh Key", "play-online/the-missing-sleigh-key/", "play online"), ("Christmas riddles with answers", "how-to/christmas-riddles-with-answers/", "")],
        audience="Teenagers")

    # ======================================================= PRINTABLE: TODDLERS
    printable_game(
        slug="rudolphs-lost-bells", name="Rudolph’s Lost Bells",
        h1="Rudolph’s Lost Bells: Christmas escape room for toddlers and preschoolers",
        title="Christmas Escape Room for Toddlers & Preschoolers (Ages 3–5) – Free Printable",
        description="A free picture-based Christmas escape room for toddlers and preschoolers aged 3–5. No reading needed: match pictures, count and find Rudolph’s bells. 15–20 minutes.",
        answer="Rudolph’s Lost Bells is a free picture-based Christmas escape room for children aged 3–5. No reading is needed: each card shows a big picture of where to look next, with simple counting and colour games. It takes 15–20 minutes, with a grown-up reading the story.",
        spec=[("Ages", "3–5 (and 6-year-olds who are new to escape rooms)"), ("Players", "1–4 children with a grown-up"), ("Time", "15–20 minutes"), ("Set-up", "5 minutes"), ("Difficulty", "Very easy"), ("Reading needed", "None. Picture clues only."), ("You need", "Printer, 5 sheets of A4, a bell or small treat for the end")],
        story="Oh no! Rudolph has lost the jingle bells from his harness and can’t fly on Christmas Eve without them. Little helpers follow Rudolph’s picture clues around the house to find the bells. A grown-up reads each card aloud.",
        cards=[
            {"title": "Rudolph needs help!", "intro": "Grown-up: read this aloud, then show the picture.", "type": "a picture clue.",
             "html": '<p class="big-print">“I’ve lost my bells! Can you help me find them? My first clue is somewhere fluffy that hangs up for Santa.”</p><div class="pic">🧦</div>',
             "hide": "Hand to the children at the start.", "answer": "Stocking", "explain": "Picture of a stocking."},
            {"title": "Count with Rudolph", "intro": "Grown-up: ask the children to count the presents, then do that many jumps!", "type": "a counting game, then a picture clue.",
             "html": '<div class="pic">🎁 🎁 🎁</div><p class="big-print" style="text-align:center">Count and jump! Now find the next clue near…</p><div class="pic">🎄</div>',
             "hide": "In a stocking.", "answer": "3 jumps, then the Christmas tree", "explain": "Counting to 3, then the tree picture."},
            {"title": "Colour hunt", "intro": "Grown-up: ask the children to find three red things in the room, then look for the next clue.", "type": "a colour hunt, then a picture clue.",
             "html": '<div class="pic" style="color:#b3263a">🔴 🔴 🔴</div><p class="big-print" style="text-align:center">Find 3 red things! Then look somewhere soft you sit on…</p><div class="pic">🛋️</div>',
             "hide": "Under the Christmas tree.", "answer": "3 red things, then the sofa", "explain": "Colour hunt, then the sofa picture."},
            {"title": "Rudolph’s snack", "intro": "Grown-up: ask “What does Rudolph like to eat on Christmas Eve?”", "type": "a matching clue.",
             "html": '<div class="pic">🥕</div><p class="big-print" style="text-align:center">Rudolph loves carrots! Where do we keep the food?</p><div class="pic">🍽️</div>',
             "hide": "Under a sofa cushion.", "answer": "Kitchen", "explain": "Carrot leads to the kitchen."},
        ],
        finale={"title": "You found the bells!", "html": '<div class="pic">🔔🦌🔔</div><p class="big-print" style="text-align:center">Jingle jingle! Thank you, little helpers.<br>Now Rudolph can fly!</p>',
                "hide": "In the kitchen with a bell, or a small treat.", "setup": "Put the final card with a bell or small treat in the kitchen."},
        faq=[("Can toddlers do an escape room?", "Yes, if it uses pictures instead of words. Rudolph’s Lost Bells is built for ages 3–5: a grown-up reads each card and the children match the picture to a place in the house."),
             ("How long does it take?", "About 15–20 minutes, which suits young attention spans. Set-up takes 5 minutes."),
             ("Can older siblings help?", "Yes. Older children can be ‘Rudolph’s helpers’ and read the cards aloud to the little ones."),
             ("What should the prize be?", "A jingle bell, a sticker or a small treat works well. Little ones love ringing a bell at the end.")],
        ages_min=3, players=(1, 4), minutes=20,
        easier="leave each card in plain sight and walk with the children to each spot.",
        harder="for 5–6-year-olds, hide the cards properly and add the Great Pudding Heist straight afterwards.",
        related=[("The Great Pudding Heist", "printable/the-great-pudding-heist/", "next step up, ages 6+"), ("Certificate maker", "tools/certificate-maker/", "print a ‘You saved Christmas’ certificate")],
        audience="Ages 3–5")

    # ======================================================= PRINTABLE: CARE HOMES
    printable_game(
        slug="christmas-memory-lane", name="Christmas Memory Lane",
        h1="Christmas Memory Lane: a seated escape room for care homes and older adults",
        title="Christmas Escape Room for Care Homes & Older Adults – Free Large-Print Activity",
        description="A free large-print Christmas escape room for care home residents and older adults. Seated, 20–30 minutes, gentle festive puzzles that spark memories. Run by one activity coordinator.",
        answer="Christmas Memory Lane is a free large-print Christmas escape room for care home residents and older adults. Played seated around a table, a host reads gentle festive puzzles aloud, and each answer earns a letter or number to open the ‘Christmas box’. It takes 20–30 minutes for groups of 3–10.",
        spec=[("Who for", "Care home residents, day centres, older relatives at home"), ("Players", "3–10, seated"), ("Time", "20–30 minutes"), ("Set-up", "5 minutes"), ("Difficulty", "Gentle"), ("Format", "Large print (18pt+), host reads aloud, no moving around"), ("You need", "Printer, a box or tin with a treat inside (mince pies work well)")],
        story="Father Christmas has locked his box of treats and lost the code. Residents help him by remembering Christmases past. Every round earns part of the code word, and the box opens when the word is complete. The rounds are designed to start conversations as much as to be solved.",
        cards=[
            {"title": "Round 1: Christmas memories", "intro": "Host: read each question aloud. Write the FIRST LETTER of each answer in the boxes.", "type": "five gentle festive questions; first letters spell a word.",
             "html": '<div class="big-print"><ol><li>What do we pull at Christmas dinner that goes <em>bang</em> and has a paper hat inside?</li><li>What sits at the very top of many Christmas trees, with wings?</li><li>Which reindeer has a very shiny red nose?</li><li>Which round fruit was often found in the toe of a Christmas stocking?</li><li>What do we hang on the tree that twinkle and glow?</li></ol><div class="puzzle-box">☐ ☐ ☐ ☐ ☐</div></div>',
             "hide": "Read aloud at the table.", "answer": "CAROL", "explain": "Cracker, Angel, Rudolph, Orange, Lights."},
            {"title": "Round 2: Sing it out", "intro": "Host: the code word from Round 1 is a clue. Ask everyone to sing a favourite one together!", "type": "a group sing-along.",
             "html": '<div class="big-print"><p>Your word was a <strong>CAROL</strong>.</p><p>Sing one together, such as <em>Silent Night</em>, <em>Hark! The Herald Angels Sing</em> or <em>O Come, All Ye Faithful</em>.</p><p>Then count: how many words are in the title of the carol you sang? That is your first number.</p></div>',
             "hide": "Read aloud.", "answer": "Number of words in the carol title", "explain": "E.g. Silent Night = 2. Any answer works; write it down."},
            {"title": "Round 3: The Twelve Days", "intro": "Host: read each line aloud. These come from the old carol “The Twelve Days of Christmas”.", "type": "counting with the Twelve Days of Christmas.",
             "html": '<div class="big-print"><p>How many…</p><ol><li>…calling birds?</li><li>…gold rings?</li><li>…French hens?</li></ol><p>Add them together for your second number.</p></div>',
             "hide": "Read aloud.", "answer": "12", "explain": "4 calling birds + 5 gold rings + 3 French hens = 12. Sing the song to help."},
        ],
        finale={"title": "The Christmas box is open!", "html": '<div class="pic">🎁🥧☕</div><p class="big-print" style="text-align:center">Well done, everyone! Father Christmas says thank you.<br>Time for a mince pie and a cup of tea.</p>',
                "hide": "In the box with the treats. Open it when the group has the word CAROL and both numbers.", "setup": "Put the treats and the final card in a box or tin in the middle of the table."},
        faq=[("Can you do an escape room in a care home?", "Yes. Christmas Memory Lane is designed for care homes: it’s seated, large print and read aloud by one host, with gentle questions that bring back Christmas memories. It takes 20–30 minutes."),
             ("Is it suitable for residents with dementia?", "Many groups with mild memory loss enjoy it because the questions are about long-held Christmas traditions. Go at the group’s pace, give plenty of prompts and celebrate every answer. Activity staff know their residents best."),
             ("How many people can play?", "3–10 residents around one table works best. For larger lounges, split into two tables with a staff member each."),
             ("What do I need?", "A printer, a box or tin, and a treat such as mince pies. Print the cards in large print; they are already set at a bigger size.")],
        ages_min=60, players=(3, 10), minutes=30,
        easier="give multiple-choice options for each question (for example, “Cracker, candle or card?”).",
        harder="add your own local memories, such as the town’s Christmas lights or a well-known shop window display.",
        related=[("Christmas riddles with answers", "how-to/christmas-riddles-with-answers/", "more gentle puzzles to read aloud"), ("Certificate maker", "tools/certificate-maker/", "print certificates for residents")],
        audience="Care homes")

    # ======================================================= ADVENT CALENDAR
    build_advent()
    build_riddles()


WORDS = ["SNOWMAN", "REINDEER", "STOCKING", "TINSEL", "PRESENTS", "CRACKER", "ICICLE", "TURKEY", "HOLLY", "ANGEL", "SLEIGH", "ROBIN",
         "CANDLE", "WREATH", "CAROLS", "ELVES", "PUDDING", "SANTA", "MISTLETOE", "JINGLE", "FROSTY", "BAUBLE", "GIFTS", "YULE LOG"]


def advent_clue(day, L):
    t = day % 4
    if t == 0 or (t == 1 and L == "A"):
        return f"Write the letter for number <b>{ALPHA.index(L)+1}</b> (A = 1, B = 2…).", "number code"
    if t == 1:
        return f"Which letter comes straight <b>after {ALPHA[ALPHA.index(L)-1]}</b> in the alphabet?", "alphabet order"
    if t == 2 and L != "Z":
        return f"Which letter comes straight <b>before {ALPHA[ALPHA.index(L)+1]}</b> in the alphabet?", "alphabet order"
    for w in WORDS:
        if L in w:
            blank = w.replace(L, "_", 1)
            return f"Fill the gap in this festive word: <b>{blank}</b>", "missing letter"
    return f"Write the letter for number <b>{ALPHA.index(L)+1}</b>.", "number code"


def build_advent():
    msg = "SEASONSGREETINGSTOYOUALL"
    assert len(msg) == 24
    slug = "advent-calendar"; path = f"printable/{slug}/"
    days = ""
    key = []
    for d, L in enumerate(msg, start=1):
        clue, typ = advent_clue(d, L)
        days += f'<div class="day"><b>{d} December</b>{clue}<br><span style="color:#5d574d">Letter: ____</span></div>'
        key.append(f"{d}: {L}")
    from games_lib import gumroad_button
    faq = [("What is an escape room advent calendar?", "It’s one small puzzle a day from 1 to 24 December. Each puzzle gives one letter, and on Christmas Eve the 24 letters spell a secret festive message."),
           ("What age is it for?", "Ages 5–9 can do it with a little help; it takes about 2 minutes a day. Older children can race to solve it before the 24th."),
           ("How do I use it?", "Print the page, cut out each day (or fold it) and reveal one a day, or keep the sheet on the fridge and fill in one box each morning."),
           ("Is there an answer key?", "Yes, at the bottom of this page behind a ‘show answers’ button.")]
    body = f"""
<div class="wrap narrow">
<p class="eyebrow">Printable · Free · Advent</p>
<h1>Christmas escape room advent calendar: 24 free printable puzzles</h1>
{byline()}
<p class="answer">This free printable advent calendar gives children one tiny puzzle a day from 1 to 24 December. Each puzzle reveals one letter, and on Christmas Eve the 24 letters spell a secret festive message. Each day takes about 2 minutes and suits ages 5–9.</p>
{spec_table([("Ages", "5–9"), ("Players", "1–4"), ("Time", "About 2 minutes a day, 1–24 December"), ("Set-up", "Print one page"), ("Puzzles", "24: number codes, alphabet order and missing letters"), ("You need", "Printer, pencil; scissors optional")])}
<div class="btn-row no-print"><button class="btn" data-print>Print the calendar</button>{gumroad_button(slug)}</div>
<p id="print-note" class="callout no-print" hidden>If nothing happened, press <strong>Ctrl + P</strong> or <strong>⌘ + P</strong>.</p>
<h2 class="no-print">How it works</h2>
<ol class="steps no-print"><li>Print the calendar and pin it to the fridge.</li><li>Each morning, solve that day’s puzzle and write the letter in the box.</li><li>On 24 December, read all 24 letters in order to reveal the secret message.</li></ol>
<div class="print-only"><h1>Christmas Escape Room Advent Calendar</h1><p>christmasescaperoom.co.uk</p></div>
</div>
<div class="wrap"><div class="daygrid">{days}</div>
<div class="day" style="margin-top:14px;text-align:center"><b>Secret message</b><span style="letter-spacing:.3em">_ _ _ _ _ _ _ &nbsp; _ _ _ _ _ _ _ _ _ &nbsp; _ _ &nbsp; _ _ _ &nbsp; _ _ _</span></div></div>
<div class="wrap narrow no-print">
<h2>Answers</h2>
<button class="btn ghost small" id="reveal">Show answers</button>
<div id="ans-list" hidden><p>{' · '.join(key)}</p><p>The message is <strong>SEASON’S GREETINGS TO YOU ALL</strong>.</p></div>
{faq_html(faq)}
<h2>Try next</h2><ul><li><a href="../the-great-pudding-heist/index.html">The Great Pudding Heist</a>: for Christmas Day itself</li><li><a href="../../tools/christmas-cipher-maker/index.html">Make your own coded advent messages</a></li></ul>
</div>
<script>document.getElementById('reveal').onclick=function(){{document.getElementById('ans-list').hidden=false;this.hidden=true}}</script>"""
    schema = {"@type": ["Game", "CreativeWork"], "name": "Christmas Escape Room Advent Calendar", "url": DOMAIN + "/" + path,
              "description": "24 free printable advent puzzles that spell a secret message by Christmas Eve.", "isAccessibleForFree": True,
              "inLanguage": "en-GB", "typicalAgeRange": "5-9", "author": {"@id": PERSON_ID}, "image": f"{DOMAIN}/assets/og/{slug}.png"}
    page(path, "Christmas Escape Room Advent Calendar – 24 Free Printable Puzzles",
         "Free printable Christmas escape room advent calendar: one 2-minute puzzle a day from 1–24 December that spells a secret message. Ages 5–9. Answers included.",
         body, crumbs=[("Printable", "printable/"), ("Advent calendar", path)], schema=[schema, faq_schema(faq)], active="Printable", og_image=f"assets/og/{slug}.png")


RIDDLES = {
    "Easy riddles for kids (ages 5–8)": [
        ("I have needles but I never sew. I wear lights and baubles in a row. What am I?", "A Christmas tree"),
        ("I’m cold and white and fall from the sky. Roll me up and I’ll grow to be big. What am I?", "Snow"),
        ("I hang by the fireplace and get filled on Christmas Eve. What am I?", "A stocking"),
        ("I have a red nose that glows so bright, I help pull the sleigh on Christmas night. Who am I?", "Rudolph"),
        ("Pull me and I go bang! Inside you’ll find a joke and a paper hat. What am I?", "A Christmas cracker"),
        ("I’m round and shiny and hang on the tree. Drop me and I might break. What am I?", "A bauble"),
        ("I have a carrot for a nose and coal for eyes, and I melt when the sun comes out. Who am I?", "A snowman"),
        ("I’m wrapped in paper with a bow on top, and you open me on Christmas morning. What am I?", "A present"),
        ("I’m made of biscuit, I have buttons of sweets, and I live in a house you can eat. Who am I?", "A gingerbread man"),
        ("I’m tall when I’m new and short when I’m old, and I glow on the Christmas table. What am I?", "A candle"),
    ],
    "Medium riddles for older kids (ages 9–12)": [
        ("What can go up a chimney down, but can’t go down a chimney up?", "An umbrella"),
        ("What has bark but no bite, and stands in your living room in December?", "A Christmas tree"),
        ("I start with E, end with E, and usually contain only one letter. You send lots of me at Christmas.", "An envelope"),
        ("The more of me you make in the snow, the more you leave behind. What am I?", "Footprints"),
        ("What gets wetter the more it dries, especially after Christmas dinner washing-up?", "A tea towel"),
        ("What falls in winter but never gets hurt?", "Snow"),
        ("I have hands but can’t wrap presents, and I tell you when it’s time for bed on Christmas Eve. What am I?", "A clock"),
        ("I have one eye but I can’t see, and I help sew up a stocking. What am I?", "A needle"),
        ("What goes up every year but never comes down?", "Your age"),
        ("What can travel all the way to the North Pole while staying in the corner of an envelope?", "A stamp"),
    ],
    "Hard riddles for teens and adults": [
        ("Feed me and I live, give me a drink and I die. I keep you warm on Christmas Eve. What am I?", "A fire"),
        ("I can be cracked, made, told and played, and you’ll find one in every cracker. What am I?", "A joke"),
        ("What breaks as soon as you say its name? (Hint: think of a famous carol.)", "Silence"),
        ("I have cities but no houses, forests but no trees, and water but no fish. Santa needs me on Christmas Eve.", "A map"),
        ("What can you catch every winter but never throw?", "A cold"),
        ("What has many keys but can’t open a single lock, and plays carols?", "A piano"),
        ("If there are three mince pies and you take two, how many do you have?", "Two"),
        ("What has a neck but no head and wears a cork at Christmas?", "A bottle"),
        ("What has four legs but can’t walk, and everyone gathers round it for Christmas dinner?", "A table"),
        ("I’m full of holes but I still hold water, and I’m busy after Christmas dinner. What am I?", "A sponge"),
    ],
}


def build_riddles():
    path = "how-to/christmas-riddles-with-answers/"
    sections = ""
    qas = []
    n = 0
    for head, items in RIDDLES.items():
        lis = ""
        for q, a in items:
            n += 1
            lis += f"<details><summary>{n}. {q}</summary><p><strong>Answer:</strong> {a}</p></details>"
            qas.append((q, a))
        sections += f"<h2>{head}</h2><div class=\"faq\">{lis}</div>"
    faq = [("What are good Christmas riddles for an escape room?", "Riddles with a hiding place as the answer work best: ‘I have needles but never sew’ (the tree), ‘I hang by the fireplace’ (a stocking) or ‘Pull me and I go bang’ (a cracker). Put the next clue in that place."),
           ("How do I use these riddles in an escape room?", "Pick a riddle whose answer is an object in your home, write it on a card and hide the next clue there. Mix riddles with codes from our cipher maker for variety."),
           ("Are these riddles suitable for a classroom?", "Yes. Use the easy set for KS1, the medium set for KS2 and the hard set for secondary school or staff quizzes.")]
    body = f"""
<div class="wrap narrow">
<p class="eyebrow">Riddles</p>
<h1>30 Christmas riddles with answers (for kids, teens and adults)</h1>
{byline()}
<p class="answer">Here are 30 Christmas riddles with answers, sorted into easy (ages 5–8), medium (9–12) and hard (teens and adults). Tap a riddle to reveal its answer. Riddles whose answer is a place, such as a stocking or the tree, make perfect escape room clues.</p>
{sections}
<h2>Using riddles in a Christmas escape room</h2>
<ol class="steps"><li>Choose a riddle whose answer is a hiding place in your home.</li><li>Write it on a card and hide the next clue in that place.</li><li>Mix in a code from the <a href="../../tools/christmas-cipher-maker/index.html">Christmas cipher maker</a> and finish with a prize.</li></ol>
<p>Want it done for you? Try <a href="../../printable/the-great-pudding-heist/index.html">The Great Pudding Heist</a> or read <a href="../make-a-christmas-escape-room/index.html">how to make a Christmas escape room</a>.</p>
{faq_html(faq)}
</div>"""
    from layout import article_schema
    page(path, "30 Christmas Riddles with Answers – Kids, Teens & Adults | Christmas Escape Room",
         "30 Christmas riddles with answers, sorted by age: easy for kids, medium for 9–12s and hard for teens and adults. Perfect for escape rooms, crackers and classrooms.",
         body, crumbs=[("Christmas riddles with answers", path)],
         schema=[article_schema(path, "30 Christmas riddles with answers", "Christmas riddles sorted by age, with answers."), faq_schema(faq)], active="How to", og_image="assets/og/christmas-riddles-with-answers.png")
