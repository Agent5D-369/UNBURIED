from pathlib import Path
import textwrap

site = Path('/mnt/data/unburied-site')
assets = site / 'assets' / 'placeholders'
assets.mkdir(parents=True, exist_ok=True)
icons = site / 'assets' / 'icons'
icons.mkdir(parents=True, exist_ok=True)

brand = 'UNBURIED'
brand_full = 'UNBURIED Screen Network'
domain = 'https://YOURDOMAIN.com'

common_head = lambda title, desc, path, og='assets/placeholders/og-cover.svg', extra_json='': f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#090b12">
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  <link rel="canonical" href="{domain}/{path}">
  <link rel="icon" href="assets/icons/favicon.svg" type="image/svg+xml">
  <link rel="manifest" href="site.webmanifest">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{domain}/{path}">
  <meta property="og:image" content="{domain}/{og}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{domain}/{og}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
  <script type="application/ld+json">{{
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "{brand_full}",
    "url": "{domain}",
    "logo": "{domain}/assets/icons/favicon.svg",
    "description": "A filmmaker-first screen network for culturally important independent films facing structural distribution resistance.",
    "sameAs": []
  }}</script>
  <script type="application/ld+json">{{
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "{brand_full}",
    "url": "{domain}",
    "description": "A filmmaker-first screen network for culturally important independent films facing structural distribution resistance.",
    "potentialAction": {{
      "@type": "SubscribeAction",
      "target": "{domain}/index.html#waitlist",
      "name": "Join the waitlist"
    }}
  }}</script>
  {extra_json}
</head>'''

header = f'''<body>
  <div class="progress-line" aria-hidden="true"></div>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header" id="top">
    <div class="container nav-shell">
      <a class="brand" href="index.html" aria-label="{brand_full} home">
        <span class="brand-mark" aria-hidden="true"></span>
        <span class="brand-lockup">
          <span class="brand-word">{brand}</span>
          <span class="brand-sub">Screen Network</span>
        </span>
      </a>
      <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links">
        <span></span><span></span><span></span>
      </button>
      <nav class="nav-links" id="nav-links">
        <a href="index.html">Home</a>
        <a href="filmmakers.html">Filmmakers</a>
        <a href="hosts.html">Hosts</a>
        <a href="investors.html">Investors</a>
        <a href="index.html#waitlist" class="nav-cta">Get early access</a>
      </nav>
    </div>
  </header>
  <main id="main">'''

footer = f'''
  </main>
  <div class="mobile-cta-bar">
    <a href="index.html#waitlist" class="btn btn-primary btn-block">Get early access</a>
  </div>
  <footer class="site-footer">
    <div class="container footer-grid">
      <div>
        <div class="footer-brand">{brand_full}</div>
        <p class="footer-copy">A filmmaker-first screen network for films that deserve circulation, not quiet disappearance.</p>
      </div>
      <div>
        <div class="footer-label">Explore</div>
        <a href="filmmakers.html">For filmmakers</a>
        <a href="hosts.html">For hosts</a>
        <a href="investors.html">For investors</a>
      </div>
      <div>
        <div class="footer-label">Primary promise</div>
        <p class="footer-note">Keep rights. Own audience. Activate direct revenue, local screening rights, and resilient distribution rails in one premium system.</p>
      </div>
      <div>
        <div class="footer-label">Launch note</div>
        <p class="footer-note">Brand, domain, and trademark clearance pending final legal review. Replace Formspree form IDs and canonical domain before launch.</p>
      </div>
    </div>
  </footer>
  <script src="script.js" defer></script>
</body>
</html>'''

home_extra = '''<script type="application/ld+json">{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is UNBURIED Screen Network?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "UNBURIED Screen Network is a filmmaker-first distribution network for culturally important independent films facing structural distribution resistance."
      }
    },
    {
      "@type": "Question",
      "name": "Who is it built for?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "It is built for independent filmmakers, small rights-holding teams, aligned hosts, educators, cultural distributors, and investors who care about creator sovereignty and resilient rails."
      }
    },
    {
      "@type": "Question",
      "name": "What do I get if I join early?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "You receive the Sovereign Release Brief, launch updates, and priority access to early filmmaker, host, or investor conversations."
      }
    }
  ]
}</script>'''

home = common_head(
    f'{brand_full} | Sovereign distribution for films that matter',
    'A premium, filmmaker-first screen network for culturally important independent films facing structural distribution resistance.',
    'index.html',
    extra_json=home_extra,
) + header + '''
<section class="hero hero-home">
  <div class="container hero-shell">
    <div class="hero-copy reveal">
      <span class="eyebrow">For films that matter and the people who move them</span>
      <div class="persona-switch" data-persona-switch>
        <button class="persona-pill is-active" data-persona="filmmakers" type="button">Filmmakers</button>
        <button class="persona-pill" data-persona="hosts" type="button">Hosts</button>
        <button class="persona-pill" data-persona="investors" type="button">Investors</button>
      </div>
      <h1 class="display-title" data-persona-title>Your film should not need permission to circulate.</h1>
      <p class="lead" data-persona-copy>UNBURIED gives high-friction films a premium path from buried and fragmented to watchable, licensable, hostable, and paid — without forcing the filmmaker to become a full-time distribution company.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" data-persona-primary href="#waitlist">Get the Sovereign Release Brief</a>
        <a class="btn btn-secondary" data-persona-secondary href="filmmakers.html">See the filmmaker model</a>
      </div>
      <div class="hero-proof-list" data-persona-bullets>
        <span>Keep rights by default</span>
        <span>Own your audience relationship</span>
        <span>Monetize through watch, host, license, and support</span>
      </div>
      <div class="trust-strip">
        <div><strong>Broad umbrella.</strong><span>Independent cinema network.</span></div>
        <div><strong>Sharp wedge.</strong><span>High-friction films first.</span></div>
        <div><strong>Simple ask.</strong><span>Join early. Shape the launch.</span></div>
      </div>
    </div>
    <div class="hero-stage reveal reveal-delay">
      <div class="hero-stage-glow"></div>
      <div class="screen-stack">
        <div class="floating-screen screen-a">
          <span class="screen-label">Direct viewing</span>
          <strong>Rent · Buy · Gift</strong>
          <p>One clean film page. Premium playback. Friction-free checkout.</p>
        </div>
        <div class="floating-screen screen-b">
          <span class="screen-label">Community circulation</span>
          <strong>Host · Ticket · Tour</strong>
          <p>Local screening rights built for cities, campuses, and trusted networks.</p>
        </div>
        <div class="floating-screen screen-c">
          <span class="screen-label">Resilient rails</span>
          <strong>Fiat first. Bitcoin optional.</strong>
          <p>Mainstream ease on top. Sovereign fallbacks underneath.</p>
        </div>
      </div>
      <div class="orbit-card">
        <div class="orbit-dot"></div>
        <p>Built for directors, producers, rights holders, educators, venues, curators, and aligned capital who are done watching important films get softened, stranded, or quietly buried.</p>
      </div>
    </div>
  </div>
</section>

<section class="logo-rail reveal">
  <div class="container">
    <div class="eyebrow eyebrow-muted">What this replaces</div>
    <div class="chip-scroll" role="list" aria-label="Current system pain points">
      <span class="chip-card" role="listitem">Festival buzz with no durable release path</span>
      <span class="chip-card" role="listitem">Streaming exposure with no audience ownership</span>
      <span class="chip-card" role="listitem">Patchwork tools that break under real pressure</span>
      <span class="chip-card" role="listitem">Payment fragility across borders and categories</span>
      <span class="chip-card" role="listitem">One-week attention spikes followed by silence</span>
    </div>
  </div>
</section>

<section class="section-story">
  <div class="container split-intro reveal">
    <div>
      <span class="eyebrow">The future we are selling</span>
      <h2>A world where bold films keep moving long after the gatekeepers pass.</h2>
      <p class="body-lg">Not another “upload your movie here” site. A premium distribution network where difficult, necessary, culture-shaping films can be discovered, purchased, hosted, licensed, and backed through living communities instead of dying in a maze of stalled buyers, weak payment rails, and disconnected tools.</p>
    </div>
    <aside class="pull-quote-card">
      <p class="pull-quote">The real pain is not only suppression. It is suppression plus fragmentation plus financial fragility plus operational overload.</p>
      <p class="quote-foot">That is the gap UNBURIED is built to close.</p>
    </aside>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Why dream clients lean in fast</span>
      <h2>This names the problem they have been carrying without giving them another vague “platform promise.”</h2>
      <p class="body-lg">The site should make the right person feel three things in under ten seconds: seen, relieved, and curious enough to act.</p>
    </div>
    <div class="bento-grid reveal">
      <article class="bento-card bento-wide">
        <span class="kicker">2 a.m. problem</span>
        <h3>“I made something important, but I still do not have a safe, sovereign, financially viable way to get it seen and paid for.”</h3>
        <p>No trustworthy distribution partner. No integrated release stack. No room to hand over the asset just to survive. No appetite to become a full-time distribution company.</p>
      </article>
      <article class="bento-card">
        <span class="kicker">Desired transformation</span>
        <h3>From stranded title to sovereign release machine</h3>
        <p>Direct revenue, portable audience ownership, local screening rights, educational licensing, support campaigns, and resilient settlement rails.</p>
      </article>
      <article class="bento-card">
        <span class="kicker">Why it feels different</span>
        <h3>It respects the film and the people around it</h3>
        <p>Premium curation. No sludge feed. No bait language. No performative “community” that does nothing for circulation.</p>
      </article>
      <article class="bento-card">
        <span class="kicker">Regenerative purpose</span>
        <h3>Restore narrative sovereignty</h3>
        <p>Return cultural distribution power to creators and communities instead of forcing vital films through extractive choke points.</p>
      </article>
    </div>
  </div>
</section>

