# Builds index.html from the content below. Run: python3 build/make.py
import html, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = html.escape
CV = 'assets/Ishani-Handa-CV.pdf'
EMAIL = 'ishanihanda1709@gmail.com'
LINKEDIN = 'https://www.linkedin.com/in/ishani-handa'

# ---------- stroke icons (currentColor) ----------
ICONS = {
 'home': '<path d="M4 11 12 4l8 7v9h-5v-6H9v6H4Z"/>',
 'search': '<circle cx="11" cy="11" r="6.5"/><path d="m20 20-4.2-4.2"/>',
 'bag': '<path d="M5 8h14l-1 12H6Z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>',
 'route': '<circle cx="6" cy="18" r="2.4"/><circle cx="18" cy="6" r="2.4"/><path d="M8.4 18H15a3 3 0 0 0 0-6H9a3 3 0 0 1 0-6h6.6"/>',
 'grid': '<rect x="4" y="4" width="7" height="7" rx="1.5"/><rect x="13" y="4" width="7" height="7" rx="1.5"/><rect x="4" y="13" width="7" height="7" rx="1.5"/><rect x="13" y="13" width="7" height="7" rx="1.5"/>',
 'sparkle': '<path d="M12 3c.6 4.6 2.4 6.4 7 7-4.6.6-6.4 2.4-7 7-.6-4.6-2.4-6.4-7-7 4.6-.6 6.4-2.4 7-7Z"/>',
 'ruler': '<path d="M3 15 15 3l6 6L9 21Z"/><path d="m7 11 2 2M10 8l2 2M13 5l2 2M5 13l1.5 1.5"/>',
 'check': '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
 'plus': '<path d="M12 5v14M5 12h14"/>',
 'down': '<path d="m6 9 6 6 6-6"/>',
 'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
 'moon': '<path d="M19.5 14.5A8 8 0 0 1 9.5 4.5a8 8 0 1 0 10 10Z"/>',
 'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2.5M12 19v2.5M2.5 12H5M19 12h2.5M5.3 5.3l1.8 1.8M16.9 16.9l1.8 1.8M5.3 18.7l1.8-1.8M16.9 7.1l1.8-1.8"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m3.5 6.5 8.5 7 8.5-7"/>',
 'download': '<path d="M12 4v11M7 10.5l5 5 5-5M4.5 20h15"/>',
 'x': '<path d="M6 6l12 12M18 6 6 18"/>',
 'truck': '<path d="M2.5 6.5h11v10h-11Z"/><path d="M13.5 10h4l3 3.5v3h-7"/><circle cx="6.5" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
 'chart': '<path d="M4 20V4M4 20h16"/><path d="m7.5 15 3.5-4 3 2.5 5-6.5"/>',
 'users': '<circle cx="9" cy="8.5" r="3.2"/><path d="M3 20c.5-3.5 3-5.5 6-5.5s5.5 2 6 5.5"/><circle cx="17" cy="9" r="2.5"/><path d="M16.5 14.6c2.6.2 4.2 2 4.5 5"/>',
 'rocket': '<path d="M12 15c-2-2-2.5-4-2.5-4S11 4.5 18.5 3.5C17.5 11 11 12.5 11 12.5"/><path d="M9.5 11 6 11.5 4 14.5l4 .5M13 14.5l-.5 3.5-3 2-.5-4"/><circle cx="15" cy="7" r="1.2"/>',
 'bolt': '<path d="M13 3 5 13.5h6L10 21l8-10.5h-6Z"/>',
 'gift': '<rect x="3.5" y="8.5" width="17" height="4" rx="1"/><path d="M5 12.5v8h14v-8M12 8.5v12M12 8.5C10 4 6.5 5 7.5 7.5c.5 1 2.5 1 4.5 1Zm0 0c2-4.5 5.5-3.5 4.5-1-.5 1-2.5 1-4.5 1Z"/>',
 'video': '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="m16 10 5-3v10l-5-3"/>',
 'img': '<rect x="3.5" y="4.5" width="17" height="15" rx="2.5"/><circle cx="9" cy="10" r="1.8"/><path d="m4 18 5.5-5 4 3.5 2.5-2 4 3.5"/>',
 'doc': '<path d="M6 3.5h8l4 4v13H6Z"/><path d="M14 3.5v4h4M9 12.5h6M9 16h6"/>',
 'ext': '<path d="M8 16 16 8M9 8h7v7"/>',
 'calendar': '<rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
 'star': '<path d="m12 3.5 2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8-4.3-4.1 5.9-.9Z"/>',
}
def ic(name, cls='ic'):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'

# ---------- the five KRAs from the JD, as "fabric technologies" ----------
FAB = {
 'brand':   ('BrandWeave',  'Brand Strategy & Marketing'),
 'creator': ('CreatorKnit', 'Influencer Marketing'),
 'growth':  ('GrowthFlex',  'Growth & Execution'),
 'npd':     ('NewCut',      'New Product Development'),
 'founder': ('FounderFit',  'Founder’s Office & Strategy'),
}

# garment tones for the generated product packs: (background, text)
TONES = [('#24262b', '#f4f1ea'), ('#1f2a44', '#f4f1ea'), ('#d9cdb8', '#1d1b18'), ('#4a5240', '#f4f1ea'),
         ('#5a2632', '#f6efe9'), ('#e8e2d6', '#1d1b18'), ('#46566a', '#f4f1ea'), ('#8c7f6c', '#fbf8f2')]

# ---------- products ----------
ALL = {}
def p(pid, title, stat, unit, tag, desc, fab=(), img=None, pos='50% 40%', media=None, link=None, best=False, new=False):
    assert pid not in ALL, pid
    d = dict(id=pid, title=title, stat=stat, unit=unit, tag=tag, desc=desc, fab=list(fab), img=img, pos=pos,
             media=media or [], link=link, best=best, new=new)
    ALL[pid] = d
    return d

def price_html(stat, unit):
    if '→' in stat:
        a, b = [s.strip() for s in stat.split('→')]
        return f'<s>{E(a)}</s> <b>{E(b)}</b> <span>{E(unit)}</span>'
    return f'<b>{E(stat)}</b> <span>{E(unit)}</span>'

def media_html(m):
    out = []
    for kind, src, cap, *rest in m:
        if kind == 'img':
            out.append(f'<a class="m-img" href="assets/{src}" target="_blank" rel="noopener"><img src="assets/{src}" alt="{E(cap)}" loading="lazy"><small>{E(cap)}</small></a>')
        else:
            out.append(f'<figure class="m-vid"><video controls muted playsinline preload="none" poster="assets/{rest[0]}"><source src="assets/{src}" type="video/mp4"></video><figcaption>{E(cap)}</figcaption></figure>')
    return f'<div class="m-row">{"".join(out)}</div>' if out else ''

