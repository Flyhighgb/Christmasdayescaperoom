import asyncio, os, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = (ROOT / 'docs').as_uri()
from playwright.async_api import async_playwright
ITEMS=[("default","Free Christmas escape rooms","Play online or print at home","🎄🔑"),
("the-missing-sleigh-key","The Missing Sleigh Key","Free online Christmas escape room · Ages 8+ · 20–30 min","🔑🎅"),
("office-party-escape","The Office Party Escape","Free online team game for work Christmas parties","🥧🎉"),
("the-great-pudding-heist","The Great Pudding Heist","Free printable Christmas escape room · Ages 6+","🍮🧝"),
("scrooges-safe","Scrooge’s Safe","Free printable Christmas escape room for adults","🗝️🕯️"),
("elf-academy-final-exam","Elf Academy Final Exam","Christmas escape room for teenagers · Free printable","🎓🧝"),
("rudolphs-lost-bells","Rudolph’s Lost Bells","Picture escape room for toddlers · Ages 3–5","🔔🦌"),
("christmas-memory-lane","Christmas Memory Lane","Large-print escape room for care homes","☕🎁"),
("advent-calendar","Escape Room Advent Calendar","24 free printable puzzles · 1–24 December","📅⭐"),
("christmas-riddles-with-answers","30 Christmas Riddles","With answers · for kids, teens and adults","❓🎄")]
def html(t,sub,emo,w,h):
    big = h>w
    return f"""<html><body style="margin:0;width:{w}px;height:{h}px;background:radial-gradient(900px 500px at 80% 0%,#1f5a49,transparent 60%),#0c2a22;font-family:Georgia,serif;color:#fff;display:flex;flex-direction:column;justify-content:center;padding:0 70px;box-sizing:border-box;position:relative;overflow:hidden">
<div style="position:absolute;inset:0;opacity:.35;background-image:radial-gradient(#fff 1.4px,transparent 1.7px),radial-gradient(#fff 1px,transparent 1.3px);background-size:90px 90px,140px 140px;background-position:0 0,40px 60px"></div>
<div style="position:relative">
<div style="font-size:{170 if big else 110}px;line-height:1.1">{emo}</div>
<div style="font:700 {26 if big else 22}px system-ui;letter-spacing:.14em;color:#c9a24a;margin:20px 0 10px">FREE · NO SIGN-UP</div>
<div style="font-weight:700;font-size:{96 if big else 72}px;line-height:1.05">{t}</div>
<div style="font:400 {40 if big else 32}px system-ui;color:#e9e1cf;margin-top:24px;line-height:1.3">{sub}</div>
<div style="margin-top:{60 if big else 36}px;display:inline-block;background:#b3263a;padding:14px 26px;border-radius:999px;font:600 {32 if big else 26}px system-ui">christmasescaperoom.co.uk</div>
</div></body></html>"""
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(args=['--no-sandbox'])
    pg=await b.new_page()
    for slug,t,sub,e in ITEMS:
      for w,h,folder in [(1200,630,'og'),(1000,1500,'pins')]:
        await pg.set_viewport_size({'width':w,'height':h});await pg.set_content(html(t,sub,e,w,h))
        await pg.screenshot(path=f'{ROOT}/docs/assets/{folder}/{slug}.png')
    await b.close()
asyncio.run(main())
