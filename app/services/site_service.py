from __future__ import annotations

from flask import current_app

from app.domain.site_content import build_site_content
from app.services.google_reviews_service import get_google_reviews


def build_navigation() -> list[dict[str, str]]:
    return [
        {"endpoint": "site.home", "label": "Inicio"},
        {"endpoint": "site.services", "label": "Servicios"},
        {"endpoint": "site.parts", "label": "Repuestos"},
        {"endpoint": "site.about", "label": "Nosotros"},
    ]


def build_site_context(page_key: str, *, title: str, description: str) -> dict:
    content = build_site_content()
    google_place, google_reviews, google_reviews_live = get_google_reviews(
        current_app.config,
        content["google_place"],
        content["google_review_cards"],
    )
    content["google_place"] = google_place
    content["google_review_cards"] = google_reviews
    content["google_reviews_live"] = google_reviews_live

    return {
        "content": content,
        "site_name": current_app.config["SITE_NAME"],
        "meta": {
            "title": title,
            "description": description,
            "page_key": page_key,
        },
        "navigation": build_navigation(),
    }
