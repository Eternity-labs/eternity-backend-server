# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
import logging
import sys

from flask import Flask, render_template, g
from flask_cors import CORS
from eternity_backend_server.blueprints.public.public import public_bp
from eternity_backend_server.blueprints.user.user import user_bp
from eternity_backend_server.blueprints.admin.admin import admin_bp
from eternity_backend_server.blueprints.datasprint.datasprint import datasprint_bp
from eternity_backend_server.blueprints.dispatch.dispatch_api import dispatch_bp
from eternity_backend_server.blueprints.ipfs.ipfs_api import ipfs_bp
from eternity_backend_server.blueprints.quantiza.quantiza_api import quantize_bp

from eternity_backend_server.extensions import (
    bcrypt,
    cache,
    csrf_protect,
    db,
    debug_toolbar,
    flask_static_digest,
    migrate,
    bootstrap,
)


def create_app(config_object="eternity_backend_server.settings"):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask('eternity_backend_server')
    with app.app_context():
        CORS(app)
        app.config.from_object(config_object)
        configure_models()
        register_extensions(app)
        register_blueprints(app)
        register_errorhandlers(app)
        register_shellcontext(app)
        # register_commands(app)
        configure_logger(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    csrf_protect.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app, db)
    flask_static_digest.init_app(app)
    bootstrap.init_app(app)


def configure_models():
    import eternity_backend_server.blueprints.public.models

def register_blueprints(app):
    """Register Flask blueprints."""

    app.register_blueprint(public_bp)
    app.register_blueprint(ipfs_bp, url_prefix='/ipfs')
    app.register_blueprint(dispatch_bp, url_prefix='/dispatch')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(quantize_bp, url_prefix='/quantize')
def register_errorhandlers(app):
    """Register error handlers."""

    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, "code", 500)
        return render_template("errors/{}.html".format(str(error_code))), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)


def register_shellcontext(app):
    """Register shell context objects."""

    def shell_context():
        """Shell context objects."""
        return {"db": db, "User": user.models.User}

    app.shell_context_processor(shell_context)


# def register_commands(app):
#     """Register Click commands."""
#     # from fisco_bcos_toolbox.commands import * 
#     app.cli.add_command(commands.test)
#     app.cli.add_command(commands.lint)


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
