from pathlib import Path

root = Path('/mnt/data/unburied-site')
(root / 'assets' / 'placeholders').mkdir(parents=True, exist_ok=True)
(root / 'assets' / 'icons').mkdir(parents=True, exist_ok=True)

site_name = 'UNBURIED'
base_url = 'https://YOURDOMAIN.com'
waitlist_action = 'https://formspree.io/f/YOUR_WAITLIST_FORM_ID'
filmmaker_action = 'https://formspree.io/f/YOUR_FILMMAKER_FORM_ID'
investor_action = 'https://formspree.io/f/YOUR_INVESTOR_FORM_ID'

nav = '''
<header class="site-header" id="top">
  <div class="container nav-shell">
    <a class="brand" href="index.html" aria-label="UNBURIED home">
      <span class="brand-mark" aria-hidden="true"></span>
      <span class="brand-word">UNBURIED</span>
    </a>
    <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav-links" id="nav-links">
      <a href="index.html">Home</a>
      <a href="filmmakers.html">Filmmakers</a>
      <a href="hosts.html">Hosts</a>
      <a href="investors.html">Investors</a>
      <a href="index.html#waitlist" class="nav-cta">Join the Waitlist</a>
    </nav>
  </div>
</header>
'''

footer = '''
<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <a class="brand brand-footer" href="index.html">
        <span class="brand-mark" aria-hidden="true"></span>
        <span class="brand-word">UNBURIED</span>
      </a>
      <p class="footer-copy">Sovereign distribution for important films. Built to help culturally vital cinema travel, earn, and outlast the choke points that bury it.</p>
    </div>
    <div>
      <h3>Explore</h3>
      <ul>
        <li><a href="filmmakers.html">For Filmmakers</a></li>
        <li><a href="hosts.html">For Hosts</a></li>
        <li><a href="investors.html">For Investors</a></li>
        <li><a href="index.html#faq">FAQ</a></li>
      </ul>
    </div>
    <div>
      <h3>Lead Magnets</h3>
      <ul>
        <li><a href="index.html#lead-magnet">Narrative Friction Index</a></li>
        <li><a href="filmmakers.html#diagnostic">Release Risk Brief</a></li>
        <li><a href="investors.html#thesis">Narrative Sovereignty Thesis</a></li>
      </ul>
    </div>
    <div>
      <h3>Infrastructure</h3>
      <ul>
        <li><a href="robots.txt">robots.txt</a></li>
        <li><a href="sitemap.xml">sitemap.xml</a></li>
        <li><a href="llms.txt">llms.txt</a></li>
      </ul>
    </div>
  </div>
  <div class="container footer-bottom">
    <p>Working brand concept. Verify trademark and domain availability before launch.</p>
    <p>Hosted on GitHub Pages. Forms powered by Formspree.</p>
  </div>
</footer>
'''

scripts = '<script src="script.js" defer></script>'

