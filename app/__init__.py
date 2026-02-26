from flask import Flask 

from app.config import DevConfig
from app.controllers.auth_controller import auth_bp
from app.controllers.page_controller import page_bp
from app.extensions import bcrypt
from app.views.response import method_not_allowed, not_found, server_error

def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.url_map.strict_slashes = False

    bcrypt.init_app(app)

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(page_bp)

    register_error_handlers(app)

    return app

def register_error_handlers(app: Flask):
    @app.errorhandler(404)
    def handle_404(_):
        return not_found("endpoint_not_found")

    @app.errorhandler(405)
    def handle_405(_):
        return method_not_allowed("method_not_allowed")

    @app.errorhandler(500)
    def handle_500(_):
        return server_error("internal_server_error")