<section class="section-contrast">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">The new standard</span>
      <h2>What dream targets want is not a bigger feed. It is a cleaner route through reality.</h2>
    </div>
    <div class="compare-toggle reveal" data-compare>
      <div class="compare-tabs">
        <button class="compare-tab is-active" data-target="old" type="button">The current release stack</button>
        <button class="compare-tab" data-target="new" type="button">The UNBURIED model</button>
      </div>
      <div class="compare-panel is-active" data-panel="old">
        <div class="stack-list">
          <div><strong>Buyers pass or stall.</strong><span>The film sits in limbo while momentum cools.</span></div>
          <div><strong>Generic hosts do not solve rights.</strong><span>You still need ticketing, approvals, customer support, and host tools.</span></div>
          <div><strong>Payment systems behave like a hidden enemy.</strong><span>Cross-border payouts, reserves, disputes, and banking limits show up late.</span></div>
          <div><strong>The audience is rented.</strong><span>You get views. You do not build a durable relationship graph.</span></div>
        </div>
      </div>
      <div class="compare-panel" data-panel="new">
        <div class="stack-list">
          <div><strong>One premium title page.</strong><span>Watch, buy, support, host, and share from a single high-trust surface.</span></div>
          <div><strong>Rights-aware distribution.</strong><span>Keep rights by default and activate viewing, screenings, and licensing without surrendering the whole asset.</span></div>
          <div><strong>Modular rails.</strong><span>Mainstream rails for ease. Sovereign fallback rails for continuity.</span></div>
          <div><strong>Audience ownership.</strong><span>Buyers, supporters, hosts, affiliates, and educators become part of a living distribution network.</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">How the system works</span>
      <h2>A premium, rights-aware network with enough depth to hold complexity and enough restraint to stay usable.</h2>
    </div>
    <div class="pillars-grid reveal">
      <article class="feature-card">
        <span class="feature-step">01</span>
        <h3>Curated trust</h3>
        <p>A selective catalog that protects discoverability and brand integrity instead of collapsing into an open upload dump.</p>
      </article>
      <article class="feature-card">
        <span class="feature-step">02</span>
        <h3>Direct revenue</h3>
        <p>Rentals, purchases, gifts, educational licensing, community screenings, and later support campaigns in one system.</p>
      </article>
      <article class="feature-card">
        <span class="feature-step">03</span>
        <h3>Community circulation</h3>
        <p>Hosts, educators, venues, curators, and aligned organizations become the film’s distribution engine.</p>
      </article>
      <article class="feature-card">
        <span class="feature-step">04</span>
        <h3>Resilient architecture</h3>
        <p>Portable audiences, modular payments, premium playback, and fallback rails built to reduce dependency on any single choke point.</p>
      </article>
    </div>
  </div>
</section>

<section class="section-workflows">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Product-as-proof</span>
      <h2>The page shows the category before the product exists in full.</h2>
      <p class="body-lg">That matters in 2026. Great sites do not just “look premium.” They help the buyer see the future workflow fast.</p>
    </div>
    <div class="workflow-grid reveal">
      <article class="workflow-card">
        <span class="workflow-label">For filmmakers</span>
        <h3>Fund → Launch → Watch → Host → License → Get paid</h3>
        <p>One coherent release path instead of six disconnected tools and a fragile spreadsheet.</p>
        <a href="filmmakers.html" class="text-link">See the full filmmaker model</a>
      </article>
      <article class="workflow-card">
        <span class="workflow-label">For hosts</span>
        <h3>Request → Approve → Sell tickets → Screen → Settle</h3>
        <p>A local screening flow that feels simple enough for communities and rigorous enough for rights holders.</p>
        <a href="hosts.html" class="text-link">See the host flow</a>
      </article>
      <article class="workflow-card">
        <span class="workflow-label">For aligned capital</span>
        <h3>Back infrastructure → finance releases → expand rails</h3>
        <p>A category bet on seller tools, artist entrepreneurship, and open-money-aligned distribution.</p>
        <a href="investors.html" class="text-link">See the investor thesis</a>
      </article>
    </div>
  </div>
</section>

<section class="section-investor-callout">
  <div class="container investor-callout reveal">
    <div>
      <span class="eyebrow">For investors shaped by seller tools and open money</span>
      <h2>If you understand why small merchants, artists, and communities need simpler ownership and better rails, you will recognize this category immediately.</h2>
      <p class="body-lg">This is not a bet on generic content volume. It is a bet on creator-controlled commerce, optional self-custody, and a seller network for films the current system cannot place cleanly.</p>
    </div>
    <div class="callout-card">
      <div class="callout-row"><strong>Legible to:</strong><span>people bullish on seller infrastructure, artist entrepreneurship, optional bitcoin rails, and self-custody without consumer complexity</span></div>
      <div class="callout-row"><strong>Why now:</strong><span>important films are underserved, direct support is normalized, and payment + wallet infrastructure is finally maturing</span></div>
      <a class="btn btn-secondary btn-small" href="investors.html">Read the investor page</a>
    </div>
  </div>
</section>

<section>
  <div class="container section-head reveal">
    <span class="eyebrow">What you get for joining early</span>
    <h2>Not a vague newsletter. Useful intelligence and first access to the people shaping the launch.</h2>
    <p class="body-lg">Lead magnets only work when they name a problem the right people are already trying to solve. So the offer has to feel like clarity, not bait.</p>
  </div>
  <div class="resource-grid reveal">
    <article class="resource-card">
      <span class="kicker">For filmmakers</span>
      <h3>The Sovereign Release Brief</h3>
      <p>The seven choke points burying bold films in 2026 and the release architecture that routes around them.</p>
    </article>
    <article class="resource-card">
      <span class="kicker">For hosts</span>
      <h3>The Community Screening Playbook</h3>
      <p>How to bring important films to your city without rights confusion, weak turnout, or post-event chaos.</p>
    </article>
    <article class="resource-card">
      <span class="kicker">For investors</span>
      <h3>The Narrative Sovereignty Thesis</h3>
      <p>The category map, business model, risk architecture, and why this looks more like seller infrastructure than entertainment fluff.</p>
    </article>
  </div>
</section>

<section id="waitlist" class="section-waitlist">
  <div class="container waitlist-shell reveal">
    <div>
      <span class="eyebrow">Join early</span>
      <h2>Get the brief that fits your role and a front-row seat to the first wave.</h2>
      <p class="body-lg">Whether you are carrying a film, filling rooms, or looking at the infrastructure thesis, this is the cleanest way into the network.</p>
      <ul class="checklist">
        <li>Pick your role and receive the most relevant brief first.</li>
        <li>Get launch notes, early access invitations, and pilot updates.</li>
        <li>Be first to hear when filmmaker applications, host onboarding, and investor conversations open.</li>
      </ul>
    </div>
    <div class="form-shell form-shell-strong">
      <h3>Get early access</h3>
      <form action="https://formspree.io/f/YOUR_PRIMARY_FORM_ID" method="POST" class="form-grid">
        <input type="hidden" name="form_name" value="Primary Waitlist">
        <label><span class="field-label">Name</span><input type="text" name="name" placeholder="Your name" required></label>
        <label><span class="field-label">Email</span><input type="email" name="email" placeholder="you@example.com" required></label>
        <label><span class="field-label">I am joining as</span>
          <select name="role" required>
            <option value="">Choose one</option>
            <option>Filmmaker / rights holder</option>
            <option>Host / venue / educator</option>
            <option>Investor / strategic partner</option>
            <option>Curator / journalist / ecosystem ally</option>
          </select>
        </label>
        <label><span class="field-label">What are you trying to solve right now?</span><textarea name="note" placeholder="A release problem, a rights headache, a hosting ambition, an investment angle, or the reason this instantly felt relevant."></textarea></label>
        <button class="btn btn-primary btn-block" type="submit">Send me the right brief</button>
        <p class="micro-note">Replace the Formspree endpoint with your live form ID and connect the response email that matches your launch workflow.</p>
      </form>
    </div>
  </div>
</section>

<section class="section-faq">
  <div class="container reveal">
    <div class="section-head">
      <span class="eyebrow">FAQ</span>
      <h2>The questions smart dream targets ask before they opt in</h2>
    </div>
    <div class="faq-grid">
      <details class="faq-item"><summary>Is this only for political documentaries?</summary><p>No. The wedge is high-friction films first, but the umbrella brand is broader: premium independent cinema that deserves a real release path and a rights-respecting home.</p></details>
      <details class="faq-item"><summary>Is this trying to replace YouTube?</summary><p>No. That is the wrong category model. This is a curated distribution and rights network, not a mass-feed video platform.</p></details>
      <details class="faq-item"><summary>Will crypto be forced on normal users?</summary><p>No. Mainstream checkout should feel effortless. Sovereign rails sit underneath as optional resilience and international-settlement layers where they actually help.</p></details>
      <details class="faq-item"><summary>What makes the waitlist worth joining?</summary><p>You receive a role-specific brief that is designed to name the exact release, hosting, or category problem you are already trying to solve, plus early access to pilot opportunities.</p></details>
    </div>
  </div>
</section>
''' + footer

filmmakers_extra = '''<script type="application/ld+json">{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://YOURDOMAIN.com/index.html"},
    {"@type": "ListItem", "position": 2, "name": "Filmmakers", "item": "https://YOURDOMAIN.com/filmmakers.html"}
  ]
}</script>'''

filmmakers = common_head(
    f'For Filmmakers | {brand_full}',
    'Keep your rights, own your audience, and activate direct viewing, local screenings, and licensing through one premium release system.',
    'filmmakers.html',
    extra_json=filmmakers_extra,
) + header + '''
<section class="page-hero page-hero-filmmakers">
  <div class="container page-hero-grid">
    <div class="reveal">
      <span class="eyebrow">For filmmakers and rights holders</span>
      <h1 class="display-title display-title-page">Stop carrying an important film into a release system that was never built to carry it with you.</h1>
      <p class="lead">UNBURIED helps high-friction films move from stranded and fragmented to watchable, hostable, licensable, and paid — without demanding that you surrender the asset or become your own exhausted distribution department.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#filmmaker-form">Get the Sovereign Release Brief</a>
        <a class="btn btn-secondary" href="#model">See the revenue model</a>
      </div>
      <div class="hero-proof-list compact">
        <span>Keep rights by default</span>
        <span>Own your audience relationship</span>
        <span>Open multiple revenue lanes without patchwork chaos</span>
      </div>
    </div>
    <div class="visual-panel reveal reveal-delay">
      <img src="assets/placeholders/filmmakers-hero.svg" alt="Abstract cinematic illustration representing a premium release engine for independent films">
    </div>
  </div>
</section>