style = r'''
:root {
  --bg: #06070a;
  --bg-soft: #0d1016;
  --panel: rgba(16, 21, 31, 0.74);
  --panel-strong: rgba(11, 16, 23, 0.92);
  --line: rgba(255, 255, 255, 0.1);
  --line-strong: rgba(255, 255, 255, 0.18);
  --text: #edf1f7;
  --text-dim: #b8c1d1;
  --text-soft: #8f98aa;
  --gold: #f3b55f;
  --gold-2: #ffcf82;
  --cyan: #71d7ff;
  --pink: #f58eff;
  --success: #9ef0c7;
  --shadow: 0 24px 80px rgba(0, 0, 0, 0.45);
  --radius: 24px;
  --radius-sm: 18px;
  --max: 1220px;
  --space: clamp(1rem, 2vw, 1.5rem);
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background:
    radial-gradient(circle at 10% 10%, rgba(113, 215, 255, 0.12), transparent 28%),
    radial-gradient(circle at 90% 18%, rgba(245, 142, 255, 0.08), transparent 24%),
    radial-gradient(circle at 50% 80%, rgba(243, 181, 95, 0.08), transparent 30%),
    linear-gradient(180deg, #07090d 0%, #050608 100%);
  color: var(--text);
  min-height: 100vh;
  line-height: 1.5;
}

body::before {
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  background-image:
    linear-gradient(rgba(255,255,255,0.014) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.014) 1px, transparent 1px);
  background-size: 22px 22px;
  opacity: 0.25;
  mask-image: radial-gradient(circle at center, rgba(0,0,0,0.9), transparent 85%);
}

a { color: inherit; text-decoration: none; }
img { max-width: 100%; display: block; }
button, input, select, textarea { font: inherit; }

.container {
  width: min(calc(100% - 1.5rem), var(--max));
  margin-inline: auto;
}

.skip-link {
  position: absolute;
  left: -999px;
  top: 0;
}
.skip-link:focus {
  left: 1rem;
  top: 1rem;
  z-index: 1000;
  background: var(--gold);
  color: #111;
  padding: 0.75rem 1rem;
  border-radius: 999px;
}

.site-header {
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(18px);
  background: rgba(6, 8, 12, 0.72);
  border-bottom: 1px solid rgba(255,255,255,0.06);
}

.nav-shell {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.9rem 0;
  gap: 1rem;
}

.brand {
  display: inline-flex;
  align-items: center;
  gap: 0.8rem;
  font-weight: 800;
  letter-spacing: 0.08em;
}
.brand-mark {
  width: 1rem;
  height: 1rem;
  border-radius: 3px;
  background: linear-gradient(135deg, var(--gold), var(--cyan));
  box-shadow: 0 0 16px rgba(243, 181, 95, 0.48);
  transform: rotate(45deg);
}
.brand-word { font-size: 0.98rem; }

.nav-toggle {
  width: 3rem;
  height: 3rem;
  border-radius: 999px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 4px;
  color: var(--text);
}
.nav-toggle span {
  display: block;
  width: 1.1rem;
  height: 2px;
  border-radius: 99px;
  background: currentColor;
}

.nav-links {
  position: absolute;
  right: 0.75rem;
  top: calc(100% + 0.5rem);
  width: min(92vw, 24rem);
  display: none;
  flex-direction: column;
  padding: 0.9rem;
  gap: 0.6rem;
  border-radius: 20px;
  background: rgba(10, 14, 22, 0.95);
  border: 1px solid rgba(255,255,255,0.08);
  box-shadow: var(--shadow);
}
.nav-links.is-open { display: flex; }
.nav-links a {
  padding: 0.8rem 0.9rem;
  border-radius: 14px;
  color: var(--text-dim);
}
.nav-links a:hover, .nav-links a:focus-visible {
  background: rgba(255,255,255,0.05);
  color: var(--text);
}
.nav-cta {
  background: linear-gradient(135deg, rgba(243,181,95,0.17), rgba(113,215,255,0.16));
  color: var(--text) !important;
  border: 1px solid rgba(243,181,95,0.22);
}

main { overflow: clip; }
section { padding: clamp(3.8rem, 7vw, 7rem) 0; }
.section-tighter { padding-top: 2.5rem; }

.eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  font-size: 0.8rem;
  text-transform: uppercase;
  letter-spacing: 0.14em;
  color: var(--gold-2);
  padding: 0.55rem 0.85rem;
  border-radius: 999px;
  background: rgba(243,181,95,0.08);
  border: 1px solid rgba(243,181,95,0.12);
}
.eyebrow::before {
  content: "";
  width: 0.45rem;
  height: 0.45rem;
  border-radius: 999px;
  background: var(--gold);
  box-shadow: 0 0 12px rgba(243,181,95,0.56);
}

h1, h2, h3, h4 {
  margin: 0;
  line-height: 1.05;
  letter-spacing: -0.04em;
}

h1 {
  font-size: clamp(2.9rem, 8vw, 6rem);
  max-width: 13ch;
}

h2 {
  font-size: clamp(2rem, 5vw, 4rem);
  max-width: 16ch;
}

h3 {
  font-size: clamp(1.25rem, 3vw, 1.7rem);
}

.lead, .body-lg {
  font-size: clamp(1.08rem, 2vw, 1.28rem);
  color: var(--text-dim);
  max-width: 60ch;
}

.body-md {
  color: var(--text-dim);
  max-width: 62ch;
}

.hero {
  position: relative;
  padding-top: clamp(4rem, 9vw, 8rem);
}
.hero-grid {
  display: grid;
  gap: 1.6rem;
}
.hero-copy {
  display: grid;
  gap: 1.2rem;
}
.gradient-title {
  background: linear-gradient(135deg, #ffffff 5%, #e6c18f 38%, #9ce2ff 78%, #f1b0ff 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}
.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.85rem;
}

.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.55rem;
  min-height: 3.3rem;
  padding: 0.9rem 1.25rem;
  border-radius: 999px;
  border: 1px solid transparent;
  font-weight: 700;
  letter-spacing: -0.02em;
  transition: transform 0.18s ease, border-color 0.18s ease, background 0.18s ease;
}
.btn:hover, .btn:focus-visible { transform: translateY(-1px); }
.btn-primary {
  color: #121212;
  background: linear-gradient(135deg, var(--gold) 0%, var(--gold-2) 40%, var(--cyan) 100%);
  box-shadow: 0 18px 48px rgba(100, 188, 218, 0.18);
}
.btn-secondary {
  color: var(--text);
  background: rgba(255,255,255,0.04);
  border-color: rgba(255,255,255,0.1);
}
.btn-quiet {
  color: var(--gold-2);
  background: rgba(243,181,95,0.06);
  border-color: rgba(243,181,95,0.12);
}

.hero-proof {
  display: grid;
  gap: 0.8rem;
  margin-top: 0.4rem;
}
.hero-proof p { margin: 0; color: var(--text-soft); }
.proof-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
}
.proof-chip {
  padding: 0.65rem 0.85rem;
  border-radius: 999px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  color: var(--text-dim);
  font-size: 0.92rem;
}

.hero-visual {
  position: relative;
}
.image-card {
  border-radius: calc(var(--radius) + 6px);
  overflow: hidden;
  border: 1px solid var(--line);
  background: rgba(255,255,255,0.03);
  box-shadow: var(--shadow);
}
.image-card img {
  width: 100%;
  aspect-ratio: 4 / 5;
  object-fit: cover;
}
.image-caption {
  padding: 1rem 1.1rem;
  color: var(--text-soft);
  font-size: 0.96rem;
  background: rgba(0,0,0,0.24);
}
.floating-stat {
  position: absolute;
  bottom: 1rem;
  left: 1rem;
  right: 1rem;
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.7rem;
}
.stat-card {
  padding: 1rem;
  border-radius: 18px;
  background: rgba(6,10,16,0.78);
  border: 1px solid rgba(255,255,255,0.08);
  backdrop-filter: blur(14px);
}
.stat-card strong {
  display: block;
  font-size: 1.45rem;
  margin-bottom: 0.25rem;
}
.stat-card span { color: var(--text-soft); font-size: 0.92rem; }

.panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: clamp(1.2rem, 2.5vw, 1.7rem);
  box-shadow: var(--shadow);
}
.panel-strong {
  background: var(--panel-strong);
}

.grid-2, .grid-3, .grid-4 {
  display: grid;
  gap: 1rem;
}

.value-grid .panel,
.card-stack .panel,
.flow-grid .panel,
.metric-grid .panel,
.lane-grid .panel,
.faq-grid .panel,
.comparison-grid .panel {
  height: 100%;
}

.kicker {
  color: var(--text-soft);
  text-transform: uppercase;
  letter-spacing: 0.13em;
  font-size: 0.78rem;
}

.big-quote {
  font-size: clamp(1.3rem, 2vw, 1.7rem);
  color: var(--text);
  max-width: 30ch;
}

.metric-grid strong {
  display: block;
  font-size: clamp(2.2rem, 4vw, 3rem);
  margin-bottom: 0.2rem;
}
.metric-grid p, .panel p:last-child { margin-bottom: 0; }

.split-band {
  display: grid;
  gap: 1rem;
  align-items: center;
}

.band-visual {
  border-radius: var(--radius);
  overflow: hidden;
  border: 1px solid var(--line);
  box-shadow: var(--shadow);
}
.band-visual img {
  width: 100%;
  aspect-ratio: 16 / 10;
  object-fit: cover;
}

.checklist, .bullet-list, .numbered-list, .page-links, .mini-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: grid;
  gap: 0.8rem;
}
.checklist li,
.bullet-list li,
.numbered-list li,
.mini-list li {
  position: relative;
  padding-left: 1.35rem;
  color: var(--text-dim);
}
.checklist li::before,
.bullet-list li::before,
.mini-list li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0.62rem;
  width: 0.48rem;
  height: 0.48rem;
  border-radius: 999px;
  background: linear-gradient(135deg, var(--gold), var(--cyan));
}
.numbered-list li {
  padding-left: 2rem;
}
.numbered-list li::before {
  content: counter(step);
  counter-increment: step;
  position: absolute;
  left: 0;
  top: -0.1rem;
  width: 1.35rem;
  height: 1.35rem;
  border-radius: 999px;
  display: grid;
  place-items: center;
  background: rgba(243,181,95,0.14);
  color: var(--gold-2);
  font-size: 0.8rem;
  font-weight: 800;
}
.numbered-list { counter-reset: step; }

.tag-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
}
.tag {
  padding: 0.55rem 0.8rem;
  border-radius: 999px;
  font-size: 0.88rem;
  color: var(--text-dim);
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
}

.ribbon {
  position: relative;
  padding: 1rem 1.2rem;
  border-radius: 18px;
  background: linear-gradient(135deg, rgba(113,215,255,0.12), rgba(243,181,95,0.12));
  border: 1px solid rgba(255,255,255,0.08);
  color: var(--text-dim);
}

.flow {
  display: grid;
  gap: 0.8rem;
}
.flow-step {
  display: flex;
  gap: 0.9rem;
  align-items: flex-start;
}
.flow-step strong {
  width: 2rem;
  height: 2rem;
  border-radius: 999px;
  display: grid;
  place-items: center;
  flex: 0 0 auto;
  background: rgba(243,181,95,0.14);
  border: 1px solid rgba(243,181,95,0.22);
  color: var(--gold-2);
}
.flow-step div p { margin: 0.25rem 0 0; color: var(--text-soft); }

.table-wrap {
  overflow-x: auto;
  border-radius: var(--radius);
  border: 1px solid var(--line);
  background: rgba(255,255,255,0.03);
}
.table {
  width: 100%;
  border-collapse: collapse;
  min-width: 42rem;
}
.table th, .table td {
  text-align: left;
  padding: 1rem;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  vertical-align: top;
}
.table th {
  font-size: 0.84rem;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--text-soft);
  background: rgba(255,255,255,0.02);
}
.table td { color: var(--text-dim); }

.section-head {
  display: grid;
  gap: 1rem;
  margin-bottom: 1.6rem;
}
.section-head-row {
  display: grid;
  gap: 1rem;
  margin-bottom: 1.8rem;
}

.highlight-box {
  padding: 1.25rem;
  border-radius: 20px;
  border: 1px solid rgba(255,255,255,0.08);
  background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
}

.form-shell {
  display: grid;
  gap: 1rem;
  border-radius: var(--radius);
  padding: clamp(1.25rem, 3vw, 1.75rem);
  background: linear-gradient(180deg, rgba(11,16,24,0.92), rgba(8,11,17,0.96));
  border: 1px solid rgba(255,255,255,0.08);
  box-shadow: var(--shadow);
}
.form-grid {
  display: grid;
  gap: 0.85rem;
}
.form-grid input,
.form-grid select,
.form-grid textarea {
  width: 100%;
  border: 1px solid rgba(255,255,255,0.08);
  background: rgba(255,255,255,0.04);
  color: var(--text);
  border-radius: 16px;
  padding: 0.95rem 1rem;
}
.form-grid textarea {
  min-height: 8rem;
  resize: vertical;
}
.form-note {
  color: var(--text-soft);
  font-size: 0.92rem;
}

.cta-band {
  background: linear-gradient(145deg, rgba(243,181,95,0.1), rgba(113,215,255,0.08) 46%, rgba(245,142,255,0.08));
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: calc(var(--radius) + 8px);
  padding: clamp(1.3rem, 4vw, 2rem);
  box-shadow: var(--shadow);
}

.faq-grid details {
  border-radius: 18px;
  border: 1px solid rgba(255,255,255,0.08);
  background: rgba(255,255,255,0.03);
  padding: 1rem 1.1rem;
}
.faq-grid summary {
  cursor: pointer;
  font-weight: 700;
  list-style: none;
}
.faq-grid summary::-webkit-details-marker { display: none; }
.faq-grid details p { color: var(--text-dim); margin-bottom: 0; margin-top: 0.8rem; }

.pillar-grid .panel,
.value-grid .panel,
.metric-grid .panel,
.comparison-grid .panel,
.lane-grid .panel,
.page-links .panel,
.page-card {
  position: relative;
  overflow: hidden;
}
.pillar-grid .panel::after,
.value-grid .panel::after,
.comparison-grid .panel::after,
.page-card::after {
  content: "";
  position: absolute;
  inset: auto -2rem -2rem auto;
  width: 8rem;
  height: 8rem;
  background: radial-gradient(circle, rgba(113,215,255,0.16), transparent 68%);
  pointer-events: none;
}

.page-hero {
  padding-top: clamp(4rem, 8vw, 7rem);
}
.page-hero-grid {
  display: grid;
  gap: 1.2rem;
}

.page-links {
  display: grid;
  gap: 1rem;
}
.page-card {
  display: grid;
  gap: 0.8rem;
  padding: 1.2rem;
  border-radius: var(--radius);
  border: 1px solid rgba(255,255,255,0.08);
  background: rgba(255,255,255,0.03);
}

.site-footer {
  padding: 3rem 0 2rem;
  border-top: 1px solid rgba(255,255,255,0.08);
  background: rgba(6, 8, 11, 0.86);
}
.footer-grid {
  display: grid;
  gap: 1.5rem;
}
.site-footer h3 {
  font-size: 1rem;
  margin-bottom: 0.7rem;
}
.site-footer ul {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0.6rem;
  color: var(--text-dim);
}
.footer-copy, .footer-bottom {
  color: var(--text-soft);
}
.footer-bottom {
  display: grid;
  gap: 0.2rem;
  padding-top: 1.5rem;
  margin-top: 1.5rem;
  border-top: 1px solid rgba(255,255,255,0.06);
}

.notice {
  color: var(--gold-2);
  font-weight: 600;
}

.compare-strip {
  display: grid;
  gap: 1rem;
}
.compare-card {
  padding: 1rem;
  border-radius: 18px;
  border: 1px solid rgba(255,255,255,0.08);
  background: rgba(255,255,255,0.03);
}
.compare-card h3 { margin-bottom: 0.55rem; }
.compare-card p { margin: 0; color: var(--text-dim); }

.aside-quote {
  padding: 1rem;
  border-left: 3px solid rgba(243,181,95,0.55);
  color: var(--text-dim);
  background: rgba(243,181,95,0.05);
  border-radius: 0 16px 16px 0;
}

@media (min-width: 760px) {
  .grid-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .grid-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .grid-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .hero-grid,
  .split-band,
  .section-head-row,
  .page-hero-grid,
  .footer-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
  .hero-grid { align-items: center; gap: 2rem; }
  .footer-grid { grid-template-columns: 1.35fr 1fr 1fr 1fr; }
  .section-head-row > :first-child,
  .page-hero-grid > :first-child { padding-right: 1rem; }
}

@media (min-width: 980px) {
  .nav-toggle { display: none; }
  .nav-links {
    position: static;
    width: auto;
    display: inline-flex;
    flex-direction: row;
    align-items: center;
    padding: 0;
    box-shadow: none;
    border: 0;
    background: transparent;
    gap: 0.35rem;
  }
  .nav-links a { padding-inline: 0.95rem; }
  .hero-grid { grid-template-columns: 1.18fr 0.82fr; }
  .split-band { grid-template-columns: 1fr 1fr; }
  .compare-strip { grid-template-columns: repeat(4, minmax(0, 1fr)); }
}

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after { animation: none !important; transition: none !important; }
}
'''

