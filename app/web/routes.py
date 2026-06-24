from __future__ import annotations

from flask import Blueprint, abort, current_app, jsonify, render_template, request

from app.domain.site_content import get_service_by_slug
from app.schemas.contact import parse_contact_intent
from app.services.contact_service import build_contact_message, build_whatsapp_url
from app.services.site_service import build_site_context

site = Blueprint("site", __name__)


@site.get("/")
def home():
    return render_template(
        "home.html",
        **build_site_context(
            "home",
            title="MotorLab | Taller mecánico moderno",
            description="Taller mecánico moderno con navegación rápida, servicios, repuestos y contacto por WhatsApp.",
        ),
    )


@site.get("/servicios")
def services():
    return render_template(
        "services.html",
        **build_site_context(
            "services",
            title="Servicios | MotorLab",
            description="Servicios de mantención, frenos, suspensión, diagnóstico y atención a flotas.",
        ),
    )


@site.get("/servicios/<slug>")
def service_detail(slug: str):
    service = get_service_by_slug(slug)
    if service is None:
        abort(404)

    return render_template(
        "service_detail.html",
        service=service,
        **build_site_context(
            "services",
            title=f"{service['title']} | MotorLab",
            description=service["description"],
        ),
    )


@site.get("/repuestos")
def parts():
    return render_template(
        "parts.html",
        **build_site_context(
            "parts",
            title="Repuestos | MotorLab",
            description="Consulta de repuestos para frenos, mantención y suspensión con atención por WhatsApp.",
        ),
    )


@site.get("/nosotros")
def about():
    return render_template(
        "about.html",
        **build_site_context(
            "about",
            title="Nosotros | MotorLab",
            description="Conoce el taller, su propuesta de valor y la infraestructura digital preparada para crecer.",
        ),
    )


@site.get("/contacto")
def contact():
    return render_template(
        "contact.html",
        **build_site_context(
            "contact",
            title="Contacto | MotorLab",
            description="Cotiza o agenda tu servicio con un flujo seguro conectado a WhatsApp.",
        ),
    )


@site.route("/api/contact-intent", methods=["POST", "OPTIONS"])
def contact_intent():
    if request.method == "OPTIONS":
        return ("", 204)

    if not request.is_json:
        return jsonify({"error": "El contenido debe enviarse como JSON"}), 415

    try:
        intent = parse_contact_intent(request.get_json(silent=True))
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    message = build_contact_message(intent)
    whatsapp_url = build_whatsapp_url(current_app.config["WHATSAPP_NUMBER"], message)
    return jsonify({"whatsappUrl": whatsapp_url}), 200