<section>
  <div class="container split-intro reveal">
    <div>
      <span class="eyebrow">Your actual 2 a.m. problem</span>
      <h2>“I made something brave and culturally important, and I still do not have a trustworthy path to get it seen, sold, protected, and paid for.”</h2>
    </div>
    <aside class="pull-quote-card">
      <p class="pull-quote">This is not only a visibility problem. It is a release architecture problem.</p>
      <p class="quote-foot">You do not need another generic host. You need infrastructure.</p>
    </aside>
  </div>
</section>

<section>
  <div class="container">
    <div class="bento-grid reveal">
      <article class="bento-card bento-wide">
        <span class="kicker">Before</span>
        <h3>You have a real film and an unreal release stack.</h3>
        <p>Festival buzz cools. Buyers stall. Streamers ask for safer positioning. Self-release means piecing together video hosting, ticketing, spreadsheets, rights emails, audience capture, payout logic, and support tickets on your own.</p>
      </article>
      <article class="bento-card">
        <span class="kicker">After</span>
        <h3>A sovereign release path</h3>
        <p>One system for direct viewing, local screenings, educational access, support campaigns, audience ownership, and resilient settlement rails.</p>
      </article>
      <article class="bento-card">
        <span class="kicker">Emotional relief</span>
        <h3>You stop carrying all of it alone</h3>
        <p>The right page, the right rights flow, the right host flow, and the right payout logic already exist.</p>
      </article>
      <article class="bento-card">
        <span class="kicker">Operational edge</span>
        <h3>Your audience becomes a living asset</h3>
        <p>Buyers, supporters, hosts, educators, and affiliates become a durable relationship graph, not a ghost audience trapped inside someone else’s feed.</p>
      </article>
    </div>
  </div>
</section>

<section id="model">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">What you can do inside the network</span>
      <h2>The filmmaker model in plain language</h2>
      <p class="body-lg">This page is intentionally specific. Serious filmmakers do not trust hand-wavy promises anymore, and they should not.</p>
    </div>
    <div class="feature-list reveal">
      <article class="feature-row"><span class="feature-step">01</span><div><h3>Onboard a title once</h3><p>Set rights, territories, pricing bands, windows, host rules, educational availability, and payout preferences in one place.</p></div></article>
      <article class="feature-row"><span class="feature-step">02</span><div><h3>Sell directly</h3><p>Activate rentals, purchases, gifts, and pre-order style campaigns without handing over the film to an opaque platform economy.</p></div></article>
      <article class="feature-row"><span class="feature-step">03</span><div><h3>Approve or automate screening rights</h3><p>Let trusted hosts move quickly while keeping more sensitive events under manual control.</p></div></article>
      <article class="feature-row"><span class="feature-step">04</span><div><h3>License for educators and institutions</h3><p>Offer classroom, campus, and library access with cleaner terms and less negotiation drag.</p></div></article>
      <article class="feature-row"><span class="feature-step">05</span><div><h3>Track what matters</h3><p>See revenue by lane, reserve holds, screenings booked, audience growth, and who is actually helping the film travel.</p></div></article>
    </div>
  </div>
</section>

<section>
  <div class="container section-head reveal">
    <span class="eyebrow">Revenue lanes</span>
    <h2>Simple enough to explain to your team. Sophisticated enough to hold up under real pressure.</h2>
  </div>
  <div class="table-wrap reveal">
    <table class="table">
      <thead>
        <tr>
          <th>Lane</th>
          <th>What the buyer experiences</th>
          <th>Suggested split</th>
          <th>Why it matters</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Rental / purchase</td>
          <td>Film page → checkout → secure playback</td>
          <td>85 / 10 / 5</td>
          <td>Fastest path to direct revenue and clean audience capture</td>
        </tr>
        <tr>
          <td>Community screening</td>
          <td>Host request → approval → ticketing → event settlement</td>
          <td>60 / 25 / 15</td>
          <td>Turns trusted communities into distribution nodes</td>
        </tr>
        <tr>
          <td>Educational license</td>
          <td>Institution inquiry → instant tier or manual quote</td>
          <td>70 / 20 / 10</td>
          <td>Builds long-tail value beyond launch week</td>
        </tr>
        <tr>
          <td>Support campaign</td>
          <td>Story page → pledge or pre-buy → updates</td>
          <td>95 / 5</td>
          <td>Helps upcoming titles finish strong and activate early believers</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section class="section-contrast">
  <div class="container split-band reveal">
    <div>
      <span class="eyebrow">Money and rails</span>
      <h2>Fiat first for ease. Sovereign options where they genuinely improve resilience.</h2>
      <p class="body-lg">Normal viewers should never need a crypto education just to watch a film. At the same time, the system should not be naïve about payment fragility, cross-border complexity, or the need for fallback rails.</p>
      <ul class="checklist">
        <li>Easy consumer checkout on mainstream rails</li>
        <li>Reserve logic that reflects real dispute risk</li>
        <li>Optional stablecoin and self-custody rails where they actually reduce friction</li>
        <li>Rights and contracts kept legible in plain language, not hidden inside token theater</li>
      </ul>
    </div>
    <div class="visual-panel visual-panel-compact">
      <img src="assets/placeholders/payments-rails.svg" alt="Diagram showing layered payment and resilience rails for film distribution">
    </div>
  </div>
</section>

<section>
  <div class="container section-head reveal">
    <span class="eyebrow">What this replaces emotionally</span>
    <h2>The feeling of watching your film’s momentum die because no one put the whole machine in one place.</h2>
  </div>
  <div class="quote-grid reveal">
    <article class="quote-card"><h3>Relief</h3><p>“Finally, someone understands the actual release burden.”</p></article>
    <article class="quote-card"><h3>Hope</h3><p>“This is the first model that feels built for films like ours.”</p></article>
    <article class="quote-card"><h3>Urgency</h3><p>“If this exists, I want in early, before the first wave hardens the category.”</p></article>
  </div>
</section>

<section id="filmmaker-form" class="section-waitlist">
  <div class="container waitlist-shell reveal">
    <div>
      <span class="eyebrow">For filmmakers</span>
      <h2>Get the Sovereign Release Brief and the first invitation when filmmaker onboarding opens.</h2>
      <p class="body-lg">This is for finished films, near-finished films, and rights holders who can already feel the release problem building.</p>
      <ul class="checklist">
        <li>The seven release choke points killing important films right now</li>
        <li>The revenue lanes most teams underuse</li>
        <li>The first version of the filmmaker onboarding criteria</li>
      </ul>
    </div>
    <div class="form-shell form-shell-strong">
      <h3>Get the brief</h3>
      <form action="https://formspree.io/f/YOUR_FILMMAKER_FORM_ID" method="POST" class="form-grid">
        <input type="hidden" name="form_name" value="Filmmaker Waitlist">
        <label><span class="field-label">Name</span><input type="text" name="name" required></label>
        <label><span class="field-label">Email</span><input type="email" name="email" required></label>
        <label><span class="field-label">Film or company</span><input type="text" name="project"></label>
        <label><span class="field-label">Current stage</span>
          <select name="stage">
            <option>Finished</option>
            <option>Picture locked / near release</option>
            <option>In post</option>
            <option>Seeking completion support</option>
          </select>
        </label>
        <label><span class="field-label">What is the hardest part of your release path right now?</span><textarea name="note" placeholder="Acquisition silence, political risk, payments, rights complexity, local screenings, audience ownership, or another pressure point."></textarea></label>
        <button class="btn btn-primary btn-block" type="submit">Send me the filmmaker brief</button>
      </form>
    </div>
  </div>
</section>
''' + footer

hosts_extra = '''<script type="application/ld+json">{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://YOURDOMAIN.com/index.html"},
    {"@type": "ListItem", "position": 2, "name": "Hosts", "item": "https://YOURDOMAIN.com/hosts.html"}
  ]
}</script>'''

hosts = common_head(
    f'For Hosts | {brand_full}',
    'Bring important films to your city, campus, venue, or community without drowning in rights confusion or event chaos.',
    'hosts.html',
    extra_json=hosts_extra,
) + header + '''
<section class="page-hero page-hero-hosts">
  <div class="container page-hero-grid">
    <div class="reveal">
      <span class="eyebrow">For hosts, venues, educators, and local distributors</span>
      <h1 class="display-title display-title-page">Bring important films to your people without getting trapped in rights confusion, event drag, or fragile logistics.</h1>
      <p class="lead">UNBURIED turns community screenings into a premium, rights-aware flow that feels simple on the surface and serious underneath — request, approve, ticket, screen, settle.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#host-form">Get the Community Screening Playbook</a>
        <a class="btn btn-secondary" href="#workflow">See the host workflow</a>
      </div>
    </div>
    <div class="visual-panel reveal reveal-delay">
      <img src="assets/placeholders/hosts-hero.svg" alt="Abstract illustration of a premium local screening network across multiple cities">
    </div>
  </div>
</section>

<section>
  <div class="container split-intro reveal">
    <div>
      <span class="eyebrow">What hosts are actually trying to solve</span>
      <h2>You do not want to become a legal department just to fill a room with a film that matters.</h2>
      <p class="body-lg">Hosts want to move quickly, protect trust, fill seats, and know the rights are real. Rights holders want the same thing from the other side. The system has to honor both.</p>
    </div>
    <aside class="pull-quote-card">
      <p class="pull-quote">The win is not just a screening. It is a local node of circulation that can keep working for the film after one night.</p>
    </aside>
  </div>
</section>

<section>
  <div class="container bento-grid reveal">
    <article class="bento-card bento-wide">
      <span class="kicker">Who this page is for</span>
      <h3>Independent venues, educators, libraries, community organizers, podcasters, cultural leaders, nonprofit teams, and trusted groups who know a film can open a room.</h3>
      <p>Sometimes the right audience is local, not algorithmic. This page is for the people willing to make that audience real.</p>
    </article>
    <article class="bento-card">
      <span class="kicker">2 a.m. problem</span>
      <h3>“I want to bring this film here, but licensing and logistics are a mess.”</h3>
      <p>Too many emails. Too much uncertainty. Not enough clarity about rights, pricing, promotion, and support.</p>
    </article>
    <article class="bento-card">
      <span class="kicker">Desired transformation</span>
      <h3>From passionate supporter to empowered local distributor</h3>
      <p>Request rights, launch an event page, sell tickets, access the screening, and settle cleanly.</p>
    </article>
    <article class="bento-card">
      <span class="kicker">Why it matters</span>
      <h3>Local screenings turn attention into culture</h3>
      <p>The audience is not just watching. They are gathering, discussing, and often carrying the film further.</p>
    </article>
  </div>
