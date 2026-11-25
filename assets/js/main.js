const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
if (menuButton && navigation) {
  menuButton.hidden = false;
  menuButton.addEventListener('click', () => {
    const open = menuButton.getAttribute('aria-expanded') !== 'true';
    menuButton.setAttribute('aria-expanded', String(open));
    navigation.classList.toggle('is-open', open);
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
      menuButton.setAttribute('aria-expanded', 'false');
      navigation.classList.remove('is-open');
      menuButton.focus();
    }
  });
}

const search = document.querySelector('#publication-search');
if (search) {
  const filters = [...document.querySelectorAll('[data-filter]')];
  const publications = [...document.querySelectorAll('[data-publication]')];
  const years = [...document.querySelectorAll('[data-year-group]')];
  const resultCount = document.querySelector('#result-count');
  const empty = document.querySelector('#empty-state');
  let selectedType = 'all';
  const normalized = value => value.normalize('NFKD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  function update() {
    const terms = normalized(search.value).trim().split(/\s+/).filter(Boolean);
    let count = 0;
    publications.forEach(publication => {
      const matchesType = selectedType === 'all' || publication.dataset.type === selectedType;
      const searchable = normalized(publication.dataset.search);
      const visible = matchesType && terms.every(term => searchable.includes(term));
      publication.hidden = !visible;
      if (visible) count++;
    });
    years.forEach(group => { group.hidden = !group.querySelector('[data-publication]:not([hidden])'); });
    resultCount.textContent = `${count} ${count === 1 ? 'publication' : 'publications'}${terms.length || selectedType !== 'all' ? ' found' : ' in this collection'}`;
    empty.hidden = count > 0;
  }
  filters.forEach(button => button.addEventListener('click', () => {
    selectedType = button.dataset.filter;
    filters.forEach(other => other.setAttribute('aria-pressed', String(other === button)));
    update();
  }));
  search.addEventListener('input', update);
  document.querySelector('[data-reset]').addEventListener('click', () => {
    selectedType = 'all'; search.value = '';
    filters.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === 'all')));
    update(); search.focus();
  });
  document.querySelector('.publication-controls').hidden = false;
  update();
}

document.querySelectorAll('[data-copy-citation]').forEach(button => {
  button.hidden = !navigator.clipboard;
  button.addEventListener('click', async () => {
    const status = button.parentElement.querySelector('[role="status"]');
    try {
      await navigator.clipboard.writeText(button.dataset.copyCitation);
      status.textContent = 'Citation copied';
    } catch {
      status.textContent = 'Copy unavailable. Use the BibTeX download above.';
    }
  });
});