def visual(d, n, col):
    if d['img']:
        return f'<img src="assets/{d["img"]}" alt="" loading="lazy" style="object-position:{d["pos"]}">'
    bg, fg = TONES[n % len(TONES)]
    long = ' long' if len(d['stat']) > 8 else ''
    return (f'<span class="pack{long}" style="--pb:{bg};--pf:{fg}"><small>DaISHANI · {E(col)}</small>'
            f'<b>{E(d["stat"])}</b><em>{E(d["unit"])}</em><i class="pack-seam"></i></span>')

def prod_html(n, d, col):
    fabs = ' · '.join(FAB[f][0] for f in d['fab'])
    badge = '<span class="badge">Bestseller</span>' if d['best'] else ('<span class="badge new">New</span>' if d['new'] else '')
    has = ''.join(ic({'img': 'img', 'vid': 'video'}[k], 'ic s') for k in sorted({k for k, *_ in d['media']}))
    if d['link']: has += ic('doc' if d['link'][1].endswith('.pdf') else 'ext', 'ic s')
    link = ''
    if d['link']:
        ext = '' if d['link'][1].startswith('#') else ' target="_blank" rel="noopener"'
        link = f'<a class="pd-link" href="{d["link"][1]}"{ext}>{E(d["link"][0])} {"↓" if d["link"][1].startswith("#") else "↗"}</a>'
    chips = ''.join(f'<span class="chip f-{f}">{FAB[f][0]}<small>{FAB[f][1]}</small></span>' for f in d['fab'])
    return f'''<article class="prod" id="p-{d["id"]}" data-id="{d["id"]}" data-title="{E(d["title"])}" data-stat="{E(d["stat"])}" data-col="{E(col)}" data-fab="{" ".join(d["fab"])}" data-search="{E((d["title"]+" "+d["tag"]+" "+col+" "+fabs).lower())}">
<button class="prod-img" type="button" data-qv="{d["id"]}" aria-label="Quick view: {E(d["title"])}">{visual(d, n, col)}{badge}<span class="qv-hint">Quick view</span></button>
<div class="prod-info"><p class="prod-fab">{fabs or "Foundation"}</p><h4><button type="button" data-qv="{d["id"]}">{E(d["title"])}</button></h4>
<p class="prod-tag">{E(d["tag"])} <span class="has">{has}</span></p><p class="price">{price_html(d["stat"], d["unit"])}</p></div>
<button class="add" type="button" aria-pressed="false" aria-label="Add “{E(d["title"])}” to your hire bag">{ic("plus","ic s ip")}{ic("check","ic s ok")}<span class="add-t">Add to bag</span></button>
<div class="pd" hidden><div class="pd-chips">{chips}</div><p>{d["desc"]}</p>{media_html(d["media"])}{link}</div>
</article>'''

# ======================= CONTENT =======================
COLS = []
def col(**k): COLS.append(k)

col(id='school', no='01', name='The Foundation Edit', where='D.A.V Public School', years='2018–20', place='Gurugram',
  cover='cover-school.webp', short='D.A.V',
  desc='Where it started: commerce, a first taste of leadership, and an early habit of planning backwards from a deadline.',
  hl=[('94.4%', 'Class X, CBSE'), ('87.8%', 'Class XII, Commerce'), ('Top 10%', 'of the cohort')],
  items=[
   p('sc-12', 'Class XII, Commerce', '87.8%', 'CBSE', 'Top 10% of the cohort',
     'Where business first made sense to me: accounts, economics and business studies. The start of thinking in numbers.', best=True),
   p('sc-10', 'Class X', '94.4%', 'CBSE', 'All-round foundation',
     'A strong all-round foundation, and an early habit of planning backwards from a deadline.'),
   p('sc-pre', 'Prefect of the House', 'Prefect', 'leadership', 'House events',
     'My first taste of coordinating people towards one outcome: house events, schedules and a lot of follow-ups.', fab=['founder']),
  ])

col(id='christ', no='02', name='The Marketing Basics', where='Christ University', years='2020–23', place='Bengaluru',
  cover='cover-christ.webp', short='Christ',
  desc='A BBA Honours in Marketing, a marketing club to run and two agency internships. This is where I learned why people choose, buy and come back.',
  hl=[('3.67 / 4', 'First Class with Distinction'), ('Vice-President', 'NICHE, the marketing club'), ('2 agencies', 'Foxymoron · Arting Out Loud')],
  items=[
   p('ch-bba', 'BBA Honours in Marketing', '3.67/4', 'CGPA', 'First Class with Distinction',
     'Consumer behaviour, marketing research, brand management and marketing analytics: a framework for understanding <b>why people choose, buy and come back</b>. In a category where people rarely switch once they find their fit, that last part is the whole game.', fab=['brand'], best=True),
   p('ch-foxy-gtm', 'Foxymoron: pitch & positioning for 5+ brands', 'Up to 20%', 'engagement lift', 'DS Group · Kingfisher · Revv',
     'Shaped pitch and positioning for brands like DS Group through market research and competitive analysis, and lifted engagement by up to 20% with social strategy recommendations for Kingfisher and Revv Cars.', fab=['brand'], best=True),
   p('ch-foxy-btl', 'Foxymoron: on-ground activation, “Grab the Pulse”', '1,000+', 'shoppers engaged', 'Agency internship',
     'Executed an on-ground activation at DLF Mall of India for a brand, from the floor plan to the footfall. Hands-on BTL experience.', fab=['brand']),
   p('ch-aol', 'Arting Out Loud: content built on customer voice', '30%', 'reach growth', 'Social media internship',
     'Grew campaign reach by 30% by building the content strategy around what customers said and which posts performed best, and kept 5+ client accounts publishing on schedule with 20+ posts.', fab=['brand', 'creator']),
   p('ch-niche', 'Vice-President, NICHE', 'VP', 'marketing club', 'Events on schedule',
     'Ran the Events Department operations behind workshops, conferences and marketing fests, and led content strategy and social branding for the club. My first calendar of campaigns, with real deadlines.', fab=['brand', 'founder']),
   p('ch-lit', 'Literary Committee · Program Coordinator', 'Community', 'cross-college', '2021 – 2023',
     'Ran outreach for literary events and grew a cross-college community of student writers. My first time finding people, getting them to show up, and getting them to come back.', fab=['creator']),
   p('ch-study', 'Research: content and buying decisions', '100', 'survey responses', 'IBM SPSS',
     'An academic study on how content marketing shapes customer buying decisions in banking. I analysed 100 survey responses in IBM SPSS to find which content formats sway buyers most.', fab=['brand']),
   p('ch-ymad', 'Volunteer, Youth Making a Difference', '200+', 'learners', 'Community',
     'Taught Maths and Science online to 200+ learners in Grades 5–8 during Covid, and led food-basket distribution to 20+ families.'),
  ])

