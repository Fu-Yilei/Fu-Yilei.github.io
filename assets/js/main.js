(() => {
  'use strict';
  document.documentElement.classList.add('js');
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#site-nav');
  if (toggle && nav) {
    toggle.hidden = false;
    const setOpen = (open) => {
      toggle.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('is-open', open);
    };
    toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
    nav.addEventListener('click', (event) => { if (event.target.closest('a')) setOpen(false); });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        toggle.focus();
      }
    });
  }
  const panel = document.querySelector('[data-publication-filters]');
  if (!panel) return;
  const input = panel.querySelector('input[type="search"]');
  const buttons = [...panel.querySelectorAll('[data-filter]')];
  const publications = [...document.querySelectorAll('[data-publication]')];
  const resultCount = document.querySelector('[data-result-count]');
  const empty = document.querySelector('[data-empty-state]');
  let status = 'all';
  const normalize = (value) => value.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const update = () => {
    const terms = normalize(input.value.trim()).split(/\s+/).filter(Boolean);
    let count = 0;
    publications.forEach((publication) => {
      const text = normalize(`${publication.dataset.search} ${publication.dataset.year}`);
      const visible = (status === 'all' || status === publication.dataset.status) && terms.every(term => text.includes(term));
      publication.hidden = !visible;
      if (visible) count += 1;
    });
    resultCount.textContent = `Showing ${count} of ${publications.length} publications and preprints`;
    empty.hidden = count !== 0;
  };
  buttons.forEach(button => button.addEventListener('click', () => {
    status = button.dataset.filter;
    buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    update();
  }));
  input.addEventListener('input', update);
  const reset = document.querySelector('[data-reset-filters]');
  reset.addEventListener('click', () => {
    input.value = '';
    buttons[0].click();
    input.focus();
  });
  panel.hidden = false;
  update();
})();
