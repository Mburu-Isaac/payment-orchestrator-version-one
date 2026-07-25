from flask import Flask
from .extensions import db
from flask_login import LoginManager






def launch_app():
    
    app = Flask(__name__)

    app.config.from_object("config.Config")

    from myorchestrator import models
    from myorchestrator.routes.auth import bp as client_auth

    app.register_blueprint(client_auth, url_prefix="/auth")

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    
    login_manager.login_view = 'auth/login'
    login_manager.login_message = 'log in or sign up to view contents of this page'


    return app
    