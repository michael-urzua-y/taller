from __future__ import annotations

from urllib.parse import quote

from app.schemas.contact import ContactIntent


def build_whatsapp_url(number: str, message: str) -> str:
    return f"https://wa.me/{number}?text={quote(message)}"


def build_contact_message(intent: ContactIntent) -> str:
    return (
        f"Hola, soy {intent.name}. "
        f"Quiero cotizar el servicio: {intent.service}. "
        f"Detalle: {intent.details or 'Sin detalle adicional.'}"
    )