</section>

<section id="workflow">
  <div class="container section-head reveal">
    <span class="eyebrow">How the host flow works</span>
    <h2>Fast enough to feel frictionless. Serious enough to protect the title.</h2>
  </div>
  <div class="feature-list reveal">
    <article class="feature-row"><span class="feature-step">01</span><div><h3>Discover a host-ready title</h3><p>Browse films already set up for community, educational, commercial, or private event use.</p></div></article>
    <article class="feature-row"><span class="feature-step">02</span><div><h3>Request the right license</h3><p>Choose event type, city, date, venue size, and ticket plan without decoding legal language.</p></div></article>
    <article class="feature-row"><span class="feature-step">03</span><div><h3>Get approved or routed cleanly</h3><p>Simple events can move fast. Sensitive requests can still go to manual review when they should.</p></div></article>
    <article class="feature-row"><span class="feature-step">04</span><div><h3>Launch the screening page</h3><p>Use a high-trust event surface with ticketing, approved copy, share assets, and viewing instructions.</p></div></article>
    <article class="feature-row"><span class="feature-step">05</span><div><h3>Run the event and settle fairly</h3><p>The system handles access timing, settlement logic, and the post-event summary without turning your night into admin soup.</p></div></article>
  </div>
</section>

<section class="section-contrast">
  <div class="container split-band reveal">
    <div>
      <span class="eyebrow">Why hosts support this</span>
      <h2>You are not only screening a film. You are helping it travel.</h2>
      <ul class="checklist">
        <li>Trusted access to films that deserve real rooms</li>
        <li>Rights clarity in minutes instead of days</li>
        <li>Fair rev-share so hosting becomes sustainable</li>
        <li>Ready-made promo assets that still feel premium</li>
      </ul>
    </div>
    <div class="visual-panel visual-panel-compact">
      <img src="assets/placeholders/hosts-event.svg" alt="Illustration of a polished local screening event and host toolkit">
    </div>
  </div>
</section>

<section>
  <div class="container section-head reveal">
    <span class="eyebrow">Use cases</span>
    <h2>The host network should feel expansive without feeling sloppy.</h2>
  </div>
  <div class="pillars-grid reveal">
    <article class="feature-card"><span class="feature-step">A</span><h3>Community screening</h3><p>For local groups, issue circles, and trusted organizers bringing a film into conversation.</p></article>
    <article class="feature-card"><span class="feature-step">B</span><h3>Educational screening</h3><p>For universities, classrooms, libraries, and institutions that need clean licensing and predictable terms.</p></article>
    <article class="feature-card"><span class="feature-step">C</span><h3>Commercial venue screening</h3><p>For theaters, coworking spaces, festivals, and cultural venues with a ticketed event model.</p></article>
    <article class="feature-card"><span class="feature-step">D</span><h3>Private host circle</h3><p>For aligned private groups, donors, or member communities who need a protected viewing context.</p></article>
  </div>
</section>

<section id="host-form" class="section-waitlist">
  <div class="container waitlist-shell reveal">
    <div>
      <span class="eyebrow">For hosts</span>
      <h2>Get the Community Screening Playbook and hear first when host onboarding opens.</h2>
      <p class="body-lg">This is for the people who already know that one film, in one room, at the right moment, can change what becomes sayable in a community.</p>
      <ul class="checklist">
        <li>How to choose the right event type for the audience you actually have</li>
        <li>How the rights request flow should feel when it is built well</li>
        <li>How to fill a room without hypey, low-trust promotion</li>
      </ul>
    </div>
    <div class="form-shell form-shell-strong">
      <h3>Get the host playbook</h3>
      <form action="https://formspree.io/f/YOUR_HOST_FORM_ID" method="POST" class="form-grid">
        <input type="hidden" name="form_name" value="Host Waitlist">
        <label><span class="field-label">Name</span><input type="text" name="name" required></label>
        <label><span class="field-label">Email</span><input type="email" name="email" required></label>
        <label><span class="field-label">Organization / venue</span><input type="text" name="organization"></label>
        <label><span class="field-label">Primary host type</span>
          <select name="host_type">
            <option>Independent venue</option>
            <option>Educator / campus</option>
            <option>Community organizer</option>
            <option>Nonprofit / issue network</option>
            <option>Podcast / creator audience</option>
          </select>
        </label>
        <label><span class="field-label">What kind of films do you want to bring into your world?</span><textarea name="note" placeholder="A quick note on your audience, venue, city, or the kind of films you know your people are ready for."></textarea></label>
        <button class="btn btn-primary btn-block" type="submit">Send me the host playbook</button>
      </form>
    </div>
  </div>
</section>
''' + footer

investors_extra = '''<script type="application/ld+json">{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://YOURDOMAIN.com/index.html"},
    {"@type": "ListItem", "position": 2, "name": "Investors", "item": "https://YOURDOMAIN.com/investors.html"}
  ]
}</script>'''

investors = common_head(
    f'For Investors | {brand_full}',
    'A category bet on creator-controlled film commerce, local screening rights, modular payment rails, and artist-owned distribution infrastructure.',
    'investors.html',
    extra_json=investors_extra,
) + header + '''
<section class="page-hero page-hero-investors">
  <div class="container page-hero-grid">
    <div class="reveal">
      <span class="eyebrow">For investors and strategic partners</span>
      <h1 class="display-title display-title-page">This is not another media bet. It is a seller network for films the current system cannot place cleanly.</h1>
      <p class="lead">UNBURIED sits at the intersection of creator commerce, rights infrastructure, community distribution, and resilient payment rails. The category is film. The architecture is closer to seller tooling.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#investor-form">Request the investor thesis</a>
        <a class="btn btn-secondary" href="#why-now">See why now</a>
      </div>
    </div>
    <div class="visual-panel reveal reveal-delay">
      <img src="assets/placeholders/investors-hero.svg" alt="Abstract illustration of a networked, premium film commerce infrastructure">
    </div>
  </div>
</section>

<section id="why-now">
  <div class="container split-intro reveal">
    <div>
      <span class="eyebrow">Why the category is opening</span>
      <h2>Important films are underserved, direct support is normalized, and the rails under the rails are finally getting better.</h2>
      <p class="body-lg">The old answer was “hope a streamer says yes.” The new answer is a more diversified release machine: direct viewing, local screening rights, educational access, support campaigns, and optional sovereign rails where they actually matter.</p>
    </div>
    <aside class="pull-quote-card">
      <p class="pull-quote">The platform does not need to out-feed incumbents. It needs to own a sharper lane and a better transaction model.</p>
    </aside>
  </div>
</section>

<section>
  <div class="container bento-grid reveal">
    <article class="bento-card bento-wide">
      <span class="kicker">The thesis</span>
      <h3>A premium screen network for culturally important films facing structural distribution resistance.</h3>
      <p>The wedge is high-friction cinema first. The umbrella brand is broader: an independent film network with stronger monetization, cleaner rights mechanics, and audience ownership built in.</p>
    </article>
    <article class="bento-card">
      <span class="kicker">What the market keeps missing</span>
      <h3>There is no integrated operator for this</h3>
      <p>Crowdfunding, streaming, community screenings, and crypto experiments all exist. The filmmaker still has to stitch them together alone.</p>
    </article>
    <article class="bento-card">
      <span class="kicker">Why this can compound</span>
      <h3>Each film strengthens the network</h3>
      <p>Hosts, educators, buyers, supporters, affiliates, and curators become reusable infrastructure for the next release.</p>
    </article>
    <article class="bento-card">
      <span class="kicker">Why this can defend itself</span>
      <h3>Transaction-first beats ad dependence</h3>
      <p>Revenue comes from watching, hosting, licensing, and backing films — not from chasing low-quality scale and fragile brand-safe advertising.</p>
    </article>
  </div>
</section>

<section>
  <div class="container section-head reveal">
    <span class="eyebrow">The shape of the business</span>
    <h2>Broad umbrella. Sharp wedge. Multiple monetization lanes. Modular rails.</h2>
  </div>
  <div class="pillars-grid reveal">
    <article class="feature-card"><span class="feature-step">01</span><h3>Primary revenue</h3><p>VOD rentals, purchases, gifts, and memberships later.</p></article>
    <article class="feature-card"><span class="feature-step">02</span><h3>High-margin layer</h3><p>Community screenings, educational licenses, and local rights packages.</p></article>
    <article class="feature-card"><span class="feature-step">03</span><h3>Support layer</h3><p>Pre-sales, completion funds, and launch-support campaigns for upcoming titles.</p></article>
    <article class="feature-card"><span class="feature-step">04</span><h3>Resilience layer</h3><p>Mainstream payments on top, self-hosted or stablecoin options underneath where they reduce real risk.</p></article>
  </div>
</section>

<section class="section-contrast">
  <div class="container split-band reveal">
    <div>
      <span class="eyebrow">For Jack Dorsey and investors like him</span>
      <h2>If you are bullish on seller infrastructure, artist-owned rails, optional bitcoin payments, and self-custody that does not punish normal users, this should already feel legible.</h2>
      <ul class="checklist">
        <li>It serves creators as sellers, not as content inputs for a feed.</li>
        <li>It benefits from simpler, more open payment infrastructure as that stack matures.</li>
        <li>It treats portability and sovereignty as product advantages, not ideological decoration.</li>
        <li>It can use bitcoin and self-custody as optional leverage, not mandatory consumer friction.</li>
      </ul>
    </div>
    <div class="callout-card investor-card-strong">
      <div class="callout-row"><strong>Closer category analogy</strong><span>seller tools + rights marketplace + artist commerce infrastructure</span></div>
      <div class="callout-row"><strong>Not the analogy</strong><span>generic streaming or ad-supported “alternative YouTube” scale chase</span></div>
      <div class="callout-row"><strong>Underlying bet</strong><span>the creators with the hardest distribution problem are often the most motivated to adopt better rails first</span></div>
    </div>
  </div>
</section>

