document.documentElement.classList.add("js");

const pageKey = document.body.dataset.pageKey || "";
const skipHomeIntroKey = "skip-home-intro-once";

const revealElements = document.querySelectorAll("[data-reveal]");

function setupRevealAnimations() {
  if (!revealElements.length) {
    return;
  }

  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (prefersReducedMotion || !("IntersectionObserver" in window)) {
    revealElements.forEach((element) => element.classList.add("is-visible"));
    return;
  }

  revealElements.forEach((element) => element.classList.add("reveal-ready"));

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          return;
        }

        entry.target.classList.remove("is-visible");
      });
    },
    {
      threshold: 0.14,
      rootMargin: "0px 0px -6% 0px",
    },
  );

  revealElements.forEach((element) => observer.observe(element));
}

setupRevealAnimations();

function waitForIntroLogo() {
  const introLogo = document.querySelector(".home-intro-logo");
  if (!introLogo) {
    return Promise.resolve();
  }

  if (introLogo.complete && introLogo.naturalWidth > 0) {
    return Promise.resolve();
  }

  return new Promise((resolve) => {
    let isResolved = false;

    const finish = () => {
      if (isResolved) {
        return;
      }

      isResolved = true;
      introLogo.removeEventListener("load", finish);
      introLogo.removeEventListener("error", finish);
      resolve();
    };

    introLogo.addEventListener("load", finish, { once: true });
    introLogo.addEventListener("error", finish, { once: true });
    window.setTimeout(finish, 1800);
  });
}

function setupHomeIntro() {
  const intro = document.querySelector("#home-intro");
  if (!intro) {
    return;
  }

  const shouldSkipIntro = window.sessionStorage.getItem(skipHomeIntroKey) === "1";
  if (shouldSkipIntro) {
    window.sessionStorage.removeItem(skipHomeIntroKey);
    intro.remove();
    return;
  }

  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const introDuration = prefersReducedMotion ? 350 : 2100;

  document.body.classList.add("has-home-intro");

  waitForIntroLogo().finally(() => {
    window.setTimeout(() => {
      intro.classList.add("is-complete");
      document.body.classList.remove("has-home-intro");

      window.setTimeout(() => {
        intro.remove();
      }, 900);
    }, introDuration);
  });
}

function setupHomeNavigationIntroGuard() {
  const homeLinks = document.querySelectorAll("[data-home-link]");
  if (!homeLinks.length) {
    return;
  }

  homeLinks.forEach((link) => {
    link.addEventListener("click", () => {
      if (pageKey !== "home") {
        window.sessionStorage.setItem(skipHomeIntroKey, "1");
      }
    });
  });
}

setupHomeNavigationIntroGuard();
setupHomeIntro();