script = r'''
const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.nav-links');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(isOpen));
  });
  nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
    nav.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
  }));
}
'''


def shell(title, description, path, content, schema_extra=""):
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#06070a">
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  <link rel="canonical" href="{base_url}/{path}">
  <link rel="icon" href="assets/icons/favicon.svg" type="image/svg+xml">
  <link rel="manifest" href="site.webmanifest">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{base_url}/{path}">
  <meta property="og:image" content="{base_url}/assets/placeholders/og-cover.svg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{base_url}/assets/placeholders/og-cover.svg">
  <link rel="stylesheet" href="styles.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "UNBURIED",
    "url": "{base_url}",
    "logo": "{base_url}/assets/icons/favicon.svg",
    "description": "Curated sovereign distribution for important independent films.",
    "sameAs": []
  }}
  </script>
  {schema_extra}
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  {nav}
  <main id="main">{content}</main>
  {footer}
  {scripts}
</body>
</html>'''

index_schema = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "UNBURIED",
  "url": "''' + base_url + '''",
  "description": "Sovereign distribution for important films.",
  "potentialAction": {
    "@type": "SubscribeAction",
    "target": "''' + base_url + '''/#waitlist",
    "name": "Join the waitlist"
  }
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is UNBURIED?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "UNBURIED is a filmmaker-first distribution operating system for important independent films facing structural distribution friction."
      }
    },
    {
      "@type": "Question",
      "name": "Who is it for?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Independent filmmakers, small rights-holding teams, aligned hosts, educators, and investors who care about narrative sovereignty and direct creator revenue."
      }
    },
    {
      "@type": "Question",
      "name": "What is the main call to action?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Join the waitlist to get the Narrative Friction Index and early access to filmmaker and partner updates."
      }
    }
  ]
}
</script>'''

