# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
# from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_static_digest import FlaskStaticDigest
from flask_wtf.csrf import CSRFProtect
from flask_bootstrap import Bootstrap
from eternity_backend_server.blueprints.dispatch.server import DispatchQueue


bcrypt = Bcrypt()
csrf_protect = CSRFProtect()
# login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
cache = Cache()
debug_toolbar = DebugToolbarExtension()
flask_static_digest = FlaskStaticDigest()
bootstrap = Bootstrap()
global dispatchList
dispatchList = DispatchQueue()

# global dispatchList
# @login_manager.user_loader
# def load_user(user_id):
#     from eternity_backend_server.blueprints.public.models import User
#     if User.query.get(int(user_id)) is not None:
#         user = User.query.get(int(user_id))
#         return user
#
# login_manager.login_view = 'public.login'
# login_manager.login_message_category = 'info'
# login_manager.login_message = 'Access denied.'


# class InvalidSystemClock(Exception):
#     """
#     时钟回拨异常
#     """
#     pass
#
# class ValidationError(Exception):
#     pass
#
#
# class BadSignature(Exception):
#     pass