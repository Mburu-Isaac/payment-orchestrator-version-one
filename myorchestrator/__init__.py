from flask import Flask

from .extensions import db, login_manager


def launch_orchestrator():

    app = Flask(__name__)

    app.config.from_object("config.Config")

    from myorchestrator import models  # noqa:F401
    from myorchestrator.routes.auth import bp as client_auth

    app.register_blueprint(client_auth, url_prefix="/auth")

    db.init_app(app)

    login_manager.init_app(app)

    login_manager.login_view = "auth/login"
    login_manager.login_message = "log in or sign up to view contents of this page"
    login_manager.login_message_category = "info"

    return app