col(id='phonepe', no='03', name='The Growth Collection', where='PhonePe', years='2023–25', place='Bengaluru',
  cover='cover-phonepe.webp', short='PhonePe',
  desc='Two years: Associate Campaign Manager from June 2023, then Campaign Manager from December 2024. I planned and ran brand campaigns on PhonePe’s in-app inventory, owned monthly revenue for 30+ brands, and kept 93% of them coming back.',
  hl=[('₹2 Cr+ / month', 'across 30+ brands'), ('100% of AOP', 'annual operating plan'), ('Up to 4×', 'ROAS, to end-funnel'), ('93%', 'brands came back')],
  items=[
   p('pp-aop', 'Revenue owned, plan delivered', '₹2 Cr+', '/ month', '100% of annual plan',
     'Owned monthly revenue for a 30+ brand portfolio including Myntra, Amazon and Netflix, planning month by month against the annual operating plan and delivering all of it.', fab=['growth'], best=True),
   p('pp-ctr', 'New formats, new CTR', '0.2% → 1.5%', 'CTR', 'GIF · Dual CTA · Video · Animation',
     'Co-created new ad formats like live score and dual-CTA with design teams, and owned the GIF, Dual CTA and Payment Innovation formats from pilot to live. CTR went from 0.2% to 1.5%, and 4 new formats joined the inventory through SOPs I wrote.',
     fab=['growth', 'npd'], img='cover-thunder.webp', pos='50% 30%',
     media=[('vid', 'thunderbolts.mp4', 'Marvel’s Thunderbolts*: payment animation, then the movie banner', 'thunder-poster.jpg')], best=True),
   p('pp-roas', 'ROAS that holds down the funnel', 'Up to 4×', 'ROAS', 'Lakmé · Country Delight',
     'Raised ROAS up to 4× for Lakmé and Country Delight by tracking CAC and end-funnel conversion, not just clicks, and improving the steps where users dropped off.', fab=['growth'], best=True),
   p('pp-10x', 'Slot-level RCA → 10× growth', '10×', 'key-account growth', 'Spend moved to what converts',
     'A slot-level root-cause analysis showed which banner and widget slots were actually converting. Moving spend to those slots drove 10× growth in a key account.', fab=['growth', 'founder']),
   p('pp-ret', 'Partners who come back', '93%', 'brands retained', 'Repeat campaigns',
     'Used past campaign insights to sharpen planning and targeting for the next flight, so 93% of brands came back for repeat campaigns.', fab=['growth']),
   p('pp-jio', 'JioHotstar: a live score after every payment', 'IPL', 'real-time campaign', 'Live data · Contextual creative',
     'Brought the cricket match into a familiar touchpoint. The score updated from a scoring-platform API, and contextual messages changed on wickets and sixes. I owned the campaign, live creative execution and cross-functional coordination.',
     fab=['brand', 'growth'], img='cover-jio.webp', pos='50% 35%',
     media=[('img', 'cricket-phone-live.webp', 'The live score, updated from the scoring feed'), ('img', 'cricket-phone-moment.webp', 'A message tied to the match moment'),
            ('vid', 'jiohotstar-launch.mp4', 'JioHotstar launch video banner', 'jio-poster.jpg')]),
   p('pp-airtel', 'Airtel: a lead funnel that works', '3–4×', 'lead volume', 'Targeting · lead capture',
     'Achieved 3–4× lead volumes for Airtel by refining targeting and optimising each step of the lead-capture funnel.', fab=['growth']),
   p('pp-gif', 'Amazon Great Indian Festival launches', '10+', 'launches in under 2 days', 'Fashion · Beauty · Home',
     'Delivered 10+ launches in under 2 days during the festive peak, planning in-app placements and takeovers across banners, widgets and tiles so every category went live on time.', fab=['growth', 'founder']),
   p('pp-ab', 'A test for every assumption', '40%', 'engagement & efficiency', 'Creatives × cohorts',
     'Ran hypothesis-driven A/B tests on creatives and audience cohorts, then carried winning promotions from one category to another, lifting conversion across 5+ categories.', fab=['growth']),
   p('pp-24h', 'Go-live in a day, not two', '2 days → 24 hrs', 'launch turnaround', 'Automation',
     'Automated the repeat steps in the launch process, cutting campaign go-live time in half so changes reached the app while the moment was still on.', fab=['growth', 'founder']),
   p('pp-mis', 'An MIS that flags, not just reports', '30%', 'efficiency gain', 'Zero errors',
     'Built an Excel MIS and KPI dashboard on DCM and DV data that flagged spend, CTR and ROAS gaps for action in weekly reviews, improving efficiency by 30% with zero errors.', fab=['growth', 'founder']),
   p('pp-xfn', 'Design, Data Science, Sales, agencies', '10+', 'agencies, 100% on time', 'GroupM · Publicis',
     'Worked with design on new formats, with Data Science on retargeting segments for 10+ brands, with Sales on decks that helped close deals, and managed 10+ agencies like GroupM and Publicis with 100% on-time delivery.', fab=['founder', 'creator']),
   p('pp-mentor', 'Mentored new joiners', '6 months', 'weekly reviews', 'Playbooks',
     'Ran weekly reviews for new joiners over 6 months, which sped up their ramp-up.', fab=['founder']),
  ])

