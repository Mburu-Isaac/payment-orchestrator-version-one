from flask import Blueprint

bp = Blueprint("auth", __name__)


@bp.route("/signup")
def register_client():
    pass


@bp.route("/login")
def login_client():
    pass
