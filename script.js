
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
