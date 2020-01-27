from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension
from .config import config_by_name

# Login Configuration
login_manager = LoginManager()
login_manager.session_protection ='strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()
moment = Moment()
toolbar = DebugToolbarExtension()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    db.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)
    toolbar.init_app(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .questions import questions as questions_blueprint
    app.register_blueprint(questions_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .quiz import tests as tests_blueprint
    app.register_blueprint(tests_blueprint)

    return app

import models
