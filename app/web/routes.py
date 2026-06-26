from __future__ import annotations

from flask import Blueprint, abort, render_template

from app.domain.site_content import get_service_by_slug
from app.services.site_service import build_site_context, resolve_page_meta

site = Blueprint("site", __name__)


@site.get("/")
def home():
    meta = resolve_page_meta("home")
    return render_template(
        "home.html",
        **build_site_context("home", **meta),
    )


@site.get("/servicios")
def services():
    meta = resolve_page_meta("services")
    return render_template(
        "services.html",
        **build_site_context("services", **meta),
    )


@site.get("/servicios/<slug>")
def service_detail(slug: str):
    service = get_service_by_slug(slug)
    if service is None:
        abort(404)

    meta = resolve_page_meta(
        "service_detail",
        service_title=service["title"],
        service_description=service["description"],
    )
    return render_template(
        "service_detail.html",
        service=service,
        **build_site_context("services", **meta),
    )


@site.get("/repuestos")
def parts():
    meta = resolve_page_meta("parts")
    return render_template(
        "parts.html",
        **build_site_context("parts", **meta),
    )


@site.get("/nosotros")
def about():
    meta = resolve_page_meta("about")
    return render_template(
        "about.html",
        **build_site_context("about", **meta),
    )