col(id='masters', no='04', name='The 0 → 1 Drop', where='Masters’ Union', years='2026–', place='Gurugram',
  cover='cover-slay.webp', short='MU',
  desc='The build year. A PGP in Technology & Business Management, where I test ideas in the market with real customers and real money: a D2C brand, an AI product and a Startup Weekend win.',
  hl=[('₹3L+', 'D2C revenue, Slay Pop Cult'), ('Winner', 'Startup Weekend, 25+ teams'), ('Live', 'postwire.in')],
  items=[
   p('mu-slay', 'Slay Pop Cult · Co-founder', '₹3L+', 'revenue', '350+ customers · ~50% margin',
     'A Gen Z D2C lifestyle and gifting brand, built from scratch. I curated the assortment, built a 4-market supplier base (Gujarat, Mumbai, Chandni Chowk, China), set prices and ran the pop-up stall. I also set up the Shopify storefront for the hero SKUs.',
     fab=['npd', 'founder', 'growth'], img='cover-slay.webp', pos='50% 40%', media=[('img', 'slay-stall.webp', 'Slay Pop Cult pop-up stall')], best=True),
   p('mu-oohlala', 'Oohlala Stories · D2C intimate-wear growth plan', 'GA4', 'traffic & conversion', '6-member team · presented to founders',
     'Built a growth plan for a D2C intimate-wear brand by analysing its GA4 traffic and conversion data, and presented the data-backed recommendations live to the founders. The closest thing on this page to DaMENSCH’s own category.', fab=['growth', 'founder'], best=True),
   p('mu-postwire', 'Postwire AI · Founder', 'Live', 'postwire.in', 'Built with Claude',
     'An AI writing tool that turns trending news into ready-to-post LinkedIn content. I built and launched it end to end with Claude, from news sourcing to post generation, designed around a time-poor professional who faces a blank page.',
     fab=['npd', 'founder'], img='cover-postwire.webp', pos='50% 50%', link=('Explore Postwire', 'https://postwire.in')),
   p('mu-sw', 'Winner, Startup Weekend', '1st', 'of 25+ teams', 'Pitch',
     'Won the Masters’ Union Startup Weekend against 25+ teams, pitching a venture for DINK couples.', fab=['founder']),
   p('mu-prolectro', 'Prolectro · GTM strategy (team)', '35%', 'repeat-purchase gate', '101-person survey',
     'A go-to-market plan for a clear protein and electrolyte sachet. We targeted “Lapsed Intenders”, proposed a ₹129 trial sachet with multipacks for the second purchase, and set a 35% repeat gate before expanding beyond Delhi NCR. <i>Academic team strategy; figures are proposals.</i>',
     fab=['npd', 'brand'], img='cover-prolectro.webp', pos='50% 30%', media=[('img', 'prolectro-product.webp', 'Prolectro product concept visual')], link=('Open the GTM deck (PDF)', 'assets/Prolectro-GTM-Strategy.pdf')),
   p('mu-grwm', 'In a creator’s shoes', 'GRWM', 'video', 'Nykaa case competition',
     'For the Nykaa case competition I produced a get-ready-with-me video myself. Making content, not just planning it, showed me how much effort one post takes for a creator.', fab=['creator'], link=('Watch the GRWM reel on Instagram', 'https://www.instagram.com/reel/Dd62qJpSbLI/')),
   p('mu-battery', 'Battery manufacturing · AI workflows', 'Closed-loop', 'AI design', 'Process study',
     'Mapped the battery value chain and connected scrap, long formation cycles and downtime to business performance, then outlined AI for defect detection and yield prediction, with a loop linking defects to causes and machine settings.',
     fab=['founder'], img='cover-battery.webp', pos='0% 50%', media=[('img', 'battery-ai-workflows.webp', 'AI opportunity mapping from the battery report')], link=('Read the report (PDF)', 'assets/Battery-Cell-Manufacturing.pdf')),
  ])

col(id='damensch', no='05', name='Made for DaMENSCH', where='Founder’s Office · Growth & Marketing', years='Next', place='The five KRAs, matched to proof',
  cover='cover-ishani.webp', short='DaMENSCH',
  desc='Your JD lists five KRAs. Each one is a fabric below, and every piece in this collection is real work woven from it. Use the fit guide to filter by KRA, and add anything you want to talk about to your bag.',
  hl=[('2 years', 'growing revenue at scale'), ('D2C', 'co-founded and sold'), ('Category-ready', 'intimate-wear growth plan'), ('AI-native', 'Postwire · this site')],
  items=[
   # brand
   p('dm-pos', 'Positioning, from the agency side', '5+', 'brands positioned', 'Foxymoron',
     'At Foxymoron I shaped pitch and positioning for 5+ brands like DS Group, starting from market research and a competitive map. A comfort brand lives or dies on one clear line in the customer’s head, and that work starts the same way: who else is in the drawer, and why yours.', fab=['brand'], best=True),
   p('dm-voc', 'Content built on what customers say', '30%', 'reach growth', 'Arting Out Loud',
     'I grew campaign reach by 30% by building the content around customer language and what performed. For innerwear, where people describe comfort in their own words (“no riding up”, “no marks”), that language is the brief.', fab=['brand', 'creator']),
   p('dm-jio', 'Brand moments people notice', 'IPL', 'live campaign', 'JioHotstar × PhonePe',
     'A live cricket score inside a payment screen, with messages that changed on wickets and sixes. Brand recall comes from showing up at the right moment, in a form people haven’t seen before.', fab=['brand'], img='cover-moment.webp', pos='50% 30%'),
   # creator
   p('dm-grwm', 'I’ve made the content myself', 'GRWM', '+ 20 posts', 'Nykaa · Arting Out Loud',
     'I’ve produced a GRWM video for the Nykaa case competition and created and scheduled 20+ posts for agency clients. Knowing how long one good post takes makes me a better brief-writer and a fairer partner to creators.', fab=['creator'], link=('Watch the GRWM reel on Instagram', 'https://www.instagram.com/reel/Dd62qJpSbLI/')),
   p('dm-roster', 'A big roster, all on time', '40+', 'partners managed', '30+ brands · 10+ agencies',
     'At PhonePe I managed 30+ brands and 10+ agencies like GroupM and Publicis on milestones, with 100% on-time delivery and 93% of brands coming back. A creator roster needs the same thing: clear briefs, fair terms, tracking, and a reason to work with you again.', fab=['creator', 'founder']),
   p('dm-plan', 'A creator plan, already drafted', '#OneFullDay', 'campaign idea', 'See The Ishani Drop',
     'Influencer marketing is the KRA where I have the most to learn at DaMENSCH’s scale, so I did the homework: a tiered creator plan with tracking, below in The Ishani Drop.', fab=['creator'], link=('Read the creator plan', '#drop'), new=True),
   # growth
   p('dm-oohlala', 'An intimate-wear growth plan, from GA4', 'GA4', 'traffic & conversion', 'Oohlala Stories',
     'I analysed a D2C intimate-wear brand’s GA4 traffic and conversion data with my team, found where shoppers dropped off, and presented the recommendations live to its founders. Same category, same funnel questions.', fab=['growth'], best=True),
   p('dm-aop', 'Revenue at scale, plan delivered', '₹2 Cr+', '/ month', '100% of AOP',
     'Owned monthly revenue for 30+ brands against the annual operating plan at PhonePe and delivered 100% of it.', fab=['growth'], best=True),
   p('dm-roas', 'Acquisition judged on CAC, not clicks', 'Up to 4×', 'ROAS', 'End-funnel tracked',
     'I judged campaigns on CAC and end-funnel conversion, which raised ROAS up to 4×. For DaMENSCH that means tracking first order to second order, not just installs and add-to-carts.', fab=['growth']),
   p('dm-ret', 'Retention is the real growth', '93%', 'came back', 'Repeat partners',
     'Kept 93% of brand partners coming back by learning from each campaign before planning the next. Innerwear is a repeat category, so the second order matters more than the first.', fab=['growth']),
   # npd
   p('dm-assort', 'An assortment picked from real buyers', '350+', 'customers', 'Slay Pop Cult',
     'At Slay Pop Cult I chose what to stock from what 350+ customers actually bought at the stall, built a supplier base across 4 markets, and kept margins near 50%. Consumer need first, then the product.', fab=['npd'], img='slay-stall.webp', pos='50% 45%'),
   p('dm-survey', 'Listening before building', '101', 'people surveyed', 'Prolectro',
     'For Prolectro my team surveyed 101 people before choosing a segment, then designed a ₹129 trial pack and a 35% repeat gate before scale. Find the need, design a cheap first try, and let repeat decide.', fab=['npd']),
   p('dm-formats', 'New products with design teams', '4', 'formats, pilot to live', 'PhonePe',
     'I co-created new ad formats with design teams at PhonePe and took four of them from pilot to live with SOPs. New product work is the same loop: a need, a prototype, a test, a launch plan.', fab=['npd'], img='cover-thunder.webp', pos='50% 30%'),
   # founder
   p('dm-01', '0 → 1, twice', '₹3L+', 'from zero', 'Slay Pop Cult · Postwire',
     'Co-founded Slay Pop Cult (₹3L+, 350+ customers), shipped Postwire, and won Startup Weekend against 25+ teams. I know what it feels like when the founder’s problem is your problem.', fab=['founder'], best=True),
   p('dm-rca', 'Data that changes a decision', '10×', 'key-account growth', 'PhonePe',
     'A slot-level analysis said the spend was in the wrong places, so I made the case to move it, and the account grew 10×. In a founder’s office, the job is to bring the uncomfortable number early.', fab=['founder']),
   p('dm-ai', 'AI-native, end to end', 'Built', 'with Claude', 'Postwire · this site',
     'I built Postwire AI and this store with Claude, from the idea to the live product. I use AI to move faster on research, analysis and first drafts, so more time goes to the decisions.', fab=['founder', 'npd'], link=('Explore Postwire', 'https://postwire.in')),
  ])