<section>
  <div class="container section-head reveal">
    <span class="eyebrow">Execution discipline</span>
    <h2>How to build a category-defining product without dying of ambition</h2>
  </div>
  <div class="workflow-grid reveal">
    <article class="workflow-card"><span class="workflow-label">Phase 0</span><h3>Foundation</h3><p>Curated titles, filmmaker onboarding, direct checkout, secure playback, screening requests, reserves, and payouts.</p></article>
    <article class="workflow-card"><span class="workflow-label">Phase 1</span><h3>Closed beta</h3><p>25 to 75 films, local screening pilots, event pages, support campaigns, and role-specific waitlists.</p></article>
    <article class="workflow-card"><span class="workflow-label">Phase 2</span><h3>Resilience</h3><p>Expanded rights logic, better creator analytics, fallback rails, educational licensing, and audience export.</p></article>
    <article class="workflow-card"><span class="workflow-label">Phase 3</span><h3>Treasury + category depth</h3><p>Stablecoin settlement options, higher-end DRM, partner white labels, and regulated investment handoff for selected titles.</p></article>
  </div>
</section>

<section id="investor-form" class="section-waitlist">
  <div class="container waitlist-shell reveal">
    <div>
      <span class="eyebrow">For investors and strategic partners</span>
      <h2>Request the Narrative Sovereignty Thesis.</h2>
      <p class="body-lg">Get the sharp version: category map, business model, risk architecture, phased rollout, and why this looks more like infrastructure than entertainment hype.</p>
      <ul class="checklist">
        <li>The market wedge and why high-friction films go first</li>
        <li>The money logic, reserves, and marketplace architecture</li>
        <li>The case for modular rails and creator-owned relationships</li>
      </ul>
    </div>
    <div class="form-shell form-shell-strong">
      <h3>Request the thesis</h3>
      <form action="https://formspree.io/f/YOUR_INVESTOR_FORM_ID" method="POST" class="form-grid">
        <input type="hidden" name="form_name" value="Investor Inquiry">
        <label><span class="field-label">Name</span><input type="text" name="name" required></label>
        <label><span class="field-label">Email</span><input type="email" name="email" required></label>
        <label><span class="field-label">Organization</span><input type="text" name="organization"></label>
        <label><span class="field-label">Interest type</span>
          <select name="interest">
            <option>Angel / early investor</option>
            <option>Strategic partner</option>
            <option>Payments / wallet infrastructure</option>
            <option>Distribution / venue partner</option>
            <option>Philanthropic / ecosystem support</option>
          </select>
        </label>
        <label><span class="field-label">What about this category feels most investable to you?</span><textarea name="note" placeholder="Seller infrastructure, artist commerce, open money alignment, category timing, cultural thesis, or another angle."></textarea></label>
        <button class="btn btn-primary btn-block" type="submit">Send me the investor thesis</button>
      </form>
    </div>
  </div>
</section>
''' + footer

styles = r'''
:root {
  --bg: #090b12;
  --bg-2: #0f1320;
  --bg-3: #111727;
  --panel: rgba(16, 22, 35, 0.76);
  --panel-strong: rgba(13, 18, 28, 0.92);
  --panel-soft: rgba(255, 255, 255, 0.04);
  --line: rgba(255,255,255,0.1);
  --line-strong: rgba(255,255,255,0.16);
  --text: #f5f7fb;
  --text-dim: #c2cada;
  --text-soft: #8d98ac;
  --gold: #ffbb63;
  --gold-2: #ffd49c;
  --cyan: #76d7ff;
  --violet: #ab92ff;
  --magenta: #ff8fcf;
  --success: #9cf0c7;
  --danger: #ff9ea7;
  --shadow: 0 24px 80px rgba(0,0,0,0.45);
  --shadow-soft: 0 18px 50px rgba(0,0,0,0.25);
  --radius: 28px;
  --radius-md: 22px;
  --radius-sm: 16px;
  --max: 1240px;
  --space: clamp(1rem, 2vw, 1.5rem);
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: 'Inter', ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  line-height: 1.55;
  color: var(--text);
  background:
    radial-gradient(circle at 10% 8%, rgba(118,215,255,0.13), transparent 25%),
    radial-gradient(circle at 88% 12%, rgba(171,146,255,0.12), transparent 22%),
    radial-gradient(circle at 50% 76%, rgba(255,143,207,0.11), transparent 25%),
    linear-gradient(180deg, #0a0d14 0%, #090b12 100%);
  min-height: 100vh;
}
body::before {
  content: '';
  position: fixed;
  inset: 0;
  pointer-events: none;
  opacity: 0.14;
  background-image:
    linear-gradient(rgba(255,255,255,0.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.06) 1px, transparent 1px);
  background-size: 26px 26px;
  mask-image: radial-gradient(circle at center, black, transparent 85%);
}

img { max-width: 100%; display: block; }
a { color: inherit; text-decoration: none; }
button, input, select, textarea { font: inherit; }
button { cursor: pointer; }

.container {
  width: min(calc(100% - 1.5rem), var(--max));
  margin-inline: auto;
}

.progress-line {
  position: fixed;
  top: 0;
  left: 0;
  width: 0;
  height: 3px;
  z-index: 130;
  background: linear-gradient(90deg, var(--gold), var(--cyan), var(--magenta));
  box-shadow: 0 0 18px rgba(255, 187, 99, 0.5);
}

.skip-link {
  position: absolute;
  left: -999px;
  top: 0;
}
.skip-link:focus {
  left: 1rem;
  top: 1rem;
  z-index: 999;
  background: var(--gold);
  color: #111;
  padding: 0.8rem 1rem;
  border-radius: 999px;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 120;
  background: rgba(8, 11, 18, 0.76);
  backdrop-filter: blur(18px);
  border-bottom: 1px solid rgba(255,255,255,0.06);
}
.nav-shell {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 0.9rem 0;
}
.brand {
  display: inline-flex;
  align-items: center;
  gap: 0.8rem;
}
.brand-mark {
  width: 1rem;
  height: 1rem;
  border-radius: 4px;
  transform: rotate(45deg);
  background: linear-gradient(135deg, var(--gold), var(--cyan));
  box-shadow: 0 0 18px rgba(255, 187, 99, 0.55);
}
.brand-lockup {
  display: grid;
  gap: 0.08rem;
}
.brand-word {
  font-weight: 800;
  letter-spacing: 0.12em;
  font-size: 0.92rem;
}
.brand-sub {
  color: var(--text-soft);
  font-size: 0.64rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
}
.nav-toggle {
  width: 3rem;
  height: 3rem;
  border-radius: 999px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 4px;
  color: var(--text);
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.08);
}
.nav-toggle span {
  width: 1.1rem;
  height: 2px;
  border-radius: 99px;
  background: currentColor;
}
.nav-links {
  position: absolute;
  right: 0.75rem;
  top: calc(100% + 0.45rem);
  display: none;
  flex-direction: column;
  gap: 0.5rem;
  width: min(92vw, 24rem);
  background: rgba(12, 16, 26, 0.96);
  border: 1px solid rgba(255,255,255,0.08);
  box-shadow: var(--shadow);
  border-radius: 22px;
  padding: 0.8rem;
}
.nav-links.is-open { display: flex; }
.nav-links a {
  padding: 0.8rem 0.9rem;
  border-radius: 14px;
  color: var(--text-dim);
}
.nav-links a:hover,
.nav-links a:focus-visible {
  background: rgba(255,255,255,0.05);
  color: var(--text);
}
.nav-cta {
  color: var(--text) !important;
  background: linear-gradient(135deg, rgba(255,187,99,0.18), rgba(118,215,255,0.18));
  border: 1px solid rgba(255,255,255,0.1);
}

main { overflow: clip; }
section { padding: clamp(3.8rem, 8vw, 7rem) 0; position: relative; }

.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  font-size: 0.78rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--gold-2);
  background: rgba(255, 187, 99, 0.08);
  border: 1px solid rgba(255, 187, 99, 0.14);
  padding: 0.55rem 0.85rem;
  border-radius: 999px;
}
.eyebrow::before {
  content: '';
  width: 0.45rem;
  height: 0.45rem;
  border-radius: 999px;
  background: var(--gold);
  box-shadow: 0 0 12px rgba(255, 187, 99, 0.55);
}
.eyebrow-muted {
  color: var(--text-dim);
  background: rgba(255,255,255,0.04);
  border-color: rgba(255,255,255,0.08);
}
.eyebrow-muted::before { background: var(--cyan); box-shadow: 0 0 12px rgba(118,215,255,0.45); }
.kicker, .field-label {
  display: inline-block;
  color: var(--gold-2);
  font-size: 0.76rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

h1, h2, h3, h4 {
  margin: 0;
  font-family: 'Space Grotesk', 'Inter', sans-serif;
  letter-spacing: -0.045em;
  line-height: 1.02;
}
h1 { font-size: clamp(3rem, 10vw, 6.6rem); max-width: 12ch; }
h2 { font-size: clamp(2rem, 6vw, 4.2rem); max-width: 16ch; }
h3 { font-size: clamp(1.2rem, 3vw, 1.72rem); }
.display-title {
  margin-top: 1rem;
  background: linear-gradient(180deg, #fff, #dce6ff 80%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
.display-title-page { max-width: 13ch; }
.lead, .body-lg {
  font-size: clamp(1.08rem, 2vw, 1.28rem);
  color: var(--text-dim);
  max-width: 62ch;
}
.body-md, p, li { color: var(--text-dim); }

.hero, .page-hero {
  padding-top: clamp(4.2rem, 10vw, 8rem);
}
.hero-shell, .page-hero-grid {
  display: grid;
  gap: 1.5rem;
  align-items: center;
}
.hero-copy, .page-hero-grid > div:first-child { position: relative; z-index: 1; }
.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin: 1.4rem 0 1.15rem;
}
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 3.2rem;
  padding: 0.9rem 1.15rem;
  border-radius: 999px;
  font-weight: 700;
  letter-spacing: -0.01em;
  transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
}
.btn:hover { transform: translateY(-2px); }
.btn-primary {
  color: #111;
  background: linear-gradient(135deg, var(--gold), #ffd089 50%, #fff2d2 100%);
  box-shadow: 0 12px 35px rgba(255, 187, 99, 0.28);
}
.btn-secondary {
  color: var(--text);
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.12);
}
.btn-small { min-height: 2.85rem; }
.btn-block { width: 100%; }
.text-link {
  color: var(--text);
  font-weight: 700;
  text-decoration: underline;
  text-underline-offset: 0.18em;
  text-decoration-thickness: 1px;
}

.persona-switch {
  display: inline-flex;
  gap: 0.4rem;
  flex-wrap: wrap;
  margin-top: 1rem;
}
.persona-pill, .compare-tab {
  border: 1px solid rgba(255,255,255,0.1);
  background: rgba(255,255,255,0.04);
  color: var(--text-dim);
  border-radius: 999px;
  min-height: 2.8rem;
  padding: 0.65rem 0.95rem;
  font-weight: 700;
}
.persona-pill.is-active, .compare-tab.is-active {
  color: var(--text);
  border-color: rgba(255,255,255,0.18);
  background: linear-gradient(135deg, rgba(255,187,99,0.16), rgba(118,215,255,0.18));
}
.hero-proof-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
}
.hero-proof-list span, .chip-card {
  display: inline-flex;
  align-items: center;
  border-radius: 999px;
  padding: 0.65rem 0.9rem;
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.08);
  color: var(--text-dim);
}
.hero-proof-list.compact span { padding: 0.55rem 0.82rem; }
.trust-strip {
  display: grid;
  gap: 0.8rem;
  margin-top: 1.3rem;
}
.trust-strip div {
  padding: 0.95rem 1rem;
  border-radius: 18px;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
}
.trust-strip strong { display: block; color: var(--text); }
.trust-strip span { color: var(--text-soft); font-size: 0.95rem; }

