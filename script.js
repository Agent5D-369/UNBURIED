
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.nav-links');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const expanded = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!expanded));
      nav.classList.toggle('open');
    });
  }

  const progress = document.querySelector('.progress-line');
  const updateProgress = () => {
    if (!progress) return;
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    progress.style.width = `${pct}%`;
  };
  updateProgress();
  window.addEventListener('scroll', updateProgress, { passive: true });

  document.querySelectorAll('form.ajax-form').forEach(form => {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const status = form.querySelector('.form-status') || (() => {
        const el = document.createElement('p');
        el.className = 'form-status';
        form.appendChild(el);
        return el;
      })();
      status.textContent = 'Sending…';
      const formData = new FormData(form);
      formData.append('_subject', document.title);
      try {
        const res = await fetch(form.action, {
          method: 'POST',
          body: formData,
          headers: { 'Accept': 'application/json' }
        });
        if (res.ok) {
          const redirect = form.dataset.redirect;
          if (redirect) window.location.href = redirect;
          else status.textContent = 'Thanks. Your message is in.';
        } else {
          const data = await res.json().catch(() => ({}));
          status.textContent = data?.errors?.[0]?.message || 'Something went wrong. Please try again.';
        }
      } catch (err) {
        status.textContent = 'Connection issue. Please try again.';
      }
    });
  });
});
