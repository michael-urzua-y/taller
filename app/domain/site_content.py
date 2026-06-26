from __future__ import annotations

from copy import deepcopy
from typing import Optional

from flask import current_app


def get_services_data() -> list[dict]:
    return deepcopy(current_app.config["SERVICE_CATALOG"])


def get_service_by_slug(slug: str) -> Optional[dict]:
    return next((service for service in get_services_data() if service["slug"] == slug), None)


def build_site_content() -> dict:
    content = deepcopy(current_app.config["SITE_CONTENT"])
    content["site_name"] = current_app.config["SITE_NAME"]
    content["site_copy"] = deepcopy(current_app.config["SITE_COPY"])
    content["contact"] = {
        "whatsapp_number": current_app.config["WHATSAPP_NUMBER"],
        "phone": current_app.config["CONTACT_PHONE"],
        "email": current_app.config["CONTACT_EMAIL"],
        "address": current_app.config["ADDRESS"],
        "business_hours": current_app.config["BUSINESS_HOURS"],
    }
    content["services"] = get_services_data()
    return content