.hero-stage {
  position: relative;
  min-height: 24rem;
  border-radius: 30px;
  background: radial-gradient(circle at 30% 20%, rgba(118,215,255,0.18), transparent 28%),
              radial-gradient(circle at 80% 22%, rgba(255,143,207,0.16), transparent 24%),
              linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
  border: 1px solid rgba(255,255,255,0.08);
  box-shadow: var(--shadow);
  overflow: hidden;
}
.hero-stage-glow {
  position: absolute;
  inset: auto -10% -15% auto;
  width: 22rem;
  height: 22rem;
  background: radial-gradient(circle, rgba(255,187,99,0.45), transparent 60%);
  filter: blur(20px);
}
.screen-stack {
  position: relative;
  min-height: 24rem;
}
.floating-screen {
  position: absolute;
  padding: 1rem;
  width: min(18rem, 72vw);
  border-radius: 24px;
  background: rgba(11,16,25,0.78);
  border: 1px solid rgba(255,255,255,0.08);
  box-shadow: var(--shadow-soft);
  backdrop-filter: blur(14px);
}
.screen-a { top: 1.25rem; left: 1rem; transform: rotate(-4deg); }
.screen-b { top: 7.5rem; right: 1rem; transform: rotate(3deg); }
.screen-c { bottom: 1.2rem; left: 1.8rem; transform: rotate(-2deg); }
.screen-label {
  display: inline-flex;
  color: var(--gold-2);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  font-size: 0.72rem;
  margin-bottom: 0.55rem;
}
.floating-screen strong { display: block; color: var(--text); font-size: 1.15rem; margin-bottom: 0.4rem; }
.floating-screen p { margin: 0; font-size: 0.95rem; }
.orbit-card {
  position: absolute;
  right: 1rem;
  bottom: 1rem;
  max-width: 19rem;
  display: flex;
  align-items: flex-start;
  gap: 0.7rem;
  padding: 0.95rem 1rem;
  border-radius: 20px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
}
.orbit-dot {
  width: 0.75rem;
  height: 0.75rem;
  flex: 0 0 auto;
  border-radius: 999px;
  margin-top: 0.2rem;
  background: var(--cyan);
  box-shadow: 0 0 16px rgba(118,215,255,0.55);
}
.orbit-card p { margin: 0; font-size: 0.96rem; }

.logo-rail { padding-top: 1rem; }
.chip-scroll {
  display: flex;
  gap: 0.75rem;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  padding: 1rem 0 0.1rem;
  scrollbar-width: none;
}
.chip-scroll::-webkit-scrollbar { display: none; }
.chip-card { scroll-snap-align: start; min-width: 16rem; }

.section-head {
  display: grid;
  gap: 1rem;
  margin-bottom: 1.6rem;
}
.section-head h2 { max-width: 15ch; }
.split-intro,
.split-band,
.waitlist-shell,
.footer-grid,
.workflow-grid,
.pillars-grid,
.resource-grid,
.quote-grid,
.bento-grid,
.page-hero-grid,
.hero-shell,
.feature-list,
.faq-grid,
.compare-toggle,
.section-head-row,
.investor-callout {
  display: grid;
  gap: 1rem;
}

.pull-quote-card,
.bento-card,
.feature-card,
.workflow-card,
.resource-card,
.quote-card,
.panel,
.visual-panel,
.callout-card,
.form-shell,
.feature-row,
.stack-list > div,
.trust-strip div,
.compare-panel,
.site-footer,
.faq-item,
.table-wrap,
.mobile-cta-bar,
.investor-card-strong {
  border: 1px solid rgba(255,255,255,0.09);
  background: rgba(14, 19, 31, 0.78);
  backdrop-filter: blur(14px);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-soft);
}
.pull-quote-card,
.bento-card,
.feature-card,
.workflow-card,
.resource-card,
.quote-card,
.visual-panel,
.callout-card,
.form-shell,
.feature-row,
.compare-panel,
.table-wrap,
.investor-card-strong {
  padding: 1.15rem;
}
.pull-quote {
  font-size: clamp(1.3rem, 4vw, 2rem);
  color: var(--text);
  letter-spacing: -0.03em;
  line-height: 1.12;
}
.quote-foot { color: var(--text-soft); margin-top: 0.6rem; }
.bento-grid { grid-template-columns: 1fr; }
.bento-card h3, .feature-card h3, .workflow-card h3, .resource-card h3, .quote-card h3 { margin-top: 0.6rem; margin-bottom: 0.55rem; }
.bento-wide { min-height: 100%; }
.feature-card, .workflow-card { min-height: 100%; }
.feature-step {
  display: inline-flex;
  width: 2rem;
  height: 2rem;
  border-radius: 999px;
  align-items: center;
  justify-content: center;
  background: rgba(255, 187, 99, 0.12);
  color: var(--gold-2);
  font-size: 0.78rem;
  font-weight: 800;
}
.feature-list { grid-template-columns: 1fr; }
.feature-row {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 0.9rem;
  align-items: start;
}
.feature-row p { margin-bottom: 0; }
.workflow-label {
  display: inline-flex;
  color: var(--cyan);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 0.72rem;
}
.resource-card { position: relative; overflow: hidden; }
.resource-card::after {
  content: '';
  position: absolute;
  inset: auto -2rem -2rem auto;
  width: 6rem;
  height: 6rem;
  background: radial-gradient(circle, rgba(255,187,99,0.28), transparent 65%);
}
.quote-grid { grid-template-columns: 1fr; }
.quote-card p { margin-bottom: 0; }
.callout-row {
  display: grid;
  gap: 0.35rem;
  margin-bottom: 0.9rem;
}
.callout-row strong { color: var(--text); }
.investor-card-strong {
  background: linear-gradient(180deg, rgba(22, 28, 42, 0.94), rgba(11, 15, 24, 0.92));
}

.compare-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  margin-bottom: 0.9rem;
}
.compare-panel { display: none; }
.compare-panel.is-active { display: block; }
.stack-list {
  display: grid;
  gap: 0.85rem;
}
.stack-list > div {
  padding: 1rem;
}
.stack-list strong { display: block; color: var(--text); margin-bottom: 0.25rem; }
.stack-list span { color: var(--text-soft); }

.workflow-grid,
.pillars-grid,
.resource-grid,
.quote-grid,
.bento-grid,
.footer-grid,
.investor-callout,
.split-band,
.split-intro,
.waitlist-shell,
.hero-shell,
.page-hero-grid {
  grid-template-columns: 1fr;
}

.checklist,
.bullet-list,
.numbered-list {
  margin: 0;
  padding-left: 1.15rem;
}
.checklist li,
.bullet-list li,
.numbered-list li {
  margin-bottom: 0.6rem;
}

.visual-panel img {
  width: 100%;
  height: auto;
  border-radius: 18px;
}
.visual-panel-compact { max-width: 34rem; }

.table-wrap { overflow-x: auto; }
.table {
  width: 100%;
  border-collapse: collapse;
  min-width: 700px;
}
.table th,
.table td {
  text-align: left;
  padding: 0.95rem 0.85rem;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  color: var(--text-dim);
  vertical-align: top;
}
.table th {
  color: var(--text);
  font-size: 0.9rem;
}

.form-shell h3 { margin-bottom: 0.8rem; }
.form-shell-strong {
  background: linear-gradient(180deg, rgba(18, 24, 39, 0.96), rgba(11, 15, 24, 0.96));
}
.form-grid {
  display: grid;
  gap: 0.9rem;
}
label { display: grid; gap: 0.45rem; }
input, select, textarea {
  width: 100%;
  border: 1px solid rgba(255,255,255,0.1);
  background: rgba(255,255,255,0.04);
  color: var(--text);
  border-radius: 16px;
  padding: 0.95rem 1rem;
  outline: none;
}
textarea { min-height: 8rem; resize: vertical; }
input:focus, select:focus, textarea:focus {
  border-color: rgba(118,215,255,0.55);
  box-shadow: 0 0 0 3px rgba(118,215,255,0.12);
}
.micro-note { color: var(--text-soft); font-size: 0.86rem; margin: 0; }

.faq-grid { grid-template-columns: 1fr; }
.faq-item summary {
  list-style: none;
  cursor: pointer;
  color: var(--text);
  font-weight: 700;
}
.faq-item summary::-webkit-details-marker { display: none; }
.faq-item { padding: 1rem 1.1rem; }
.faq-item[open] { background: rgba(255,255,255,0.06); }
.faq-item p { margin-bottom: 0; }

.site-footer {
  margin: 0.75rem;
  padding: 1.35rem 0 calc(6rem + env(safe-area-inset-bottom));
  background: rgba(8, 11, 18, 0.94);
}
.footer-grid a,
.footer-copy,
.footer-note { color: var(--text-dim); }
.footer-grid > div {
  display: grid;
  gap: 0.45rem;
}
.footer-brand {
  font-family: 'Space Grotesk', sans-serif;
  font-size: 1.15rem;
  color: var(--text);
}
.footer-label {
  color: var(--gold-2);
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 0.74rem;
}
.mobile-cta-bar {
  position: fixed;
  left: 0.75rem;
  right: 0.75rem;
  bottom: calc(0.75rem + env(safe-area-inset-bottom));
  z-index: 115;
  padding: 0.7rem;
  background: rgba(10, 14, 22, 0.9);
}