function setupProductsCategorySelect() {
  const dropdown = document.querySelector('[data-products-category-dropdown]');
  const trigger = document.querySelector('[data-products-category-trigger]');
  const current = document.querySelector('[data-products-category-current]');
  const menu = document.querySelector('[data-products-category-menu]');
  const optionsList = document.querySelector('[data-products-category-options]');
  const options = Array.from(document.querySelectorAll('[data-products-category-option]'));
  const groups = Array.from(document.querySelectorAll('[data-product-group]'));

  if (!dropdown || !trigger || !current || !menu || !options.length || !groups.length) {
    return;
  }

  let activeAnchor = options.find((option) => option.classList.contains('is-selected'))?.dataset.anchor || groups[0]?.dataset.groupAnchor || '';

  const setExpanded = (expanded) => {
    trigger.setAttribute('aria-expanded', expanded ? 'true' : 'false');
    dropdown.classList.toggle('is-open', expanded);
    menu.hidden = !expanded;
  };

  const setActiveGroup = (anchor, { shouldScroll = false } = {}) => {
    activeAnchor = anchor;

    groups.forEach((group) => {
      const isActive = group.dataset.groupAnchor === anchor;
      group.hidden = !isActive;
      group.classList.toggle('is-active', isActive);
    });

    options.forEach((option) => {
      const isSelected = option.dataset.anchor === anchor;
      option.classList.toggle('is-selected', isSelected);
      option.setAttribute('aria-selected', isSelected ? 'true' : 'false');
      if (isSelected) {
        current.textContent = option.dataset.label || option.textContent.trim();
      }
    });

    if (shouldScroll) {
      const activeGroup = document.getElementById(anchor);
      if (activeGroup) {
        activeGroup.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  };

  const focusOption = (index) => {
    const target = options[index];
    if (target) {
      target.focus();
    }
  };

  setActiveGroup(activeAnchor);
  setExpanded(false);

  trigger.addEventListener('click', () => {
    const isOpen = dropdown.classList.contains('is-open');
    setExpanded(!isOpen);
    if (!isOpen) {
      const selectedIndex = Math.max(0, options.findIndex((option) => option.dataset.anchor === activeAnchor));
      focusOption(selectedIndex);
    }
  });

  trigger.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowDown' || event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      setExpanded(true);
      const selectedIndex = Math.max(0, options.findIndex((option) => option.dataset.anchor === activeAnchor));
      focusOption(selectedIndex);
    }
  });

  options.forEach((option, index) => {
    option.addEventListener('click', () => {
      const anchor = option.dataset.anchor;
      if (!anchor) {
        return;
      }
      setActiveGroup(anchor, { shouldScroll: true });
      setExpanded(false);
      trigger.focus();
    });

    option.addEventListener('keydown', (event) => {
      if (event.key === 'ArrowDown') {
        event.preventDefault();
        focusOption((index + 1) % options.length);
      }

      if (event.key === 'ArrowUp') {
        event.preventDefault();
        focusOption((index - 1 + options.length) % options.length);
      }

      if (event.key === 'Home') {
        event.preventDefault();
        focusOption(0);
      }

      if (event.key === 'End') {
        event.preventDefault();
        focusOption(options.length - 1);
      }

      if (event.key === 'Escape') {
        event.preventDefault();
        setExpanded(false);
        trigger.focus();
      }

      if (event.key === 'Tab') {
        setExpanded(false);
      }
    });
  });

  document.addEventListener('click', (event) => {
    if (!dropdown.contains(event.target)) {
      setExpanded(false);
    }
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      setExpanded(false);
    }
  });
}

setupProductsCategorySelect();

const galleryButtons = document.querySelectorAll("[data-gallery-image]");
const galleryModal = document.querySelector("#gallery-modal");
const galleryModalClose = document.querySelector("#gallery-modal-close");
const galleryModalImage = document.querySelector("#gallery-modal-image");
const galleryModalTitle = document.querySelector("#gallery-modal-title");

function openGalleryModal(button) {
  if (!galleryModal || !galleryModalImage || !galleryModalTitle) {
    return;
  }

  galleryModalImage.src = button.dataset.galleryImage || "";
  galleryModalImage.alt = button.dataset.galleryTitle || "";
  galleryModalTitle.textContent = button.dataset.galleryTitle || "";
  galleryModal.showModal();
}

galleryButtons.forEach((button) => {
  button.addEventListener("click", () => openGalleryModal(button));
});

if (galleryModalClose && galleryModal) {
  galleryModalClose.addEventListener("click", () => galleryModal.close());
  galleryModal.addEventListener("click", (event) => {
    const dialogDimensions = galleryModal.getBoundingClientRect();
    const isOutside =
      event.clientX < dialogDimensions.left ||
      event.clientX > dialogDimensions.right ||
      event.clientY < dialogDimensions.top ||
      event.clientY > dialogDimensions.bottom;

    if (isOutside) {
      galleryModal.close();
    }
  });
}