index_content = f'''
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-copy">
      <span class="eyebrow">Narrative sovereignty for cinema that matters</span>
      <h1 class="gradient-title">Important films should not need permission to reach the people who need them.</h1>
      <p class="lead">UNBURIED is a filmmaker-first distribution network built for high-friction independent films that get buried by gatekeepers, softened by brand-safe systems, or stranded in fragmented release chaos.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#waitlist">Join the Waitlist</a>
        <a class="btn btn-secondary" href="filmmakers.html">See the Filmmaker Model</a>
      </div>
      <div class="hero-proof">
        <p>Built for directors, producers, rights holders, community hosts, educators, curators, aligned capital, and backers who are done watching vital stories disappear.</p>
        <div class="proof-row">
          <span class="proof-chip">Curated catalog, not an upload dump</span>
          <span class="proof-chip">Direct rentals, purchases, and rights sales</span>
          <span class="proof-chip">Local screening engine</span>
          <span class="proof-chip">Resilient payments and audience ownership</span>
        </div>
      </div>
    </div>
    <div class="hero-visual">
      <figure class="image-card">
        <img src="assets/placeholders/home-hero.svg" alt="Atmospheric placeholder for the UNBURIED homepage hero image">
        <figcaption class="image-caption">A premium cinematic future for truth-bearing films: direct revenue, local circulation, and no forced surrender of rights.</figcaption>
      </figure>
      <div class="floating-stat">
        <div class="stat-card"><strong>1 platform</strong><span>to fund, launch, license, and grow a film</span></div>
        <div class="stat-card"><strong>0 fluff</strong><span>just the clearest path from buried to circulating</span></div>
      </div>
    </div>
  </div>
</section>

<section class="section-tighter">
  <div class="container compare-strip">
    <div class="compare-card"><h3>The vacation</h3><p>A world where truth-bearing films can circulate through living communities, not die in gatekept bottlenecks.</p></div>
    <div class="compare-card"><h3>The hard result</h3><p>Direct purchases, local rights sales, screening revenue, support campaigns, audience ownership, and resilient rails.</p></div>
    <div class="compare-card"><h3>The wedge</h3><p>Start where the pain is hottest: films facing structural distribution friction. Expand under a premium umbrella brand.</p></div>
    <div class="compare-card"><h3>The invite</h3><p>Join early. Help shape the network. Back the first wave of films that should never have been buried in the first place.</p></div>
  </div>
</section>

<section>
  <div class="container section-head-row">
    <div>
      <span class="eyebrow">The 2 a.m. problem we solve</span>
      <h2>“I made something brave and important, and now I have no trustworthy path to get it seen, sold, protected, and paid for.”</h2>
    </div>
    <div class="panel panel-strong">
      <p class="big-quote">The real pain is not only censorship. It is suppression plus fragmentation plus financial fragility plus operational overload.</p>
      <ul class="checklist">
        <li>Mainstream distributors pass, stall, or demand softening.</li>
        <li>Generic video hosts do not solve discovery, licensing, or payment fragility.</li>
        <li>Self-release turns filmmakers into accidental distribution companies.</li>
        <li>Important films get attention for a week, then vanish into noise.</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Who this is for</span>
      <h2>Dream targets who instantly know this is about them</h2>
      <p class="body-lg">The core buyer is not “everyone who likes indie film.” It is the filmmaker or rights-holding team carrying a culturally important film that the normal system is structurally bad at handling.</p>
    </div>
    <div class="grid-3 value-grid">
      <article class="panel page-card">
        <span class="kicker">Primary dream client</span>
        <h3>High-friction independent filmmakers</h3>
        <p>Directors, producers, and small rights-holding teams with politically sensitive, taboo, inconvenient, or nuance-heavy films that struggle to find fair distribution.</p>
      </article>
      <article class="panel page-card">
        <span class="kicker">Secondary dream client</span>
        <h3>Aligned hosts and community distributors</h3>
        <p>Educators, cultural venues, organizers, podcasters, activist networks, nonprofits, and local nodes who want to bring meaningful films to their people without legal confusion.</p>
      </article>
      <article class="panel page-card">
        <span class="kicker">Strategic stakeholder</span>
        <h3>Investors who believe in creator sovereignty</h3>
        <p>Builders and capital partners who care about open money, artist entrepreneurship, resilient rails, and direct relationships between creators and communities.</p>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="container split-band">
    <div>
      <span class="eyebrow">Why now</span>
      <h2>The next winner will not look like a new YouTube.</h2>
      <p class="body-lg">It will look like a premium rights network that combines direct commerce, community screenings, clean catalog curation, and resilient payment options in one operating system.</p>
      <ul class="bullet-list">
        <li>Creators need audience ownership, not another opaque feed.</li>
        <li>Hosts need screening rights they can understand in minutes, not weeks.</li>
        <li>Investors need recurring transaction logic, not ad-supported hope.</li>
        <li>Viewers want a high-trust place to discover what matters before the story gets flattened.</li>
      </ul>
    </div>
    <div class="band-visual">
      <img src="assets/placeholders/home-network.svg" alt="Placeholder visual showing community screening nodes connected across cities">
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">What UNBURIED actually is</span>
      <h2>Not a generic streaming site. A sovereign distribution operating system.</h2>
      <p class="body-lg">We unify the parts filmmakers currently have to stitch together alone: funding, release, direct sales, local screenings, educational rights, audience ownership, and resilient settlement rails.</p>
    </div>
    <div class="grid-4 pillar-grid">
      <article class="panel">
        <span class="kicker">Curated trust</span>
        <h3>Premium catalog</h3>
        <p>No open sludge. No low-signal flood. A selective home for films facing structural distribution friction.</p>
      </article>
      <article class="panel">
        <span class="kicker">Rights-aware monetization</span>
        <h3>Direct revenue</h3>
        <p>Rent, buy, gift, host, license, support, and later fund. Keep rights by default.</p>
      </article>
      <article class="panel">
        <span class="kicker">Community circulation</span>
        <h3>Screenings that travel</h3>
        <p>Local hosts, educators, venues, and partner communities become the film’s living distribution engine.</p>
      </article>
      <article class="panel">
        <span class="kicker">Resilience</span>
        <h3>Modular rails</h3>
        <p>Mainstream rails for ease. Resilient rails for continuity. Portable audiences so no single vendor owns the whole organism.</p>
      </article>
    </div>
  </div>
</section>

<section class="panel-strong">
  <div class="container section-head">
    <span class="eyebrow">How the ecosystem works</span>
    <h2>One coherent lifecycle from buried to circulating</h2>
    <p class="body-lg">This product is built around the flow real filmmakers need, not the categories a traditional distributor prefers.</p>
  </div>
  <div class="container grid-2 flow-grid">
    <div class="panel panel-strong">
      <h3>For filmmakers</h3>
      <div class="flow">
        <div class="flow-step"><strong>1</strong><div><h4>Fund</h4><p>Run support campaigns, completion pushes, and pre-sale offers before release.</p></div></div>
        <div class="flow-step"><strong>2</strong><div><h4>Launch</h4><p>Open rentals, purchases, gifts, and rights-aware viewing windows.</p></div></div>
        <div class="flow-step"><strong>3</strong><div><h4>License</h4><p>Approve local screenings, educational access, and community distribution rights.</p></div></div>
        <div class="flow-step"><strong>4</strong><div><h4>Grow</h4><p>Own the audience relationship and keep the film alive beyond one burst of attention.</p></div></div>
      </div>
    </div>
    <div class="panel panel-strong">
      <h3>For the ecosystem</h3>
      <div class="flow">
        <div class="flow-step"><strong>1</strong><div><h4>Discover</h4><p>Viewers find films through trusted curation, issue hubs, and host networks.</p></div></div>
        <div class="flow-step"><strong>2</strong><div><h4>Gather</h4><p>Hosts bring films to towns, schools, venues, and communities.</p></div></div>
        <div class="flow-step"><strong>3</strong><div><h4>Support</h4><p>Backers help upcoming titles finish and launch with more leverage.</p></div></div>
        <div class="flow-step"><strong>4</strong><div><h4>Circulate</h4><p>Stories move through people, not just feeds, and revenue reaches creators directly.</p></div></div>
      </div>
    </div>
  </div>
</section>

<section id="lead-magnet">
  <div class="container split-band">
    <div class="panel form-shell">
      <span class="eyebrow">Lead magnet that feels like diagnosis, not bait</span>
      <h2>The Narrative Friction Index</h2>
      <p class="body-md">A sharp, shareable report that names the seven chokepoints most likely to bury an important film. Built to trigger the kind of “this is exactly us” recognition that makes founders and rights-holders forward it to their teams.</p>
      <ul class="checklist">
        <li>The 7 distribution friction patterns that silently kill release momentum</li>
        <li>The 3 revenue lanes most teams overlook until it is too late</li>
        <li>A simple scorecard to assess whether your film is buried, fragile, or ready to travel</li>
        <li>A next-step map for VOD, screenings, educational rights, and audience ownership</li>
      </ul>
      <p class="notice">Yes. A lead magnet makes sense here because dream targets do not want generic newsletters. They want clarity that names what is wrong and what to do next.</p>
    </div>
    <div class="form-shell" id="waitlist">
      <h3>Join the waitlist and get the report first</h3>
      <p class="form-note">Use one or many Formspree endpoints. This page is wired so you can swap them in within minutes.</p>
      <form action="{waitlist_action}" method="POST" class="form-grid">
        <input type="hidden" name="form_name" value="Main Waitlist">
        <label>
          <span class="kicker">Name</span>
          <input type="text" name="name" placeholder="Your name" required>
        </label>
        <label>
          <span class="kicker">Email</span>
          <input type="email" name="email" placeholder="you@example.com" required>
        </label>
        <label>
          <span class="kicker">I am joining as</span>
          <select name="role" required>
            <option value="">Choose one</option>
            <option>Filmmaker / rights holder</option>
            <option>Host / educator / venue</option>
            <option>Investor / partner</option>
            <option>Curator / press / media</option>
            <option>Viewer / supporter</option>
          </select>
        </label>
        <label>
          <span class="kicker">What are you carrying right now?</span>
          <textarea name="context" placeholder="Film in post. Rights but no runway. Host network but no platform. Capital looking for a category. Tell us what's alive."></textarea>
        </label>
        <button class="btn btn-primary" type="submit">Get the report and join the list</button>
      </form>
    </div>
  </div>
</section>

<section>
  <div class="container section-head">
    <span class="eyebrow">The business model in plain English</span>
    <h2>Direct commerce first. Screening rights second. Membership later. Ad dependence never central.</h2>
  </div>
  <div class="table-wrap">
    <table class="table">
      <thead>
        <tr>
          <th>Revenue lane</th>
          <th>What the buyer does</th>
          <th>Why it matters</th>
          <th>Starting split logic</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>VOD rentals and purchases</td>
          <td>Rent, buy, gift, pre-order</td>
          <td>Fastest path to direct creator revenue</td>
          <td>85% rights holder / 10% platform / 5% affiliate</td>
        </tr>
        <tr>
          <td>Community screenings</td>
          <td>Host a local event with rights cleared in-platform</td>
          <td>Turns passive viewership into movement-level circulation</td>
          <td>60% rights holder / 25% host / 15% platform</td>
        </tr>
        <tr>
          <td>Educational licensing</td>
          <td>License for campus, classroom, library, or institution</td>
          <td>Long-tail revenue and durable legitimacy</td>
          <td>70% rights holder / 20% platform / 10% referrer</td>
        </tr>
        <tr>
          <td>Funding campaigns</td>
          <td>Support, pre-buy, fund completion, reserve screenings</td>
          <td>Supports up-and-coming films before release</td>
          <td>95% project / 5% platform plus fees</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section>
  <div class="container grid-2">
    <div class="panel panel-strong">
      <span class="eyebrow">Why this is psychologically sticky</span>
      <h3>The offer speaks to relief, exposure, hope, and momentum.</h3>
      <p class="body-md">Dream targets do not buy “another platform.” They move when the message tells the truth about what they are carrying, names the hidden pattern, and gives them a believable path out.</p>
      <div class="aside-quote">This site is intentionally built to sell the changed reality first, then the mechanism, then the detailed architecture, then the invitation to join before the category hardens around someone else.</div>
    </div>
    <div class="panel panel-strong">
      <span class="eyebrow">Why this is shareable</span>
      <h3>The waitlist doubles as a diagnostic share loop.</h3>
      <p class="body-md">The lead magnet is designed to be forwarded with language like “This is the thing I have been trying to explain,” which pulls co-founders, producers, operators, and partner communities into one shared lens instead of one lonely opt-in.</p>
      <ul class="mini-list">
        <li>Sharable result framing</li>
        <li>Team comparison prompts</li>
        <li>High-recognition language</li>
        <li>Clear next-step ladder after opt-in</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="container cta-band">
    <div class="section-head">
      <span class="eyebrow">Why this can win</span>
      <h2>It gives creators what the old system withholds: leverage.</h2>
      <p class="body-lg">Not just hosting. Not just fundraising. Not just screenings. Not just crypto theater. A coherent path from film to revenue to audience to long-tail circulation.</p>
    </div>
    <div class="hero-actions">
      <a class="btn btn-primary" href="#waitlist">Join the Waitlist</a>
      <a class="btn btn-secondary" href="investors.html">See the investor thesis</a>
      <a class="btn btn-secondary" href="hosts.html">See the host model</a>
    </div>
  </div>
</section>

<section id="faq">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">FAQ</span>
      <h2>Sharp answers for serious people</h2>
    </div>
    <div class="grid-2 faq-grid">
      <details open>
        <summary>Is this a broad indie film platform or only for politically difficult films?</summary>
        <p>Broad umbrella brand. Explicit high-friction flagship lane. That keeps the mission sharp without reducing the whole company to a single oppositional identity.</p>
      </details>
      <details>
        <summary>Does funding live inside the platform?</summary>
        <p>Yes, in layers: support campaigns and pre-sales first, ecosystem completion funds second, regulated investment handoff later if true profit participation is involved.</p>
      </details>
      <details>
        <summary>Why not launch as a full crypto-native platform from day one?</summary>
        <p>Because normal humans still need dead-simple checkout. The resilient move is mainstream rails for ease and decentralized rails where they add continuity and self-custody benefits.</p>
      </details>
      <details>
        <summary>Why does the site push a lead magnet instead of just a newsletter signup?</summary>
        <p>Because dream targets share diagnosis, not generic updates. A sharp report creates recognition, cluster formation, and better-quality waitlist growth.</p>
      </details>
    </div>
  </div>
</section>
'''

