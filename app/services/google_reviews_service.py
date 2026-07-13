from __future__ import annotations

import json
from typing import Optional
from urllib.parse import quote
from urllib.request import Request, urlopen


def _fetch_json(url: str, user_agent: str) -> dict:
    request = Request(url, headers={"User-Agent": user_agent})
    with urlopen(request, timeout=8) as response:  # nosec B310
        return json.loads(response.read().decode("utf-8"))


def _resolve_place_id(api_key: str, query: str, user_agent: str) -> Optional[str]:
    if not query:
        return None

    url = (
        "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        f"?input={quote(query)}&inputtype=textquery&fields=place_id&key={quote(api_key)}"
    )
    payload = _fetch_json(url, user_agent)
    candidates = payload.get("candidates", [])
    if not candidates:
        return None
    return candidates[0].get("place_id")


def _fetch_place_details(api_key: str, place_id: str, user_agent: str) -> Optional[dict]:
    url = (
        "https://maps.googleapis.com/maps/api/place/details/json"
        f"?place_id={quote(place_id)}"
        "&fields=name,rating,user_ratings_total,formatted_address,url,reviews"
        f"&key={quote(api_key)}"
    )
    payload = _fetch_json(url, user_agent)
    result = payload.get("result")
    if not result:
        return None
    return result


def get_google_reviews(config, fallback_place: dict, fallback_cards: list[dict]) -> tuple[dict, list[dict], bool]:
    api_key = config.get("GOOGLE_PLACES_API_KEY", "")
    maps_url = config.get("GOOGLE_PLACE_URL", fallback_place["maps_url"])
    user_agent = config.get("GOOGLE_API_USER_AGENT", "HyH-Automotriz/1.0")

    if not api_key:
        return fallback_place, fallback_cards, False

    place_id = config.get("GOOGLE_PLACE_ID", "")
    if not place_id:
        place_id = _resolve_place_id(api_key, config.get("GOOGLE_PLACE_QUERY", ""), user_agent)

    if not place_id:
        return fallback_place, fallback_cards, False

    try:
        details = _fetch_place_details(api_key, place_id, user_agent)
    except Exception:
        return fallback_place, fallback_cards, False

    if not details:
        return fallback_place, fallback_cards, False

    place = {
        "name": details.get("name", fallback_place["name"]),
        "rating": str(details.get("rating", fallback_place["rating"])),
        "address": details.get("formatted_address", fallback_place["address"]),
        "phone": fallback_place["phone"],
        "maps_url": details.get("url", maps_url) or maps_url,
    }

    reviews = []
    for review in details.get("reviews", [])[:5]:
        reviews.append(
            {
                "title": review.get("author_name", "Cliente en Google"),
                "summary": review.get("text", "").strip(),
                "cta": "Ver en Google Maps",
                "rating": review.get("rating", details.get("rating", fallback_place["rating"])),
                "relative_time": review.get("relative_time_description", ""),
                "author_url": review.get("author_url", place["maps_url"]),
            }
        )

    if not reviews:
        return fallback_place, fallback_cards, False

    return place, reviews, True