FIT = [
 ('brand',   'Lead brand positioning, communication and overall marketing strategy.', 'True to size', 'Agency positioning for 5+ brands, a marketing degree built on consumer behaviour, and content written in customers’ own words.'),
 ('creator', 'Drive influencer partnerships, collaborations and campaigns.', 'Room to grow', 'I’ve made creator content and run a 40+ partner roster on time. Influencer at DaMENSCH’s scale is new, so I drafted a plan below.'),
 ('growth',  'Identify and run growth initiatives across digital: acquisition, engagement, retention.', 'True to size', '₹2 Cr+ a month, up to 4× ROAS, 93% retention, and a GA4 growth plan for an intimate-wear D2C brand.'),
 ('npd',     'Work with product and design teams on new products and consumer needs.', 'True to size', 'An assortment picked from 350+ buyers, a survey-led trial pack, and four formats taken from pilot to live with design.'),
 ('founder', 'Work with the Founder on strategic initiatives and cross-functional projects.', 'True to size', 'Co-founded a D2C brand, built an AI product, won Startup Weekend, and worked across design, data, sales and agencies.'),
]

PLAN = [('WEEKS 1–4', 'Listen', 'Sit in on customer service, read 500 reviews and returns notes, and map the funnel from first ad to second order. Write down the three biggest leaks and bring them to the founder with numbers.'),
        ('WEEKS 5–8', 'Test', 'Run two or three of the tests above, each with one owner, one metric and a stop rule. Brief the first creator cohort for #OneFullDay.'),
        ('WEEKS 9–12', 'Make it repeatable', 'Turn what worked into playbooks and a weekly founder dashboard: CAC by channel, repeat rate, size returns and creator ROI.')]

# ---------- girl graphic (reused from earlier portfolios, recoloured for the store) ----------
GIRL = '''<symbol id="girl" viewBox="-50 -180 110 190"><ellipse cx="4" cy="1" rx="29" ry="5" fill="#514331" opacity=".14"/><path d="M-20-118Q-40-183 1-179Q39-181 28-118L10-103Z" fill="#342d2d"/><g class="leg leg-back"><path d="M0-63L-13-29-17-5" fill="none" stroke="#2b3138" stroke-width="19" stroke-linecap="round"/><path d="M-23-8h16l5 10h-27q-3-9 6-10" fill="#fbf8ed" stroke="#2b3138" stroke-width="2"/></g><path d="M-9-126L15-126 28-72Q7-60-22-72Z" fill="#E2552D"/><path d="M-10-114L-26-85-12-71" fill="none" stroke="#E2552D" stroke-width="13" stroke-linecap="round"/><path d="M-12-71l7 5" stroke="#cc9870" stroke-width="9" stroke-linecap="round"/><g class="leg leg-front"><path d="M13-63L18-31 25-6" fill="none" stroke="#1f252b" stroke-width="20" stroke-linecap="round"/><path d="M17-8h17l7 10H15q-2-9 2-10" fill="#fbf8ed" stroke="#2b3138" stroke-width="2"/></g><rect x="-4" y="-137" width="13" height="16" rx="4" fill="#bd8768"/><ellipse cx="5" cy="-151" rx="19" ry="23" fill="#dca780"/><path d="M-15-153q-4-30 25-24 23 8 14 26-3-23-24-13l-15 17" fill="#342d2d"/><path d="M17-151l8 7-8 2" fill="#dca780"/><circle cx="15" cy="-153" r="1.6" fill="#342d2d"/><path d="M15-141q5 3 8-1" fill="none" stroke="#8a5248" stroke-width="1.4"/><path d="M15-114l10 29 16-2" fill="none" stroke="#E2552D" stroke-width="12" stroke-linecap="round"/><path d="M40-87l7-5" stroke="#dca780" stroke-width="8" stroke-linecap="round"/><g class="held-bag"><path d="M10-84h34l-3 33H13Z" fill="#17181b" stroke="#000" stroke-width="1.5"/><path d="M21-84v-5q6-7 12 0v5" fill="none" stroke="#17181b" stroke-width="2.4"/><text x="27" y="-63" text-anchor="middle" font-size="11" font-weight="800" fill="#fff" font-family="Archivo,sans-serif">Da</text></g></symbol>'''

