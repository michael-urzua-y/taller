const form = document.querySelector("#contact-form");
const feedback = document.querySelector("#form-feedback");
const galleryButtons = document.querySelectorAll("[data-gallery-image]");
const galleryModal = document.querySelector("#gallery-modal");
const galleryModalClose = document.querySelector("#gallery-modal-close");
const galleryModalImage = document.querySelector("#gallery-modal-image");
const galleryModalTitle = document.querySelector("#gallery-modal-title");

function setFeedback(message, state) {
  if (!feedback) {
    return;
  }

  feedback.textContent = message;
  feedback.classList.remove("is-error", "is-success");
  if (state) {
    feedback.classList.add(state);
  }
}

async function submitContactIntent(event) {
  event.preventDefault();

  if (!form) {
    return;
  }

  const payload = {
    name: form.name.value,
    service: form.service.value,
    details: form.details.value,
  };

  setFeedback("Validando datos...", "");

  try {
    const response = await fetch("/api/contact-intent", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    const data = await response.json();
    if (!response.ok) {
      throw new Error(data.error || "No se pudo procesar la solicitud.");
    }

    setFeedback("Redirigiendo a WhatsApp...", "is-success");
    window.open(data.whatsappUrl, "_blank", "noopener,noreferrer");
  } catch (error) {
    setFeedback(error.message, "is-error");
  }
}

if (form) {
  form.addEventListener("submit", submitContactIntent);
}

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
