from __future__ import annotations

from flask import Blueprint, abort, render_template

from app.domain.site_content import get_product_by_slug, get_related_products, get_service_by_slug
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
    meta = resolve_page_meta("products")
    return render_template(
        "products.html",
        **build_site_context("parts", **meta),
    )


@site.get("/productos")
def products():
    meta = resolve_page_meta("products")
    return render_template(
        "products.html",
        **build_site_context("parts", **meta),
    )


@site.get("/productos/<slug>")
def product_detail(slug: str):
    product = get_product_by_slug(slug)
    if product is None:
        abort(404)

    related = get_related_products(slug, limit=3)
    meta = resolve_page_meta(
        "product_detail",
        product_name=product["title"],
        product_description=product["short_description"],
    )
    return render_template(
        "product_detail.html",
        product=product,
        related_products=related,
        **build_site_context("parts", **meta),
    )


@site.get("/nosotros")
def about():
    meta = resolve_page_meta("about")
    return render_template(
        "about.html",
        **build_site_context("about", **meta),
    )
