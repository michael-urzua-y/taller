from flask import Flask

from .core.config import get_config
from .core.security import register_error_handlers, register_response_security
from .web.routes import site


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(get_config())

    register_response_security(app)
    register_error_handlers(app)
    app.register_blueprint(site)

    return app