STOPS = [('school', 'PACKED', 'D.A.V'), ('christ', 'QUALITY CHECK', 'Christ'), ('phonepe', 'SHIPPED', 'PhonePe'),
         ('masters', 'IN TRANSIT', 'Masters’ Union'), ('damensch', 'OUT FOR DELIVERY', 'DaMENSCH')]

def track_svg():
    road = 'M60 150 C 170 70, 250 70, 300 120 S 430 190, 520 130 S 660 50, 740 100 S 880 170, 960 110'
    blocks = ''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6"/>' for x, y, w, h in
        [(20, 20, 110, 40), (160, 8, 90, 46), (330, 20, 130, 50), (560, 170, 120, 40), (700, 20, 90, 40), (820, 26, 150, 44), (130, 175, 140, 30), (400, 200, 90, 22), (860, 185, 120, 30)])
    return f'''<svg id="trackSvg" viewBox="0 0 1000 240" role="img" aria-label="Order tracking map: a route from school to Christ University, PhonePe, Masters’ Union and DaMENSCH, with Ishani walking along it">
<defs>{GIRL}</defs><g class="blocks">{blocks}</g>
<path id="road" d="{road}" class="road"/><path d="{road}" class="road-dash"/><path id="roadDone" d="{road}" class="road-done"/>
<g id="pins"></g><g id="walker"><g id="walkerFlip"><use href="#girl" x="-30" y="-100" width="60" height="104"/></g></g></svg>'''

# ======================= PAGE =======================
def fit_row(k, ask, fit, proof):
    n = sum(1 for d in COLS[-1]['items'] if k in d['fab'])
    cls = ' grow' if fit != 'True to size' else ''
    return f'''<button class="fit-row" type="button" data-fab="{k}" aria-pressed="false"><span class="fr-k"><i class="dot f-{k}"></i><b>{FAB[k][1]}</b><small>{FAB[k][0]}</small></span>
<span class="fr-ask">{E(ask)}</span><span class="fr-proof">{E(proof)}</span><span class="fr-fit{cls}">{E(fit)}<small>{n} pieces</small></span></button>'''

def col_html(i, c):
    items = ''.join(prod_html(k, d, c['short']) for k, d in enumerate(c['items']))
    hl = ''.join(f'<li><b>{E(a)}</b><small>{E(b)}</small></li>' for a, b in c['hl'])
    dm = c['id'] == 'damensch'
    extra = ''
    if dm:
        rows = ''.join(fit_row(*r) for r in FIT)
        extra = f'''<div class="fit" id="fit" aria-labelledby="fit-h"><div class="fit-top"><h3 id="fit-h">{ic('ruler','ic s')} Size guide: the JD, measured</h3>
<button class="fit-clear" type="button" id="fitClear" hidden>Show all {len(c['items'])}</button></div>
<div class="fit-head" aria-hidden="true"><span>KRA</span><span>What the JD asks</span><span>The proof</span><span>Fit</span></div>{rows}</div>'''
    return f'''<section class="coll{' coll-dm' if dm else ''}" id="{c['id']}" data-idx="{i}" aria-labelledby="{c['id']}-h">
<div class="coll-head"><div class="coll-cover"><img src="assets/{c['cover']}" alt="" loading="lazy"><span>{'COMING SOON' if dm else 'COLLECTION ' + c['no']}</span></div>
<div class="coll-txt"><p class="kk">COLLECTION {c['no']} · {E(c['years'])} · {E(c['place'])}</p><h2 id="{c['id']}-h">{E(c['name'])}</h2>
<p class="coll-from">{E(c['where'])}</p><p class="coll-desc">{c['desc']}</p><ul class="coll-hl">{hl}</ul></div></div>
{extra}<div class="grid-top"><p><span class="count" data-count-for="{c['id']}">{len(c['items'])}</span> pieces</p></div>
<div class="grid">{items}</div></section>'''

best_ids = ['mu-oohlala', 'pp-aop', 'mu-slay', 'pp-ctr', 'pp-roas', 'dm-01', 'ch-foxy-gtm', 'mu-postwire']
def mini(pid):
    d = ALL[pid]
    colname = next(c['short'] for c in COLS if d in c['items'])
    return f'''<button class="mini" type="button" data-qv="{pid}"><span class="mini-img">{visual(d, best_ids.index(pid) + 3, colname)}</span>
<span class="mini-t">{E(d['title'])}</span><span class="price">{price_html(d['stat'], d['unit'])}</span></button>'''

tiles = ''.join(f'''<a class="tile" href="#{c['id']}"><img src="assets/{c['cover']}" alt="" loading="lazy"><span class="tile-t"><small>{E(c['where']) if c['id']!='damensch' else 'NEXT'}</small><b>{E(c['name'])}</b><em>{len(c['items'])} pieces {ic('arrow','ic s')}</em></span></a>''' for c in COLS)

USP = [('chart', 'Tested at scale', '₹2 Cr+ a month at PhonePe'), ('bag', 'D2C, hands-on', 'Co-founded Slay Pop Cult'),
       ('ruler', 'Category-ready', 'Intimate-wear growth plan from GA4'), ('sparkle', 'AI-native', 'Built Postwire and this site')]
usp = ''.join(f'<li>{ic(i)}<b>{a}</b><small>{b}</small></li>' for i, a, b in USP)

MARQ = ['2 years of growth, pre-washed', '₹2 Cr+ a month, tested at scale', 'D2C co-founder', 'Five KRAs, one fit', 'Free delivery of ideas', 'Built with AI']
marq = ''.join(f'<span>{E(m)}</span><i>✦</i>' for m in MARQ) * 3

