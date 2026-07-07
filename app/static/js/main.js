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

const mediaTrack = document.querySelector("[data-media-track]");
const mediaPrev = document.querySelector("[data-media-prev]");
const mediaNext = document.querySelector("[data-media-next]");

function getMediaScrollAmount() {
  if (!mediaTrack) {
    return 0;
  }

  const firstItem = mediaTrack.querySelector(".media-carousel-item, .media-carousel-item-video");
  if (!firstItem) {
    return mediaTrack.clientWidth * 0.9;
  }

  const styles = window.getComputedStyle(mediaTrack);
  const gap = Number.parseFloat(styles.columnGap || styles.gap || "0");
  return firstItem.getBoundingClientRect().width + gap;
}

function scrollMediaTrack(direction) {
  if (!mediaTrack) {
    return;
  }

  mediaTrack.scrollBy({
    left: getMediaScrollAmount() * direction,
    behavior: "smooth",
  });
}

if (mediaPrev && mediaNext && mediaTrack) {
  mediaPrev.addEventListener("click", () => scrollMediaTrack(-1));
  mediaNext.addEventListener("click", () => scrollMediaTrack(1));

  let isPointerDown = false;
  let isDragging = false;
  let startX = 0;
  let startScrollLeft = 0;
  let activePointerId = null;

  function stopDragging() {
    isPointerDown = false;
    activePointerId = null;
    mediaTrack.classList.remove("is-dragging");

    window.requestAnimationFrame(() => {
      isDragging = false;
    });
  }

  mediaTrack.addEventListener("pointerdown", (event) => {
    if (event.pointerType === "mouse" && event.button != 0) {
      return;
    }

    isPointerDown = true;
    isDragging = false;
    activePointerId = event.pointerId;
    startX = event.clientX;
    startScrollLeft = mediaTrack.scrollLeft;
    mediaTrack.classList.add("is-pointer-down");
    mediaTrack.setPointerCapture(event.pointerId);
  });

  mediaTrack.addEventListener("pointermove", (event) => {
    if (!isPointerDown || event.pointerId !== activePointerId) {
      return;
    }

    const deltaX = event.clientX - startX;
    if (!isDragging && Math.abs(deltaX) > 6) {
      isDragging = true;
      mediaTrack.classList.add("is-dragging");
      mediaTrack.classList.remove("is-pointer-down");
    }

    if (!isDragging) {
      return;
    }

    mediaTrack.scrollLeft = startScrollLeft - deltaX;
  });

  mediaTrack.addEventListener("pointerup", (event) => {
    if (event.pointerId !== activePointerId) {
      return;
    }

    mediaTrack.classList.remove("is-pointer-down");
    stopDragging();
  });

  mediaTrack.addEventListener("pointercancel", () => {
    mediaTrack.classList.remove("is-pointer-down");
    stopDragging();
  });

  mediaTrack.addEventListener("lostpointercapture", () => {
    mediaTrack.classList.remove("is-pointer-down");
    stopDragging();
  });

  mediaTrack.addEventListener(
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
