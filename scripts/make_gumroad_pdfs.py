import asyncio, os, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = (ROOT / 'docs').as_uri()
from playwright.async_api import async_playwright
JS="""()=>{for(const id of ['guide','answer-key']){const e=document.getElementById(id);if(e){e.classList.remove('no-print');e.querySelectorAll('.btn-row,#print-note').forEach(x=>x.remove())}}
const k=document.getElementById('answer-key'); if(k){k.style.breakBefore='page'}
const a=document.getElementById('ans-list'); if(a){a.hidden=false; a.classList.remove('no-print'); a.parentElement.classList.remove('no-print');
 a.parentElement.querySelectorAll('.faq,ul,#reveal,h2:not(:first-of-type)').forEach(x=>x.remove())}
document.querySelectorAll('.clue-card .hide-where').forEach(x=>x.remove());
const s=document.createElement('style');s.textContent='@media print{.answer,.spec{display:block} .print-only h1{font-size:28pt} h2{break-after:avoid}}';document.head.appendChild(s);
const foot=document.createElement('p');foot.className='print-only';foot.innerHTML='Free online games, tools and more printables at <b>christmasescaperoom.co.uk</b> · © 2026 Paul, Christmas Escape Room. Free for home, school and care-home use.';document.querySelector('main').appendChild(foot);}"""
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path=os.environ.get('CHROME_PATH') or None,args=['--no-sandbox']);pg=await b.new_page()
    for slug in ["the-great-pudding-heist","scrooges-safe","elf-academy-final-exam","rudolphs-lost-bells","christmas-memory-lane","advent-calendar","christmas-eve","boxing-day","new-years-eve","ks2-classroom"]:
      await pg.goto(f'{DOCS}/printable/{slug}/index.html');await pg.evaluate(JS)
      await pg.emulate_media(media='print')
      await pg.pdf(path=f'{ROOT}/gumroad/{slug}.pdf',format='A4',print_background=True,margin={'top':'14mm','bottom':'14mm','left':'14mm','right':'14mm'})
      await pg.emulate_media(media='screen')
    await b.close()
asyncio.run(main())