filmmakers_schema = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "''' + base_url + '''/index.html"},
    {"@type": "ListItem", "position": 2, "name": "Filmmakers", "item": "''' + base_url + '''/filmmakers.html"}
  ]
}
</script>'''

filmmakers_content = f'''
<section class="page-hero">
  <div class="container page-hero-grid">
    <div>
      <span class="eyebrow">For filmmakers and rights holders</span>
      <h1 class="gradient-title">Keep your rights. Own your audience. Stop getting forced into a distribution job you never wanted.</h1>
      <p class="lead">UNBURIED is built for teams who know their film matters and are done waiting for the existing system to behave like it does.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#filmmaker-form">Get on the filmmaker waitlist</a>
        <a class="btn btn-secondary" href="#nitty-gritty">See the model</a>
      </div>
    </div>
    <div class="image-card">
      <img src="assets/placeholders/filmmakers-hero.svg" alt="Placeholder visual for filmmakers page hero">
      <div class="image-caption">From isolated release chaos to a sovereign, rights-aware distribution operating system.</div>
    </div>
  </div>
</section>

<section>
  <div class="container section-head-row">
    <div>
      <span class="eyebrow">The before and after</span>
      <h2>Your film should not have to survive on hope, hustle, and a pile of disconnected tools.</h2>
    </div>
    <div class="panel panel-strong">
      <ul class="checklist">
        <li>Before: You have a finished or nearly finished film, but no integrated path to sell, screen, license, and grow it.</li>
        <li>After: You have a single system to activate direct viewing, local screenings, educational licensing, funding, and audience retention.</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="container grid-3 value-grid">
    <article class="panel">
      <span class="kicker">Pain relief</span>
      <h3>Less fragmentation</h3>
      <p>No more cobbling together a payment tool, a host spreadsheet, a ticketing app, a video host, and a half-broken audience list.</p>
    </article>
    <article class="panel">
      <span class="kicker">Credible upside</span>
      <h3>More revenue lanes</h3>
      <p>Monetize through VOD, purchases, gifts, educational licenses, local screenings, and later support campaigns or completion pushes.</p>
    </article>
    <article class="panel">
      <span class="kicker">Real leverage</span>
      <h3>Portable audience ownership</h3>
      <p>Buyers, supporters, hosts, educators, and affiliates become an asset you can keep, not a shadow audience trapped inside someone else’s ecosystem.</p>
    </article>
  </div>
</section>

<section id="nitty-gritty">
  <div class="container section-head">
    <span class="eyebrow">The nitty gritty</span>
    <h2>The final version of the filmmaker model</h2>
    <p class="body-lg">This is the detailed promise, the operational logic, and the economic structure serious teams will want to see before they back a new category.</p>
  </div>
  <div class="grid-2">
    <div class="panel panel-strong">
      <h3>What you can do inside the platform</h3>
      <ul class="numbered-list">
        <li>Onboard a title with rights verification, territory rules, windowing, pricing, and host settings.</li>
        <li>Activate direct rentals, purchases, gifts, and pre-orders.</li>
        <li>Approve local screening requests or set auto-approval rules for trusted hosts.</li>
        <li>Publish educational licensing tiers and institution-ready access.</li>
        <li>Run support or completion campaigns before release and momentum campaigns after release.</li>
        <li>Track audience growth, revenue by lane, reserve holds, payouts, and affiliate performance.</li>
      </ul>
    </div>
    <div class="panel panel-strong">
      <h3>What you do not have to do anymore</h3>
      <ul class="bullet-list">
        <li>Play technical support for a broken release stack.</li>
        <li>Manually negotiate every small screening from scratch.</li>
        <li>Guess whether to prioritize VOD, screenings, educational, or support asks in the dark.</li>
        <li>Surrender your whole asset just to get a film online.</li>
      </ul>
      <div class="ribbon">This page is intentionally heavy on specifics because dream filmmakers do not trust vague promises anymore.</div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">Economic logic</span>
      <h2>Simple enough to understand. Sophisticated enough to hold up under pressure.</h2>
    </div>
    <div class="table-wrap">
      <table class="table">
        <thead>
          <tr>
            <th>Lane</th>
            <th>Buyer journey</th>
            <th>Suggested split</th>
            <th>Operational note</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Rental / purchase</td>
            <td>Film page → checkout → secure playback</td>
            <td>85 / 10 / 5</td>
            <td>Rolling reserve held back for disputes and refunds</td>
          </tr>
          <tr>
            <td>Community screening</td>
            <td>Host request → approval → ticketing → event settlement</td>
            <td>60 / 25 / 15</td>
            <td>Event holdback released after a short post-event buffer</td>
          </tr>
          <tr>
            <td>Educational license</td>
            <td>Institution inquiry → instant tier or manual quote</td>
            <td>70 / 20 / 10</td>
            <td>Long-tail revenue lane with higher service complexity</td>
          </tr>
          <tr>
            <td>Support campaign</td>
            <td>Story page → pledge or pre-buy → updates</td>
            <td>95 / 5</td>
            <td>Best for upcoming films and campaign-driven releases</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section>
  <div class="container split-band">
    <div>
      <span class="eyebrow">Money and rights</span>
      <h2>How funds move without turning the platform into a chaos machine</h2>
      <p class="body-lg">Mainstream rails should make checkout effortless. Resilient rails should make the system harder to choke. The viewer never needs to feel the complexity unless they choose it.</p>
      <ul class="checklist">
        <li>Fiat checkout first for normal humans.</li>
        <li>Reserves and payout timing built around dispute reality, not wishful thinking.</li>
        <li>Stablecoin or self-custody options added where they reduce cross-border friction and takedown risk.</li>
        <li>Rights stay legible in plain legal terms, not buried in crypto theater.</li>
      </ul>
    </div>
    <div class="band-visual">
      <img src="assets/placeholders/payments-rails.svg" alt="Placeholder image for payment and resilience rails">
    </div>
  </div>
</section>

<section id="diagnostic">
  <div class="container grid-2">
    <div class="panel form-shell">
      <span class="eyebrow">Lead magnet for serious teams</span>
      <h2>Release Risk Brief</h2>
      <p class="body-md">A cleaner, more technical companion to the Narrative Friction Index for producers and rights holders who want the deeper architecture view before they join the wave.</p>
      <ul class="checklist">
        <li>Where payments and cross-border payouts usually break</li>
        <li>What merchant-of-record choices change operational risk</li>
        <li>How local screening rights can be productized without creating a support nightmare</li>
        <li>What to centralize, what to modularize, and what not to touch in MVP</li>
      </ul>
    </div>
    <div class="form-shell" id="filmmaker-form">
      <h3>Filmmaker early-access form</h3>
      <form action="{filmmaker_action}" method="POST" class="form-grid">
        <input type="hidden" name="form_name" value="Filmmaker Waitlist">
        <label><span class="kicker">Name</span><input type="text" name="name" required></label>
        <label><span class="kicker">Email</span><input type="email" name="email" required></label>
        <label><span class="kicker">Role</span><input type="text" name="role" placeholder="Director, producer, rights holder, sales agent"></label>
        <label><span class="kicker">Current stage</span>
          <select name="stage">
            <option>Idea / development</option>
            <option>Production</option>
            <option>Post-production</option>
            <option>Finished film</option>
            <option>Existing catalog</option>
          </select>
        </label>
        <label><span class="kicker">What is the biggest bottleneck?</span><textarea name="bottleneck" placeholder="Distribution pass. Audience without infrastructure. Need screening engine. Need resilient payouts. Tell us the truth."></textarea></label>
        <button class="btn btn-primary" type="submit">Join as a filmmaker</button>
      </form>
    </div>
  </div>
</section>

<section>
  <div class="container cta-band">
    <div class="section-head">
      <span class="eyebrow">The real promise</span>
      <h2>Move from isolated creator with a risky film to sovereign rights holder with a release pathway that can actually hold.</h2>
    </div>
    <div class="hero-actions">
      <a class="btn btn-primary" href="#filmmaker-form">Join the filmmaker waitlist</a>
      <a class="btn btn-secondary" href="hosts.html">See how host distribution works</a>
    </div>
  </div>
</section>
'''

hosts_schema = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "''' + base_url + '''/index.html"},
    {"@type": "ListItem", "position": 2, "name": "Hosts", "item": "''' + base_url + '''/hosts.html"}
  ]
}
</script>'''

