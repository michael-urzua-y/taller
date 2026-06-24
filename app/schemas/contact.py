from __future__ import annotations

from dataclasses import dataclass
from html import escape


def _clean_text(value: object, *, max_length: int) -> str:
    normalized = " ".join(str(value or "").strip().split())
    return escape(normalized[:max_length], quote=False)


@dataclass(frozen=True)
class ContactIntent:
    name: str
    service: str
    details: str


def parse_contact_intent(payload: dict | None) -> ContactIntent:
    payload = payload or {}
    intent = ContactIntent(
        name=_clean_text(payload.get("name"), max_length=80),
        service=_clean_text(payload.get("service"), max_length=80),
        details=_clean_text(payload.get("details"), max_length=300),
    )

    if len(intent.name) < 2 or len(intent.service) < 3:
        raise ValueError("Nombre y servicio son obligatorios")

    return intent