DROP = f'''<section class="drop" id="drop" aria-labelledby="drop-h"><div class="drop-intro"><p class="kk">LIMITED DROP · FOR DAMENSCH ONLY</p>
<h2 id="drop-h">The Ishani Drop.</h2><p>Three ideas I’d bring to week one, one for each of the KRAs where a founder’s office earns its keep. They’re built from the outside in, from public information and how I shop, so they’re hypotheses to test with your data, not promises.</p></div>
<div class="drop-grid">
<article class="dcard"><p class="dk">{ic('users','ic s')} INFLUENCER MARKETING</p><h3>#OneFullDay</h3>
<p class="dlead">Comfort is hard to show in a photo, so show it over time.</p>
<p>Creators wear one pair from 7 am to 11 pm on a real day: gym, commute, a nine-hour desk day, a humid evening out. The video is time-stamped, and the last shot is the honest verdict.</p>
<dl><div><dt>Mix</dt><dd>A few macro creators for reach, 40–50 micro creators (fitness, office life, college) for trust, and 150+ customers seeded for reviews and UGC.</dd></div>
<div><dt>Paid</dt><dd>Whitelist the best-performing videos as ads, so creator content does double duty.</dd></div>
<div><dt>Measure</dt><dd>A code and link per creator. CAC by tier, and the repeat rate of creator-acquired customers, not just views.</dd></div></dl>
<a class="pd-link" href="https://www.instagram.com/reel/Dd62qJpSbLI/" target="_blank" rel="noopener">My own creator reel ↗</a></article>
<article class="dcard"><p class="dk">{ic('gift','ic s')} NEW PRODUCT DEVELOPMENT</p><h3>The Gift Box line</h3>
<p class="dlead">A hypothesis worth one survey question: who is actually buying?</p>
<p>Many men’s basics are bought by someone else: a partner, a sibling, a parent. Ask “Who did you buy this for?” after checkout. If the share is real, it’s a segment no one is speaking to.</p>
<dl><div><dt>Product</dt><dd>Ready-to-gift boxes of three pieces and a note card, timed to Diwali, Valentine’s Day, Raksha Bandhan and Father’s Day, with an easy size exchange so the gifter isn’t scared of guessing wrong.</dd></div>
<div><dt>Why me</dt><dd>Slay Pop Cult was a gifting brand. I picked its assortment from what 350+ customers bought and ran it near 50% margin.</dd></div>
<div><dt>Gate</dt><dd>One box, one festival. Scale only if gift orders reach a set share and exchanges stay low.</dd></div></dl></article>
<article class="dcard"><p class="dk">{ic('chart','ic s')} GROWTH & EXECUTION</p><h3>Three tests, three stop rules</h3>
<p class="dlead">Small bets with one metric each.</p>
<ol class="tests"><li><b>Fit finder on product pages.</b> Three questions (height, weight, preferred fit) suggest a size. <small>Watch size-related returns and page-to-cart rate.</small></li>
<li><b>The refill nudge.</b> Basics wear out. A reminder around month six, with a refill pack. <small>Watch repeat rate at 180 days.</small></li>
<li><b>A bundle ladder.</b> A clear step from 3-pack to 5-pack in the cart. <small>Watch order value without losing conversion.</small></li></ol>
<p class="stop">Each test gets a stop rule before it starts, the same discipline as the 35% repeat gate I set for Prolectro.</p></article></div>
<div class="ninety"><h3>{ic('calendar','ic s')} My first 90 days in the Founder’s Office</h3><ol class="plan">{''.join(f'<li><small>{a}</small><b>{b}</b><p>{c}</p></li>' for a, b, c in PLAN)}</ol>
<p class="scope-note">A plan to test, not a promise. No internal DaMENSCH data was used.</p></div></section>'''

GAME = '''<section class="lab" id="lab" aria-labelledby="lab-h"><div class="lab-intro"><p class="kk">A SMALL DETOUR FOR CURIOUS MINDS</p>
<h2 id="lab-h">Build the Drop.</h2><p>Three calls you’d make launching a summer range. Pick one and see how I’d call it.</p>
<p class="scope-note">Illustrative exercise · No real DaMENSCH data</p></div>
<div class="game-card"><div class="game-top"><span>LAUNCH DESK</span><span id="gameProgress">01 / 03</span></div><div id="gameContent" aria-live="polite"></div>
<div class="game-bottom"><span>Every good launch has a trade-off.</span><button id="gameReset" type="button" aria-label="Restart the game">↺</button></div></div></section>'''

