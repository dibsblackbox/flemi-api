import importlib as il
import os

from apiflask import APIFlask
from flask import Flask
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

from .common import register_commands
from .extensions import db, ma, migrate
from .models import Column, Group, Message, Post, User
from .settings import config
from .utils import get_all_remotes, remote_addr

def create_app(config_name=None) -> Flask:
    if config_name is None:
        config_name = os.getenv("FLASK_CONFIG", "development")

    app = APIFlask("flemi")
    app.wsgi_app = ProxyFix(app.wsgi_app, x_host=1)

    @app.route("/")
    def index():
        """
        API documentation for the app
        """
        return {"/": f"version 4.x of flemi web API"}

    register_config(app, config_name)
    register_blueprints(app)
    register_extensions(app)
    register_commands(app, db)
    register_context(app)

    return app

def register_config(app: Flask, config_name: str) -> None:
    app.config.from_object(config[config_name])

def register_extensions(app: Flask) -> None:
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

def register_blueprints(app: Flask) -> None:
    blueprints = []
    for mod_name in ("auth", "me", "post", "user", "group"):
        mod = il.import_module(f".api.{mod_name}.views", "flemi")
        blueprint = getattr(mod, f"{mod_name}_bp")
        CORS(blueprint)
        app.register_blueprint(blueprint)

