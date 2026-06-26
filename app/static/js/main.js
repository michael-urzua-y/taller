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
}