hosts_content = f'''
<section class="page-hero">
  <div class="container page-hero-grid">
    <div>
      <span class="eyebrow">For hosts, educators, venues, and local distributors</span>
      <h1 class="gradient-title">Bring important films to your city without spending days untangling rights, logistics, and payment confusion.</h1>
      <p class="lead">UNBURIED turns a messy licensing process into a guided flow that lets aligned people gather others around films that matter.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#host-form">Join the host list</a>
        <a class="btn btn-secondary" href="#rights">See how rights work</a>
      </div>
    </div>
    <div class="image-card">
      <img src="assets/placeholders/hosts-hero.svg" alt="Placeholder visual for hosts page hero">
      <div class="image-caption">The host becomes part curator, part convener, part local circulation node, without carrying the whole legal and technical burden alone.</div>
    </div>
  </div>
</section>

<section>
  <div class="container section-head-row">
    <div>
      <span class="eyebrow">Why hosts matter</span>
      <h2>Important films spread through people who care enough to gather others around them.</h2>
    </div>
    <div class="panel panel-strong">
      <p class="big-quote">The screening network is not a side feature. It is the living distribution engine.</p>
      <ul class="bullet-list">
        <li>Neighborhood screenings</li>
        <li>Campus events</li>
        <li>Issue-driven gatherings</li>
        <li>Podcaster and creator screenings</li>
        <li>Cultural venue and micro-cinema nights</li>
      </ul>
    </div>
  </div>
</section>

<section id="rights">
  <div class="container section-head">
    <span class="eyebrow">Rights made simple</span>
    <h2>Four licensing paths. One easy flow.</h2>
  </div>
  <div class="grid-4 lane-grid">
    <article class="panel"><span class="kicker">Home circle</span><h3>Private gatherings</h3><p>Small, trusted groups. No public ticketing. Good for intimate introductions and invite-only salons.</p></article>
    <article class="panel"><span class="kicker">Community</span><h3>Public local screenings</h3><p>For grassroots organizers, nonprofits, and local cultural networks that want to gather a real audience.</p></article>
    <article class="panel"><span class="kicker">Educational</span><h3>Campus and classroom</h3><p>For libraries, student groups, teachers, and institutions that need a clean license and clear usage terms.</p></article>
    <article class="panel"><span class="kicker">Commercial</span><h3>Venue-based rights</h3><p>For theaters, micro-cinemas, coworking venues, and trusted partners selling tickets at scale.</p></article>
  </div>
</section>

<section>
  <div class="container split-band">
    <div>
      <span class="eyebrow">Host flow</span>
      <h2>From interest to event page without the legal headache</h2>
      <div class="flow">
        <div class="flow-step"><strong>1</strong><div><h4>Choose a film</h4><p>Browse only titles available for hosting and see what kind of events they support.</p></div></div>
        <div class="flow-step"><strong>2</strong><div><h4>Submit your event details</h4><p>City, venue, audience size, ticket range, event type, and timing.</p></div></div>
        <div class="flow-step"><strong>3</strong><div><h4>Get approval or automatic clearance</h4><p>Depending on the rights-holder rules and your trust tier.</p></div></div>
        <div class="flow-step"><strong>4</strong><div><h4>Launch the event page</h4><p>Use ready-made promo assets, sell tickets, and get a clear settlement summary after the event.</p></div></div>
      </div>
    </div>
    <div class="band-visual">
      <img src="assets/placeholders/hosts-event.svg" alt="Placeholder image for host event section">
    </div>
  </div>
</section>

<section>
  <div class="container grid-3 value-grid">
    <article class="panel"><span class="kicker">Revenue</span><h3>Earn fairly</h3><p>Hosts are rewarded for doing the work of convening, promoting, and filling the room.</p></article>
    <article class="panel"><span class="kicker">Clarity</span><h3>Know exactly what you are allowed to do</h3><p>No murky permission threads. No uncertainty about ticketing, public promotion, or audience size bands.</p></article>
    <article class="panel"><span class="kicker">Status</span><h3>Grow into a trusted node</h3><p>Over time, the platform can certify reliable hosts, which reduces approval friction and increases access to higher-signal titles.</p></article>
  </div>
</section>

<section>
  <div class="container cta-band">
    <div class="section-head">
      <span class="eyebrow">A better kind of community feature</span>
      <h2>Mission loops instead of cheap gamification</h2>
      <p class="body-lg">Hosts, curators, translators, and ambassadors can be recognized and rewarded for contribution. The point is to strengthen circulation, not turn serious films into a dopamine casino.</p>
    </div>
    <div class="tag-row">
      <span class="tag">Host milestones</span>
      <span class="tag">Impact markers</span>
      <span class="tag">City chapter growth</span>
      <span class="tag">Ambassador rewards</span>
      <span class="tag">Verified curator status</span>
    </div>
  </div>
</section>

<section id="host-form">
  <div class="container grid-2">
    <div class="panel form-shell">
      <span class="eyebrow">Host starter kit</span>
      <h2>The Local Screening Playbook</h2>
      <p class="body-md">A compact download for early host leads: event types, license logic, promotion tips, room setup, and how to turn one screening into a local chapter of trust.</p>
      <ul class="checklist">
        <li>Which event type fits your audience</li>
        <li>How to frame the screening so people show up for meaning, not just novelty</li>
        <li>How to stack ticketing, follow-up, and invitation loops for the next event</li>
      </ul>
    </div>
    <div class="form-shell">
      <h3>Join the host waitlist</h3>
      <form action="{waitlist_action}" method="POST" class="form-grid">
        <input type="hidden" name="form_name" value="Host Waitlist">
        <label><span class="kicker">Name</span><input type="text" name="name" required></label>
        <label><span class="kicker">Email</span><input type="email" name="email" required></label>
        <label><span class="kicker">Organization or venue</span><input type="text" name="organization"></label>
        <label><span class="kicker">I want to host as</span>
          <select name="host_type">
            <option>Community organizer</option>
            <option>Educator / campus lead</option>
            <option>Venue / micro-cinema</option>
            <option>Creator / podcaster</option>
            <option>Nonprofit / movement group</option>
          </select>
        </label>
        <label><span class="kicker">What city or region are you in?</span><input type="text" name="location"></label>
        <button class="btn btn-primary" type="submit">Get the playbook and join</button>
      </form>
    </div>
  </div>
</section>
'''

investors_schema = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "''' + base_url + '''/index.html"},
    {"@type": "ListItem", "position": 2, "name": "Investors", "item": "''' + base_url + '''/investors.html"}
  ]
}
</script>'''

investors_content = f'''
<section class="page-hero">
  <div class="container page-hero-grid">
    <div>
      <span class="eyebrow">For investors, strategic partners, and open-infrastructure builders</span>
      <h1 class="gradient-title">This is not a protest website with video hosting. It is a new rights-and-commerce category.</h1>
      <p class="lead">UNBURIED is designed as a filmmaker-first commerce network that can monetize truth-bearing films through direct sales, local screenings, licensing, and community-supported launches.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="#investor-form">Request the thesis</a>
        <a class="btn btn-secondary" href="#dorsey-fit">See the Dorsey-fit section</a>
      </div>
    </div>
    <div class="image-card">
      <img src="assets/placeholders/investors-hero.svg" alt="Placeholder image for investors page hero">
      <div class="image-caption">A new media layer for important films: category-defining, modular, and built for direct creator economics rather than ad dependency.</div>
    </div>
  </div>
</section>

<section>
  <div class="container section-head-row">
    <div>
      <span class="eyebrow">The thesis</span>
      <h2>High-friction films are not a niche content problem. They are a distribution infrastructure problem.</h2>
    </div>
    <div class="panel panel-strong">
      <ul class="checklist">
        <li>Existing buyers and platforms create structural drop-off for politically difficult and nuance-heavy work.</li>
        <li>Creators with audience demand still lack a safe, integrated route to commerce, licensing, and continuity.</li>
        <li>Direct commerce plus host-led circulation is a better fit than ad-supported algorithmic scale for this category.</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="container grid-3 metric-grid">
    <div class="panel"><strong>4</strong><p>core revenue lanes from the start: VOD, screenings, educational, funding</p></div>
    <div class="panel"><strong>1</strong><p>coherent operating system instead of a fragile stack of disconnected tools</p></div>
    <div class="panel"><strong>0</strong><p>need to make the company live or die by advertiser approval</p></div>
  </div>
</section>

<section>
  <div class="container section-head">
    <span class="eyebrow">Business model</span>
    <h2>Broad umbrella. Explicit high-friction flagship lane. Premium trust posture.</h2>
    <p class="body-lg">The brand stays broad enough to scale. The wedge stays sharp enough to matter. The economics stay grounded in transactions and rights, not just attention.</p>
  </div>
  <div class="grid-2">
    <div class="panel panel-strong">
      <h3>What the platform sells</h3>
      <ul class="bullet-list">
        <li>Direct rentals and purchases</li>
        <li>Community screening rights</li>
        <li>Educational and institutional licenses</li>
        <li>Support and completion campaigns</li>
        <li>Later: membership and strategic partner channels</li>
      </ul>
    </div>
    <div class="panel panel-strong">
      <h3>What the platform does not bet the company on</h3>
      <ul class="bullet-list">
        <li>Ad-supported scale</li>
        <li>Fully open uploads</li>
        <li>Crypto-only UX</li>
        <li>Native mobile checkout dependence in MVP</li>
      </ul>
    </div>
  </div>
</section>

