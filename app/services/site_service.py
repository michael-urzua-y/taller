from __future__ import annotations

from collections import defaultdict
from copy import deepcopy

from flask import current_app

from app.domain.site_content import build_site_content
from app.services.google_reviews_service import get_google_reviews


def build_navigation() -> list[dict[str, str]]:
    return deepcopy(current_app.config["NAVIGATION"])


def resolve_page_meta(page_key: str, **kwargs) -> dict[str, str]:
    page_meta = deepcopy(current_app.config["PAGE_META"].get(page_key, {}))
    format_values = defaultdict(
        str,
        {
            "site_name": current_app.config["SITE_NAME"],
            **kwargs,
        },
    )
    return {
        "title": page_meta.get("title_template", "{site_name}").format_map(format_values),
        "description": page_meta.get("description_template", "").format_map(format_values),
    }


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