page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Ishani Handa · DaMENSCH</title>
<meta name="description" content="Ishani Handa's portfolio, laid out like an online store: school, Christ University, PhonePe and Masters' Union, matched to the five KRAs of DaMENSCH's Founder's Office, Growth and Marketing role.">
<meta name="theme-color" content="#121212">
<link rel="icon" href="assets/favicon.svg">
<script>try{{var t=localStorage.getItem('dm-theme');if(t)document.documentElement.dataset.theme=t;}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head><body>
<a class="skip" href="#damensch">Skip to the DaMENSCH fit</a>
<div class="splash" id="splash" aria-hidden="true"><div class="splash-in"><div class="logo big"><span>Da</span>ISHANI</div><p id="splashText">Hi DaMENSCH,</p><small>Packing your order…</small></div></div>

<div class="marquee" aria-hidden="true"><div class="mq-track">{marq}</div></div>
<header class="top" id="top"><div class="top-in">
<a class="logo" href="#top" aria-label="DaISHANI home"><span>Da</span>ISHANI</a>
<nav class="desk-nav" aria-label="Sections"><a href="#shop">Collections</a><a href="#journey">Track order</a><a href="#damensch">Fit guide</a><a href="#drop">The Drop</a></nav>
<div class="search"><label for="q" class="sr">Search the store</label>{ic('search','ic s')}<input id="q" type="search" autocomplete="off" placeholder="Search “ROAS”, “D2C”, “creators”…"><div class="results" id="results" role="listbox" hidden></div></div>
<div class="top-act"><button class="icon-btn" type="button" id="themeBtn" aria-label="Switch to dark mode">{ic('moon','ic im')}{ic('sun','ic is')}</button>
<a class="icon-btn hide-s" href="{CV}" target="_blank" rel="noopener" aria-label="Download résumé">{ic('download')}</a>
<button class="icon-btn bag-open" type="button" aria-label="Open hire bag">{ic('bag')}<i class="bag-count">0</i></button></div></div></header>

<main>
<section class="hero"><div class="hero-copy"><p class="kk">NEW ARRIVAL · FOUNDER’S OFFICE · GROWTH &amp; MARKETING</p>
<h1>The hire<br>that <em>fits.</em></h1>
<p>I’m Ishani. Two years growing revenue at PhonePe, a D2C brand I co-founded, and an AI product I built myself. Every piece in this store is real work, tagged to the five KRAs in your JD.</p>
<div class="hero-cta"><a class="btn" href="#damensch">Shop the fit {ic('arrow','ic s')}</a><a class="btn ghost" href="{CV}" target="_blank" rel="noopener">{ic('download','ic s')} Résumé</a></div>
<ul class="hero-stats"><li><b>2 yrs</b><small>experience</small></li><li><b>₹2 Cr+</b><small>a month, owned</small></li><li><b>₹3L+</b><small>D2C, from zero</small></li></ul></div>
<div class="hero-art"><div class="hero-photo"><img src="assets/ishani-portrait.webp" alt="Portrait of Ishani Handa" fetchpriority="high"><span class="badge new">New season</span></div>
<div class="tag-card" aria-hidden="true"><i class="hole"></i><small>DaISHANI</small><b>Ishani Handa</b><dl><div><dt>Fit</dt><dd>Founder’s Office</dd></div><div><dt>Fabric</dt><dd>GrowthFlex · BrandWeave</dd></div><div><dt>Care</dt><dd>Give hard problems</dd></div></dl></div></div></section>

<ul class="usp" aria-label="Why this hire">{usp}</ul>

<section class="block" id="shop" aria-labelledby="shop-h"><div class="sec-top"><h2 id="shop-h" class="sec-h">Shop by collection</h2><p class="sec-sub">Four chapters, and the one I’m here for.</p></div>
<div class="tiles">{tiles}</div></section>

<section class="block track" id="journey" aria-labelledby="track-h"><div class="track-head"><div><p class="kk live">● ORDER #DI-2026</p><h2 id="track-h" class="sec-h"><span id="trackStatus">In transit</span></h2>
<p class="track-sub" id="trackSub">Currently at <b>Masters’ Union</b> · Next stop <b>DaMENSCH</b></p></div><button class="pill" type="button" id="motionToggle" aria-pressed="false">Pause motion Ⅱ</button></div>
<ol class="steps" id="steps">{''.join(f'<li><a href="#{a}"><small>{b}</small>{c}</a></li>' for a, b, c in STOPS)}</ol>
<div class="map">{track_svg()}</div><p class="track-tip">{ic('route','ic s')} Scroll the store and Ishani walks to each collection with you. Tap a stop to jump there.</p></section>

<section class="block" id="best" aria-labelledby="best-h"><div class="sec-top"><h2 id="best-h" class="sec-h">Bestsellers</h2><p class="sec-sub">If you only have a minute.</p></div>
<div class="minis">{''.join(mini(x) for x in best_ids)}</div></section>

{''.join(col_html(i, c) for i, c in enumerate(COLS))}

{DROP}
{GAME}

<section class="about block" id="about" aria-labelledby="about-h"><div class="portrait"><img src="assets/ishani-portrait.webp" alt="" loading="lazy"></div>
<div class="about-copy"><p class="kk">ABOUT THE MAKER</p><h2 id="about-h">Hi again. I’m Ishani.</h2>
<p>I like the space where a creative idea meets a spreadsheet. I’ve grown revenue for 30+ brands at PhonePe, positioned brands at an agency, built and sold through a D2C brand myself, and shipped an AI product with Claude.</p>
<p>School sparked the curiosity. Christ gave it a marketing lens. PhonePe put it into practice. At Masters’ Union I’m building from 0 → 1. Next, I’d like to work beside DaMENSCH’s founder on the brand, the creators, the growth and the products that come next.</p>
<div class="contact-row"><a class="btn" href="mailto:{EMAIL}?subject=Founder%E2%80%99s%20Office%2C%20Growth%20%26%20Marketing">{ic('mail','ic s')} Email me</a><button class="btn ghost" type="button" id="copyEmail">Copy email</button>
<a class="btn ghost" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn ↗</a><a class="btn ghost" href="{CV}" target="_blank" rel="noopener">{ic('download','ic s')} Résumé</a></div></div></section>
</main>

<footer><div class="logo"><span>Da</span>ISHANI</div><p>Ready to deliver for DaMENSCH’s Founder’s Office.</p>
<p class="disc">A personal portfolio styled as an online store, made for a job application. Not affiliated with or endorsed by DaMENSCH.</p><a href="#top">Back to the top ↑</a></footer>

<div class="strip off" id="strip" aria-hidden="true"><svg viewBox="0 0 400 54"><path d="M24 50H376" class="s-road"/><path id="stripDone" d="M24 50H24" class="s-done"/>
{''.join(f'<circle class="ms" cx="{24 + k * 88}" cy="50" r="4"/>' for k in range(5))}
<g id="miniWalker"><g id="miniFlip"><use href="#girl" x="-14" y="-2" width="28" height="48"/></g></g></svg><p id="stripHint">Walking with you</p></div>

<div class="scrim" id="scrim" hidden></div>
<div class="modal" id="qv" role="dialog" aria-modal="true" aria-labelledby="qvTitle" hidden><button class="icon-btn qv-x" type="button" id="qvClose" aria-label="Close">{ic('x')}</button>
<div class="qv-img" id="qvImg"></div><div class="qv-body"><p class="kk" id="qvCol"></p><h3 id="qvTitle"></h3><p class="price" id="qvPrice"></p><p class="prod-tag" id="qvTag"></p><div id="qvBody"></div>
<button class="btn" type="button" id="qvAdd">{ic('bag','ic s')} <span>Add to hire bag</span></button></div></div>

<aside class="drawer" id="bag" aria-labelledby="bagTitle" hidden><div class="dr-top"><h3 id="bagTitle">Your hire bag <span class="bag-count">0</span></h3><button class="icon-btn" type="button" id="bagClose" aria-label="Close bag">{ic('x')}</button></div>
<ul id="bagList"></ul><p class="bag-empty" id="bagEmpty">Your bag is empty. Add the pieces you’d like to talk about in an interview.</p>
<div class="dr-foot"><a class="btn" id="checkout" href="mailto:{EMAIL}">{ic('mail','ic s')} Checkout: let’s talk</a><a class="btn ghost" href="{CV}" target="_blank" rel="noopener">{ic('download','ic s')} Download résumé</a></div></aside>

<nav class="bottom-nav" aria-label="Store"><a href="#top" data-nav="home">{ic('home')}<span>Home</span></a><a href="#shop" data-nav="shop">{ic('grid')}<span>Shop</span></a><a href="#journey" data-nav="journey">{ic('truck')}<span>Track</span></a><a href="#drop" data-nav="drop">{ic('sparkle')}<span>Drop</span></a><button type="button" class="bag-open">{ic('bag')}<span>Bag</span><i class="bag-count">0</i></button></nav>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script>window.DM_EMAIL={EMAIL!r};</script>
<script src="app.js"></script>
</body></html>'''

open(os.path.join(ROOT, 'index.html'), 'w').write(page)
print('wrote index.html', len(page), 'bytes,', len(ALL), 'products')