.reveal {
  opacity: 0;
  transform: translateY(18px);
  transition: opacity 0.75s ease, transform 0.75s ease;
}
.reveal.is-visible {
  opacity: 1;
  transform: translateY(0);
}
.reveal-delay { transition-delay: 0.1s; }

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  .reveal { opacity: 1; transform: none; transition: none; }
  .btn, .persona-pill, .compare-tab { transition: none; }
}

@media (min-width: 720px) {
  .hero-shell,
  .page-hero-grid,
  .split-intro,
  .split-band,
  .waitlist-shell,
  .investor-callout { grid-template-columns: 1.08fr 0.92fr; }
  .trust-strip { grid-template-columns: repeat(3, 1fr); }
  .workflow-grid,
  .pillars-grid,
  .resource-grid,
  .quote-grid,
  .footer-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .bento-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .bento-wide { grid-column: span 2; }
  .mobile-cta-bar { left: auto; right: 1rem; width: 16rem; }
}

@media (min-width: 980px) {
  .nav-toggle { display: none; }
  .nav-links {
    position: static;
    display: flex;
    width: auto;
    flex-direction: row;
    background: none;
    border: 0;
    box-shadow: none;
    padding: 0;
    gap: 0.25rem;
  }
  .nav-links a { padding: 0.78rem 0.9rem; }
  .hero-shell { grid-template-columns: 1.02fr 0.98fr; }
  .hero-stage { min-height: 31rem; }
  .screen-stack { min-height: 31rem; }
  .floating-screen { width: 18rem; }
  .screen-a { top: 2rem; left: 2rem; }
  .screen-b { top: 8.5rem; right: 2rem; }
  .screen-c { bottom: 2.2rem; left: 4rem; }
  .orbit-card { right: 2rem; bottom: 1.8rem; }
  .workflow-grid,
  .pillars-grid,
  .resource-grid,
  .quote-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .resource-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .pillars-grid { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .footer-grid { grid-template-columns: 1.2fr 0.8fr 1fr 1fr; }
  .mobile-cta-bar { display: none; }
}
'''

script = r'''
const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.nav-links');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(open));
  });
  nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
    nav.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
  }));
}

const progress = document.querySelector('.progress-line');
const syncProgress = () => {
  if (!progress) return;
  const doc = document.documentElement;
  const total = doc.scrollHeight - window.innerHeight;
  const percent = total > 0 ? (window.scrollY / total) * 100 : 0;
  progress.style.width = `${Math.min(100, Math.max(0, percent))}%`;
};
window.addEventListener('scroll', syncProgress, { passive: true });
window.addEventListener('resize', syncProgress);
syncProgress();

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

const personaContent = {
  filmmakers: {
    title: 'Your film should not need permission to circulate.',
    copy: 'UNBURIED gives high-friction films a premium path from buried and fragmented to watchable, licensable, hostable, and paid — without forcing the filmmaker to become a full-time distribution company.',
    primary: { label: 'Get the Sovereign Release Brief', href: '#waitlist' },
    secondary: { label: 'See the filmmaker model', href: 'filmmakers.html' },
    bullets: [
      'Keep rights by default',
      'Own your audience relationship',
      'Monetize through watch, host, license, and support'
    ]
  },
  hosts: {
    title: 'Bring important films to your city without drowning in rights confusion.',
    copy: 'UNBURIED turns community screenings into a clean, premium flow for venues, educators, organizers, and cultural nodes who want to fill rooms with films that matter.',
    primary: { label: 'Get the Community Screening Playbook', href: '#waitlist' },
    secondary: { label: 'See the host flow', href: 'hosts.html' },
    bullets: [
      'Request rights without legal drag',
      'Launch ticketed events fast',
      'Earn fairly while helping films travel'
    ]
  },
  investors: {
    title: 'A seller network for films the current system cannot place cleanly.',
    copy: 'UNBURIED sits at the intersection of creator commerce, rights infrastructure, local screening distribution, and resilient payment rails. The category is film. The architecture is closer to seller tooling.',
    primary: { label: 'Request the investor thesis', href: '#waitlist' },
    secondary: { label: 'See the investor page', href: 'investors.html' },
    bullets: [
      'Transaction-first business model',
      'Broad umbrella with a sharp wedge',
      'Modular rails and portable relationships'
    ]
  }
};

const switcher = document.querySelector('[data-persona-switch]');
if (switcher) {
  const title = document.querySelector('[data-persona-title]');
  const copy = document.querySelector('[data-persona-copy]');
  const primary = document.querySelector('[data-persona-primary]');
  const secondary = document.querySelector('[data-persona-secondary]');
  const bullets = document.querySelector('[data-persona-bullets]');
  const renderPersona = (key) => {
    const state = personaContent[key];
    if (!state) return;
    switcher.querySelectorAll('[data-persona]').forEach(btn => {
      btn.classList.toggle('is-active', btn.dataset.persona === key);
    });
    if (title) title.textContent = state.title;
    if (copy) copy.textContent = state.copy;
    if (primary) { primary.textContent = state.primary.label; primary.setAttribute('href', state.primary.href); }
    if (secondary) { secondary.textContent = state.secondary.label; secondary.setAttribute('href', state.secondary.href); }
    if (bullets) {
      bullets.innerHTML = '';
      state.bullets.forEach(item => {
        const span = document.createElement('span');
        span.textContent = item;
        bullets.appendChild(span);
      });
    }
  };
  switcher.addEventListener('click', (event) => {
    const button = event.target.closest('[data-persona]');
    if (!button) return;
    renderPersona(button.dataset.persona);
  });
  renderPersona('filmmakers');
}

const compare = document.querySelector('[data-compare]');
if (compare) {
  compare.addEventListener('click', (event) => {
    const button = event.target.closest('.compare-tab');
    if (!button) return;
    const target = button.dataset.target;
    compare.querySelectorAll('.compare-tab').forEach(tab => tab.classList.toggle('is-active', tab === button));
    compare.querySelectorAll('.compare-panel').forEach(panel => panel.classList.toggle('is-active', panel.dataset.panel === target));
  });
}
'''

llms = f'''# {brand_full}

{brand_full} is a filmmaker-first distribution network for culturally important independent films facing structural distribution resistance.

## Primary audience
- independent filmmakers
- rights-holding teams
- community screening hosts
- educators and venues
- investors interested in creator-owned infrastructure, seller tools, and resilient payment rails

## Core promise
Keep rights. Own audience. Activate direct viewing, local screening rights, educational licensing, support campaigns, and resilient settlement rails in one premium system.

## Core pages
- /index.html: brand overview, dream client positioning, waitlist
- /filmmakers.html: filmmaker-specific problem, transformation, and model
- /hosts.html: host and community screening workflow
- /investors.html: investor thesis and category framing

## Call to action
Join early to receive one of the role-specific briefs:
- The Sovereign Release Brief
- The Community Screening Playbook
- The Narrative Sovereignty Thesis
'''

llms_full = f'''# {brand_full} — full LLM reference

## One-paragraph summary
{brand_full} is a premium, filmmaker-first screen network for culturally important independent films that face structural distribution resistance. The system combines curated trust, direct viewing, local screening rights, educational licensing, support campaigns, audience ownership, and modular payment rails. The wedge is high-friction films first. The umbrella brand is broader: independent cinema that deserves a real release path and a rights-respecting home.

## Dream client
Primary dream clients are independent filmmakers and small rights-holding teams with high-friction, culturally important films facing structural distribution resistance. Their core 2 a.m. problem is lacking a safe, sovereign, financially viable way to get important films seen and paid for without gatekeepers burying them or forcing them to become full-time distribution companies.

## Desired transformation
Dream clients want to become sovereign creators with resilient release pathways, direct audience relationships, diversified revenue, and trusted community distribution networks.

## Regenerative purpose
Restore narrative sovereignty and circulate culturally vital films through fair, community-rooted, non-extractive distribution systems.

## Revenue model snapshot
- VOD rental / purchase: suggested split 85 / 10 / 5
- Community screening: suggested split 60 / 25 / 15
- Educational licensing: suggested split 70 / 20 / 10
- Support campaign: suggested split 95 / 5

## Key product pillars
1. Curated trust
2. Rights-aware monetization
3. Community-powered circulation
4. Resilient, modular rails
5. Audience ownership

## Notes for crawlers and LLMs
- This brand is not trying to be a generic streaming service.
- The closest framing is a seller network and rights-aware distribution operating system for independent film.
- The top-level CTA is early access via role-specific briefs.
'''

robots = 'User-agent: *\nAllow: /\nSitemap: https://YOURDOMAIN.com/sitemap.xml\n'

sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{domain}/index.html</loc></url>
  <url><loc>{domain}/filmmakers.html</loc></url>
  <url><loc>{domain}/hosts.html</loc></url>
  <url><loc>{domain}/investors.html</loc></url>
</urlset>
'''

manifest = '''{
  "name": "UNBURIED Screen Network",
  "short_name": "UNBURIED",
  "start_url": "/index.html",
  "display": "standalone",
  "background_color": "#090b12",
  "theme_color": "#090b12",
  "icons": [{
    "src": "assets/icons/favicon.svg",
    "sizes": "any",
    "type": "image/svg+xml",
    "purpose": "any"
  }]
}
'''

favicon = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96" fill="none">
  <rect width="96" height="96" rx="28" fill="#0B101A"/>
  <defs>
    <linearGradient id="g" x1="12" y1="12" x2="84" y2="84" gradientUnits="userSpaceOnUse">
      <stop stop-color="#FFBB63"/>
      <stop offset="0.52" stop-color="#76D7FF"/>
      <stop offset="1" stop-color="#AB92FF"/>
    </linearGradient>
  </defs>
  <path d="M48 15L80 47.5L48 80L16 47.5L48 15Z" fill="url(#g)"/>
  <path d="M48 30.5L64.5 47.5L48 64.5L31.5 47.5L48 30.5Z" fill="#0B101A"/>