<section id="dorsey-fit">
  <div class="container split-band">
    <div>
      <span class="eyebrow">Why this may resonate with Jack Dorsey and investors like him</span>
      <h2>A creator-seller network for culture, built on open-money instincts without forcing end users into crypto complexity.</h2>
      <p class="body-lg">This project is especially aligned for people who care about creator sovereignty, direct seller economics, self-custody options, open protocols, and systems that reduce dependency on centralized choke points.</p>
      <ul class="checklist">
        <li>It maps to the logic of empowering sellers rather than extracting them.</li>
        <li>It can use bitcoin or stablecoin rails where they increase resilience and payout optionality.</li>
        <li>It respects self-custody and portability without making mainstream users learn wallet theater.</li>
        <li>It fits a world where open financial infrastructure and creator entrepreneurship increasingly blur together.</li>
      </ul>
    </div>
    <div class="panel panel-strong">
      <h3>Why this is more than “media”</h3>
      <p class="body-md">It is closer to a rights-aware seller network for film than a generic content play. That matters because seller tools, payment rails, audience ownership, and self-custody patterns are more defensible than trying to out-feed incumbents on generic entertainment.</p>
      <div class="ribbon">If you care about open money, artist entrepreneurship, self-custody, and resilient systems, this category is legible in your language.</div>
    </div>
  </div>
</section>

<section>
  <div class="container section-head">
    <span class="eyebrow">Architecture moat</span>
    <h2>Modular where it should be. Centralized where it must be.</h2>
  </div>
  <div class="grid-4 pillar-grid">
    <article class="panel"><span class="kicker">Centralized</span><h3>Curation</h3><p>Brand trust, title review, rights verification, policy, and support stay coherent.</p></article>
    <article class="panel"><span class="kicker">Modular</span><h3>Payments</h3><p>Mainstream processors for ease. Fallback or self-custody rails where continuity matters.</p></article>
    <article class="panel"><span class="kicker">Modular</span><h3>Video</h3><p>Primary commercial rail, premium DRM rail, and decentralized backup path.</p></article>
    <article class="panel"><span class="kicker">Distributed</span><h3>Circulation</h3><p>Hosts, educators, curators, and issue communities become the growth engine.</p></article>
  </div>
</section>

<section>
  <div class="container section-head">
    <span class="eyebrow">Phase logic</span>
    <h2>How to build it without dying of ambition</h2>
  </div>
  <div class="grid-4">
    <div class="panel"><span class="kicker">Phase 0</span><h3>Foundation</h3><p>Curated titles, direct checkout, secure playback, basic host requests, reserve logic.</p></div>
    <div class="panel"><span class="kicker">Phase 1</span><h3>Closed beta</h3><p>25 to 75 titles, screening requests, filmmaker dashboard, event pages, waitlist flywheel.</p></div>
    <div class="panel"><span class="kicker">Phase 2</span><h3>Resilience</h3><p>Fallback crypto acceptance, better rights controls, educational licensing, audience export.</p></div>
    <div class="panel"><span class="kicker">Phase 3</span><h3>Funding and treasury</h3><p>Support campaigns, completion funds, optional stablecoin settlements, regulated investment handoff.</p></div>
  </div>
</section>

<section id="thesis">
  <div class="container grid-2">
    <div class="panel form-shell">
      <span class="eyebrow">Investor lead magnet</span>
      <h2>The Narrative Sovereignty Thesis</h2>
      <p class="body-md">A clean investor brief covering category, problem, why now, model, moat, architecture, risk map, and phased go-to-market.</p>
      <ul class="checklist">
        <li>Why “anti-YouTube for film” is the wrong mental model</li>
        <li>Why transaction-first beats ad dependence in this category</li>
        <li>Why open-money aligned infrastructure matters even if the UX stays mainstream</li>
        <li>Why local screening rights turn culture into a seller network</li>
      </ul>
    </div>
    <div class="form-shell" id="investor-form">
      <h3>Request the investor thesis</h3>
      <form action="{investor_action}" method="POST" class="form-grid">
        <input type="hidden" name="form_name" value="Investor Inquiry">
        <label><span class="kicker">Name</span><input type="text" name="name" required></label>
        <label><span class="kicker">Email</span><input type="email" name="email" required></label>
        <label><span class="kicker">Organization</span><input type="text" name="organization"></label>
        <label><span class="kicker">Interest type</span>
          <select name="interest">
            <option>Angel / early investor</option>
            <option>Strategic partner</option>
            <option>Payment / wallet infrastructure</option>
            <option>Distribution / venue partner</option>
            <option>Philanthropic / ecosystem support</option>
          </select>
        </label>
        <label><span class="kicker">What caught your attention?</span><textarea name="note" placeholder="Open money angle, rights category thesis, creator economics, resilient rails, cultural mission, other."></textarea></label>
        <button class="btn btn-primary" type="submit">Send me the thesis</button>
      </form>
    </div>
  </div>
</section>
'''

readme = f'''# UNBURIED static site

A mobile-first GitHub Pages site for a filmmaker-first distribution network.

## Files
- `index.html` – main landing page
- `filmmakers.html` – filmmaker / rights-holder page
- `hosts.html` – local screening and host page
- `investors.html` – investor thesis page
- `styles.css` – shared styles
- `script.js` – mobile nav only
- `assets/placeholders/` – placeholder SVG art blocks
- `canva-prompts.txt` – image generation prompts mapped to each placeholder
- `robots.txt`, `sitemap.xml`, `llms.txt`, `llms-full.txt`, `site.webmanifest`

## Before launch
1. Replace `https://YOURDOMAIN.com` in:
   - `index.html`
   - `filmmakers.html`
   - `hosts.html`
   - `investors.html`
   - `sitemap.xml`
   - `llms.txt`
   - `llms-full.txt`
2. Replace Formspree placeholders:
   - `YOUR_WAITLIST_FORM_ID`
   - `YOUR_FILMMAKER_FORM_ID`
   - `YOUR_INVESTOR_FORM_ID`
3. Swap placeholder SVGs with final images.
4. Verify trademark and domain availability for the working brand name `UNBURIED`.

## GitHub Pages
Push the files to a public repo and enable GitHub Pages from the root. GitHub Pages can serve static HTML, CSS, and JS directly from a repository.

## Notes
- Built with semantic HTML for strong crawlability.
- Mobile-first layout.
- Includes canonical tags, OG tags, FAQ schema, sitemap, robots, and llms files.
- No build step required.
'''

robots = f'''User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
'''

sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{base_url}/index.html</loc></url>
  <url><loc>{base_url}/filmmakers.html</loc></url>
  <url><loc>{base_url}/hosts.html</loc></url>
  <url><loc>{base_url}/investors.html</loc></url>
</urlset>
'''

manifest = '''{
  "name": "UNBURIED",
  "short_name": "UNBURIED",
  "start_url": "/index.html",
  "display": "standalone",
  "background_color": "#06070a",
  "theme_color": "#06070a",
  "icons": [
    {
      "src": "assets/icons/favicon.svg",
      "sizes": "any",
      "type": "image/svg+xml"
    }
  ]
}
'''

llms = f'''# UNBURIED
> Sovereign distribution for important films.

- Home: {base_url}/index.html
- For Filmmakers: {base_url}/filmmakers.html
- For Hosts: {base_url}/hosts.html
- For Investors: {base_url}/investors.html

UNBURIED is a filmmaker-first distribution network built for high-friction, culturally important films facing structural distribution resistance.
'''

llms_full = f'''# UNBURIED full guide

UNBURIED is a premium, mobile-first, filmmaker-first distribution network with a broad umbrella brand and an explicit flagship lane for films facing structural distribution friction.

## Core dream client
Independent filmmakers and small rights-holding teams with high-friction, culturally important films that cannot reliably get fair distribution through the normal system.

## Core promise
Keep your rights. Own your audience. Activate direct purchases, local screening rights, educational licenses, and later support funding from one coherent operating system.

## Pages
- {base_url}/index.html – market story, waitlist, lead magnet
- {base_url}/filmmakers.html – filmmaker operating model and economics
- {base_url}/hosts.html – local screening rights and host workflow
- {base_url}/investors.html – thesis, architecture, and partner fit
'''

