from __future__ import annotations

from flask import Flask, current_app, jsonify, request


def origin_is_allowed(origin: str | None) -> bool:
    if not origin:
        return False
    allowed_origins = current_app.config.get("ALLOWED_ORIGINS", ())
    return origin.rstrip("/") in allowed_origins


def register_response_security(app: Flask) -> None:
    @app.after_request
    def apply_security_headers(response):
        origin = request.headers.get("Origin")
        if request.path.startswith("/api/") and origin_is_allowed(origin):
            response.headers["Access-Control-Allow-Origin"] = origin.rstrip("/")
            response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
            response.headers["Access-Control-Allow-Headers"] = "Content-Type"
            response.headers["Access-Control-Max-Age"] = "600"
            response.headers["Vary"] = "Origin"

        # Cache para archivos estáticos (1 semana)
        if request.path.startswith("/static/"):
            response.headers["Cache-Control"] = "public, max-age=604800, immutable"

        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
        response.headers["Cross-Origin-Opener-Policy"] = "same-origin"
        response.headers["Cross-Origin-Resource-Policy"] = "same-origin"
        if not current_app.debug:
            response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "img-src 'self' data: https://*.googleapis.com https://*.gstatic.com; "
            "style-src 'self' https://fonts.googleapis.com 'unsafe-inline'; "
            "font-src 'self' https://fonts.gstatic.com; "
            "script-src 'self'; "
            "connect-src 'self'; "
            "frame-src https://maps.google.com https://www.google.com https://maps.app.goo.gl; "
            "frame-ancestors 'none'; "
            "base-uri 'self'; "
            "form-action 'self';"
        )
        return response


def register_error_handlers(app: Flask) -> None:
    @app.errorhandler(404)
    def not_found(_error):
        return jsonify({"error": "Recurso no encontrado"}), 404

    @app.errorhandler(405)
    def method_not_allowed(_error):
        return jsonify({"error": "Método no permitido"}), 405