</svg>'''

svg_templates = {
    'home-hero.svg': ('#76D7FF', '#AB92FF', '#FFBB63', 'Networked premium film distribution'),
    'filmmakers-hero.svg': ('#FFBB63', '#FF8FCF', '#76D7FF', 'Rights-aware release engine for filmmakers'),
    'hosts-hero.svg': ('#76D7FF', '#FFBB63', '#AB92FF', 'City-based community screening network'),
    'hosts-event.svg': ('#AB92FF', '#76D7FF', '#FFBB63', 'Premium host event toolkit'),
    'investors-hero.svg': ('#FF8FCF', '#FFBB63', '#76D7FF', 'Film commerce infrastructure'),
    'payments-rails.svg': ('#76D7FF', '#FFBB63', '#FF8FCF', 'Layered payment and resilience rails'),
    'og-cover.svg': ('#FFBB63', '#76D7FF', '#AB92FF', 'UNBURIED Screen Network')
}

svg_base = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 960" fill="none">
  <defs>
    <linearGradient id="bg" x1="80" y1="120" x2="1360" y2="860" gradientUnits="userSpaceOnUse">
      <stop stop-color="#0A0D14"/>
      <stop offset="1" stop-color="#101727"/>
    </linearGradient>
    <radialGradient id="glow1" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(360 260) rotate(38) scale(540 420)">
      <stop stop-color="{c1}" stop-opacity="0.42"/>
      <stop offset="1" stop-color="{c1}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow2" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(1080 300) rotate(12) scale(480 320)">
      <stop stop-color="{c2}" stop-opacity="0.36"/>
      <stop offset="1" stop-color="{c2}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glow3" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(760 760) rotate(-15) scale(540 300)">
      <stop stop-color="{c3}" stop-opacity="0.25"/>
      <stop offset="1" stop-color="{c3}" stop-opacity="0"/>
    </radialGradient>
    <filter id="blur" x="-100" y="-100" width="1640" height="1160" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
      <feGaussianBlur stdDeviation="40"/>
    </filter>
  </defs>
  <rect width="1440" height="960" rx="48" fill="url(#bg)"/>
  <ellipse cx="360" cy="260" rx="480" ry="340" fill="url(#glow1)" filter="url(#blur)"/>
  <ellipse cx="1080" cy="300" rx="420" ry="280" fill="url(#glow2)" filter="url(#blur)"/>
  <ellipse cx="760" cy="760" rx="520" ry="260" fill="url(#glow3)" filter="url(#blur)"/>
  <g opacity="0.16" stroke="white">
    <path d="M120 820C280 600 420 540 650 520C915 497 1050 580 1320 300" stroke-width="2"/>
    <path d="M200 220C380 310 560 340 775 290C975 242 1150 180 1270 140" stroke-width="2"/>
    <path d="M170 660C410 650 560 710 770 800C960 880 1160 860 1290 700" stroke-width="2"/>
  </g>
  <g>
    <rect x="150" y="150" width="420" height="250" rx="28" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.18)"/>
    <rect x="505" y="305" width="420" height="250" rx="28" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.16)" transform="rotate(-4 505 305)"/>
    <rect x="865" y="160" width="380" height="230" rx="28" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.16)" transform="rotate(4 865 160)"/>
  </g>
  <g opacity="0.8">
    <rect x="218" y="220" width="198" height="10" rx="5" fill="white"/>
    <rect x="218" y="252" width="130" height="8" rx="4" fill="rgba(255,255,255,0.56)"/>
    <rect x="218" y="278" width="220" height="8" rx="4" fill="rgba(255,255,255,0.28)"/>
    <rect x="562" y="380" width="240" height="10" rx="5" fill="white"/>
    <rect x="562" y="412" width="168" height="8" rx="4" fill="rgba(255,255,255,0.56)"/>
    <rect x="562" y="438" width="260" height="8" rx="4" fill="rgba(255,255,255,0.28)"/>
    <rect x="932" y="230" width="190" height="10" rx="5" fill="white"/>
    <rect x="932" y="262" width="148" height="8" rx="4" fill="rgba(255,255,255,0.56)"/>
    <rect x="932" y="288" width="206" height="8" rx="4" fill="rgba(255,255,255,0.28)"/>
  </g>
  <g>
    <circle cx="472" cy="655" r="8" fill="{c1}"/>
    <circle cx="663" cy="595" r="8" fill="{c2}"/>
    <circle cx="864" cy="640" r="8" fill="{c3}"/>
    <circle cx="1090" cy="575" r="8" fill="white"/>
  </g>
  <text x="120" y="890" font-family="Inter, Arial, sans-serif" font-size="34" fill="white" opacity="0.88">{label}</text>
</svg>'''

for name, (c1, c2, c3, label) in svg_templates.items():
    (assets / name).write_text(svg_base.format(c1=c1, c2=c2, c3=c3, label=label))

readme = f'''# {brand_full}

This site has been comprehensively refined for a premium, mobile-first GitHub Pages launch.

## What changed in this pass
- tightened brand architecture to **UNBURIED Screen Network**
- removed visible internal, placeholder, and instructional language from the user-facing copy
- rewrote the homepage and supporting pages for filmmakers, hosts, and investors with sharper dream-target positioning
- added mobile-first hero architecture with persona switching, reveal animations, comparison widgets, sticky CTA, and structured machine-readable content
- upgraded image placeholders and added a Canva prompt handoff file
- updated llms.txt, llms-full.txt, robots.txt, sitemap.xml, and structured data

## Before launch
1. Replace `YOURDOMAIN.com` with the live domain.
2. Replace Formspree IDs on each page.
3. Review the brand name for domain and trademark clearance.
4. Add final images in `assets/placeholders/` or replace them with exported Canva assets.
5. Connect analytics, privacy policy, and any consent tooling you want to use.

## Suggested page order for review
1. `index.html`
2. `filmmakers.html`
3. `hosts.html`
4. `investors.html`
5. `canva-prompts.txt`

## Hosting
This site is static and GitHub Pages friendly.
'''

canva = '''UNBURIED Screen Network — Canva image prompt handoff

Brand direction
- premium, cinematic, editorial, mobile-first, anti-slop
- intelligent dark interface energy, not generic sci-fi
- luminous but disciplined palette: ember gold, electric cyan, ultraviolet, soft pearl on deep midnight blue-black
- images should feel like high-end film commerce infrastructure, not crypto hype and not activist cliché
- no visible UI gibberish, no misspelled text, no random floating graphs, no cheesy stock-photo faces
- aspect ratios should match the existing file names unless intentionally replaced with a larger export

1) URL: /index.html
   Image file: assets/placeholders/home-hero.svg
   Prompt:
   Create a cinematic editorial hero image for a premium independent film distribution platform called UNBURIED Screen Network. Show a sophisticated, mobile-first-feeling digital ecosystem for films that move through communities: layered translucent screens, elegant city nodes, premium playback cards, local screening routes, and subtle payment rails. No people. No text in the image. No cheesy icons. Mood is intelligent, high-signal, premium, and slightly rebellious. Deep midnight background with ember gold, electric cyan, and violet light. Feels like the future of independent cinema distribution, not generic tech SaaS.

2) URL: /filmmakers.html
   Image file: assets/placeholders/filmmakers-hero.svg
   Prompt:
   Create a premium cinematic image for filmmakers carrying important, high-friction films. Visualize a sovereign release engine: a film moving from a vault-like archive into multiple elegant release channels including direct viewing, screening rights, educational licensing, and supporter momentum. No people. No text. No propaganda imagery. The feeling should be relief, control, and strategic power. Luxurious glassmorphism, layered cards, subtle gradients, intelligent shadows, rich midnight tones with ember gold and magenta accents.

3) URL: /hosts.html
   Image file: assets/placeholders/hosts-hero.svg
   Prompt:
   Create a cinematic image showing a community screening network across multiple cities. Think cultural venues, campuses, local organizers, and premium event infrastructure translated into abstract visual form. No crowds. No cheesy theater popcorn clichés. No visible words. Show clean pathways, elegant venue markers, and a feeling of one film rippling through many trusted rooms. Mobile-first premium design language, dark editorial palette, electric cyan and gold accents.

4) URL: /hosts.html
   Image file: assets/placeholders/hosts-event.svg
   Prompt:
   Create an elevated event-toolkit style image for a premium film host platform. Visualize ticketing, venue setup, screening access, and approved promotional assets as beautifully arranged layered interface cards and atmospheric physical cues. No text. No people. No random charts. The image should feel calm, credible, polished, and built for cultural leaders.

5) URL: /investors.html
   Image file: assets/placeholders/investors-hero.svg
   Prompt:
   Create a high-end investor-facing visual for a film commerce infrastructure brand. Show a network of premium assets, rights flows, transaction lanes, audience nodes, and modular rails. It should feel like seller tooling and cultural infrastructure rather than entertainment fluff. No text. No dollar signs. No people. The image should appeal to investors who understand creator-owned infrastructure, open money, and resilient digital rails.

6) URL: /filmmakers.html and /index.html
   Image file: assets/placeholders/payments-rails.svg
   Prompt:
   Create a sophisticated abstract visualization of layered payment and resilience rails for a film distribution platform. Show clean mainstream payment flow, optional sovereign or bitcoin-friendly rails, reserves, settlement timing, and creator payouts without using literal charts or cheesy crypto tropes. No text. No coins flying around. It should feel stable, modern, and intelligently designed.

7) Social sharing image
   Image file: assets/placeholders/og-cover.svg
   Prompt:
   Create a dramatic social share image for UNBURIED Screen Network. The visual should instantly communicate premium independent cinema, cultural urgency, and infrastructure-level ambition. Abstract cinematic panels, luminous circulation paths, elegant glow, deep black-blue background, subtle ember and cyan highlights. No visible words. No people. It must read beautifully as a horizontal social cover.
'''

(site / 'index.html').write_text(home)
(site / 'filmmakers.html').write_text(filmmakers)
(site / 'hosts.html').write_text(hosts)
(site / 'investors.html').write_text(investors)
(site / 'styles.css').write_text(styles)
(site / 'script.js').write_text(script)
(site / 'llms.txt').write_text(llms)
(site / 'llms-full.txt').write_text(llms_full)
(site / 'robots.txt').write_text(robots)
(site / 'sitemap.xml').write_text(sitemap)
(site / 'site.webmanifest').write_text(manifest)
(site / 'README.md').write_text(readme)
(site / 'canva-prompts.txt').write_text(canva)
(icons / 'favicon.svg').write_text(favicon)

print('refined site written')