prompts = '''UNBURIED image prompt handoff
============================

Style system for all images
---------------------------
Create cinematic, premium, contemporary editorial images for a dark luxury website about sovereign film distribution. No cheesy sci-fi. No obvious AI slop. No warped anatomy. No random text in image. Lighting should feel expensive, precise, and atmospheric. Blend tactile cinema craft, modern network intelligence, and subtle resistance energy. Use deep charcoal, obsidian, warm amber, muted brass, and electric cyan highlights. Mobile-first composition. Negative space for text overlays. Premium independent-film aesthetics, not startup stock-photo clichés.

1) URL: /index.html
   Image file: assets/placeholders/home-hero.svg
   Placement: Homepage hero
   Prompt:
   "A breathtaking cinematic threshold image for a premium film-distribution brand. A dark, elegant screening environment opens into a luminous horizon of many small city lights connected by subtle lines, suggesting films traveling through living communities instead of platforms. The mood is sovereign, emotionally charged, premium, and hopeful. No people visible. No text. Deep obsidian blacks, warm projector amber, brushed metal, and a few precise cyan accents. Vertical-friendly crop."

2) URL: /index.html
   Image file: assets/placeholders/home-network.svg
   Placement: Why now / network section
   Prompt:
   "An editorial-style map-of-culture image showing independent film circulation across cities. Think abstract geographic nodes, glowing screening rooms, intimate venues, and subtle rights pathways. Sophisticated, beautiful, and legible. No cheesy world map. No text. Dark luxury palette with warm light trails and refined cyan signal lines."

3) URL: /filmmakers.html
   Image file: assets/placeholders/filmmakers-hero.svg
   Placement: Filmmakers page hero
   Prompt:
   "A powerful image of a lone filmmaker's work moving from isolation into circulation. A pristine film frame, poster wall, or edit suite opens toward a constellation of screenings, audiences, and revenue pathways. The image should feel emotionally relieving and premium, like burden turning into leverage. No distorted human faces. No text. Rich contrast, tactile materials, cinematic realism."

4) URL: /filmmakers.html
   Image file: assets/placeholders/payments-rails.svg
   Placement: Money and rights section
   Prompt:
   "A sophisticated visual metaphor for braided payment and rights rails in a modern media network. Multiple elegant streams of light and data move through secure channels into filmmaker, host, and platform nodes. It should communicate resilience, modularity, and clarity, not crypto hype. Premium fintech-meets-cinema art direction. No logos. No text."

5) URL: /hosts.html
   Image file: assets/placeholders/hosts-hero.svg
   Placement: Hosts page hero
   Prompt:
   "An intimate, high-design local film gathering in a beautiful independent venue. Small audience, emotionally engaged, warm projector light, subtle diversity, refined staging. It should feel like cultural energy, trust, and meaningful presence. Not generic conference energy. No text. Premium documentary editorial style."

6) URL: /hosts.html
   Image file: assets/placeholders/hosts-event.svg
   Placement: Host flow section
   Prompt:
   "A striking visual of a local screening event system in motion: event page, venue, projector light, ticketing, and audience gathering abstracted into one beautiful cinematic composition. Must feel organized, inspiring, and real. Dark modern interface vibe blended with physical cultural venue energy. No text."

7) URL: /investors.html
   Image file: assets/placeholders/investors-hero.svg
   Placement: Investors page hero
   Prompt:
   "A premium investor-facing hero image for a next-generation film commerce network. Elegant dark dashboard surfaces, rights pathways, city nodes, and creator revenue channels integrated into one polished visual ecosystem. It should feel like category creation, not generic SaaS. Quietly bold. Minimal but rich. No text."

8) URL: all pages / social preview
   Image file: assets/placeholders/og-cover.svg
   Placement: Open Graph social preview
   Prompt:
   "A stunning horizontal cover image for a premium, culturally disruptive film-distribution platform. Think projector beam, premium dark atmosphere, one iconic frame or lens element, and a network of subtle city lights beyond. The emotional tone is truth traveling farther. No text. Safe but edgy. Beautiful enough for social sharing and investor decks."
'''

svg_templates = {
    'home-hero.svg': ('UNBURIED HERO', 'A premium cinematic horizon for important films'),
    'home-network.svg': ('SCREENING NETWORK', 'Community nodes, circulation, and signal'),
    'filmmakers-hero.svg': ('FILMMAKER RELIEF', 'From isolated release chaos to leverage'),
    'payments-rails.svg': ('PAYMENT RAILS', 'Fiat ease, resilient options, clean rights'),
    'hosts-hero.svg': ('HOST POWER', 'Bring the film to your city'),
    'hosts-event.svg': ('EVENT FLOW', 'Screening rights, ticketing, and local gatherings'),
    'investors-hero.svg': ('INVESTOR THESIS', 'A rights-and-commerce category for culture'),
    'og-cover.svg': ('UNBURIED', 'Sovereign distribution for important films'),
}

svg_base = '''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000" role="img" aria-labelledby="t d">
<title id="t">{title}</title>
<desc id="d">{desc}</desc>
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#09111A" />
    <stop offset="55%" stop-color="#06070A" />
    <stop offset="100%" stop-color="#131117" />
  </linearGradient>
  <radialGradient id="glow1" cx="25%" cy="22%" r="50%">
    <stop offset="0%" stop-color="#71D7FF" stop-opacity="0.26" />
    <stop offset="100%" stop-color="#71D7FF" stop-opacity="0" />
  </radialGradient>
  <radialGradient id="glow2" cx="77%" cy="20%" r="35%">
    <stop offset="0%" stop-color="#F58EFF" stop-opacity="0.18" />
    <stop offset="100%" stop-color="#F58EFF" stop-opacity="0" />
  </radialGradient>
  <radialGradient id="glow3" cx="58%" cy="80%" r="45%">
    <stop offset="0%" stop-color="#F3B55F" stop-opacity="0.22" />
    <stop offset="100%" stop-color="#F3B55F" stop-opacity="0" />
  </radialGradient>
</defs>
<rect width="1600" height="1000" fill="url(#bg)" />
<rect width="1600" height="1000" fill="url(#glow1)" />
<rect width="1600" height="1000" fill="url(#glow2)" />
<rect width="1600" height="1000" fill="url(#glow3)" />
<g stroke="#FFFFFF" stroke-opacity="0.08">
  <path d="M0 130H1600" />
  <path d="M0 320H1600" />
  <path d="M0 510H1600" />
  <path d="M0 700H1600" />
  <path d="M0 890H1600" />
  <path d="M160 0V1000" />
  <path d="M480 0V1000" />
  <path d="M800 0V1000" />
  <path d="M1120 0V1000" />
  <path d="M1440 0V1000" />
</g>
<g>
  <circle cx="180" cy="180" r="12" fill="#71D7FF" fill-opacity="0.75" />
  <circle cx="350" cy="280" r="10" fill="#F3B55F" fill-opacity="0.7" />
  <circle cx="510" cy="230" r="8" fill="#71D7FF" fill-opacity="0.62" />
  <circle cx="1160" cy="220" r="9" fill="#F58EFF" fill-opacity="0.62" />
  <circle cx="1300" cy="300" r="7" fill="#F3B55F" fill-opacity="0.68" />
  <circle cx="970" cy="700" r="10" fill="#71D7FF" fill-opacity="0.64" />
  <circle cx="1200" cy="760" r="14" fill="#F3B55F" fill-opacity="0.64" />
  <circle cx="430" cy="720" r="9" fill="#F58EFF" fill-opacity="0.62" />
</g>
<g stroke="#71D7FF" stroke-opacity="0.18" stroke-width="2" fill="none">
  <path d="M180 180C300 210 370 250 510 230" />
  <path d="M510 230C680 260 940 205 1160 220" />
  <path d="M430 720C560 650 780 640 970 700" />
  <path d="M970 700C1050 710 1120 732 1200 760" />
</g>
<g>
  <rect x="140" y="610" width="1320" height="220" rx="30" fill="#0B121A" fill-opacity="0.72" stroke="#FFFFFF" stroke-opacity="0.08"/>
  <text x="210" y="702" fill="#F4F7FB" font-family="Inter,Arial,sans-serif" font-size="88" font-weight="800" letter-spacing="2">{title}</text>
  <text x="212" y="772" fill="#B8C1D1" font-family="Inter,Arial,sans-serif" font-size="34">{desc}</text>
</g>
</svg>
'''

(root / 'styles.css').write_text(style)
(root / 'script.js').write_text(script)
(root / 'README.md').write_text(readme)
(root / 'robots.txt').write_text(robots)
(root / 'sitemap.xml').write_text(sitemap)
(root / 'site.webmanifest').write_text(manifest)
(root / 'llms.txt').write_text(llms)
(root / 'llms-full.txt').write_text(llms_full)
(root / 'canva-prompts.txt').write_text(prompts)
(root / 'index.html').write_text(shell('UNBURIED | Sovereign distribution for important films', 'A filmmaker-first distribution network for important independent films facing structural distribution friction.', 'index.html', index_content, index_schema))
(root / 'filmmakers.html').write_text(shell('For Filmmakers | UNBURIED', 'Keep your rights, own your audience, and activate direct revenue, local screenings, and resilient distribution.', 'filmmakers.html', filmmakers_content, filmmakers_schema))
(root / 'hosts.html').write_text(shell('For Hosts | UNBURIED', 'Bring important films to your city with simple screening rights, event flows, and fair revenue logic.', 'hosts.html', hosts_content, hosts_schema))
(root / 'investors.html').write_text(shell('Investor Thesis | UNBURIED', 'A rights-and-commerce category for high-friction films, built for direct creator economics and resilient rails.', 'investors.html', investors_content, investors_schema))

favicon = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="UNBURIED icon"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#F3B55F"/><stop offset="100%" stop-color="#71D7FF"/></linearGradient></defs><rect x="16" y="16" width="32" height="32" rx="7" transform="rotate(45 32 32)" fill="url(#g)"/><circle cx="32" cy="32" r="6" fill="#06070a" opacity="0.85"/></svg>'''
(root / 'assets' / 'icons' / 'favicon.svg').write_text(favicon)

for filename, (title, desc) in svg_templates.items():
    (root / 'assets' / 'placeholders' / filename).write_text(svg_base.format(title=title, desc=desc))

print('Site generated at', root)
