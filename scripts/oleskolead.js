(() => {
  const names = {
    'commission-enquiry': 'Commission enquiry',
    'commission-brief': 'Commission brief'
  };
  const gtag = function () {
    (window.dataLayer = window.dataLayer || []).push(arguments);
  };
  const fire = (form) => {
    if (form.dataset.oleskoLeadSent) return;
    form.dataset.oleskoLeadSent = '1';
    const contentName = names[form.id] || 'Commission form';
    if (typeof window.fbq === 'function') {
      window.fbq('track', 'Lead', { content_name: contentName });
    }
    gtag('event', 'generate_lead', {
      content_name: contentName,
      event_label: contentName
    });
  };
  const isShown = (el) => {
    if (!el) return false;
    const s = window.getComputedStyle(el);
    if (s.display === 'none' || s.visibility === 'hidden') return false;
    return true;
  };
  const watch = (form) => {
    if (!form) return;
    const wrap = form.closest('.w-form');
    const done = wrap && wrap.querySelector('.w-form-done');
    const maybe = () => {
      if (
        done &&
        isShown(done) &&
        (done.style.display === 'block' ||
          window.getComputedStyle(form).display === 'none')
      ) {
        fire(form);
      }
    };
    if (done) {
      new MutationObserver(maybe).observe(wrap || done, {
        attributes: true,
        subtree: true,
        attributeFilter: ['style', 'class']
      });
    }
    form.addEventListener('submit', () => fire(form));
  };
  const init = () => {
    watch(document.getElementById('commission-enquiry'));
    watch(document.getElementById('commission-brief'));
  };
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init, { once: true });
  } else {
    init();
  }
})();