function setupDraggableCarousel(track, prevBtn, nextBtn, itemSelector) {
  if (!track) {
    return;
  }

  function getScrollAmount() {
    const firstItem = track.querySelector(itemSelector);
    if (!firstItem) {
      return track.clientWidth * 0.9;
    }

    const styles = window.getComputedStyle(track);
    const gap = Number.parseFloat(styles.columnGap || styles.gap || "0");
    return firstItem.getBoundingClientRect().width + gap;
  }

  function scrollTrack(direction) {
    track.scrollBy({
      left: getScrollAmount() * direction,
      behavior: "smooth",
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener("click", () => scrollTrack(-1));
  }
  if (nextBtn) {
    nextBtn.addEventListener("click", () => scrollTrack(1));
  }

  let isPointerDown = false;
  let isDragging = false;
  let startX = 0;
  let startScrollLeft = 0;
  let activePointerId = null;

  function stopDragging() {
    isPointerDown = false;
    activePointerId = null;
    track.classList.remove("is-dragging");

    window.requestAnimationFrame(() => {
      isDragging = false;
    });
  }

  track.addEventListener("pointerdown", (event) => {
    if (event.pointerType === "mouse" && event.button != 0) {
      return;
    }

    isPointerDown = true;
    isDragging = false;
    activePointerId = event.pointerId;
    startX = event.clientX;
    startScrollLeft = track.scrollLeft;
    track.classList.add("is-pointer-down");
  });

  track.addEventListener("pointermove", (event) => {
    if (!isPointerDown || event.pointerId !== activePointerId) {
      return;
    }

    const deltaX = event.clientX - startX;
    if (!isDragging && Math.abs(deltaX) > 6) {
      isDragging = true;
      track.classList.add("is-dragging");
      track.classList.remove("is-pointer-down");
      track.setPointerCapture(activePointerId);
    }

    if (!isDragging) {
      return;
    }

    track.scrollLeft = startScrollLeft - deltaX;
  });

  track.addEventListener("pointerup", (event) => {
    if (event.pointerId !== activePointerId) {
      return;
    }

    if (track.hasPointerCapture(event.pointerId)) {
      track.releasePointerCapture(event.pointerId);
    }

    track.classList.remove("is-pointer-down");
    stopDragging();
  });

  track.addEventListener("pointercancel", () => {
    track.classList.remove("is-pointer-down");
    stopDragging();
  });

  track.addEventListener("lostpointercapture", () => {
    track.classList.remove("is-pointer-down");
    stopDragging();
  });

  track.addEventListener(
    "click",
    (event) => {
      if (!isDragging) {
        return;
      }

      event.preventDefault();
      event.stopPropagation();
    },
    true,
  );
}

setupDraggableCarousel(
  document.querySelector("[data-media-track]"),
  document.querySelector("[data-media-prev]"),
  document.querySelector("[data-media-next]"),
  ".media-carousel-item, .media-carousel-item-video",
);

setupDraggableCarousel(
  document.querySelector("[data-cert-track]"),
  document.querySelector("[data-cert-prev]"),
  document.querySelector("[data-cert-next]"),
  ".certification-card",
);

const certButtons = document.querySelectorAll("[data-cert-image]");
const certModal = document.querySelector("#certification-modal");
const certModalClose = document.querySelector("#certification-modal-close");
const certModalImage = document.querySelector("#certification-modal-image");
const certModalTitle = document.querySelector("#certification-modal-title");
const certModalDescription = document.querySelector("#certification-modal-description");

function openCertModal(button) {
  if (!certModal || !certModalImage || !certModalTitle || !certModalDescription) {
    return;
  }

  certModalImage.src = button.dataset.certImage || "";
  certModalImage.alt = button.dataset.certTitle || "";
  certModalTitle.textContent = button.dataset.certTitle || "";
  certModalDescription.textContent = button.dataset.certDescription || "";
  certModal.showModal();
}

certButtons.forEach((button) => {
  button.addEventListener("click", () => openCertModal(button));
});

if (certModalClose && certModal) {
  certModalClose.addEventListener("click", () => certModal.close());
  certModal.addEventListener("click", (event) => {
    const dialogDimensions = certModal.getBoundingClientRect();
    const isOutside =
      event.clientX < dialogDimensions.left ||
      event.clientX > dialogDimensions.right ||
      event.clientY < dialogDimensions.top ||
      event.clientY > dialogDimensions.bottom;

    if (isOutside) {
      certModal.close();
    }
  });
}
