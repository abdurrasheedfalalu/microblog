from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel

import logging
from logging.handlers import SMTPHandler


from flask_babel import lazy_gettext as _l


app = Flask(__name__)
# Initializing Application Configuration
app.config.from_object(Config)
# Register an Extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

def get_locale():
    return "ha"

babel = Babel(app, locale_selector=get_locale)


login_manager = LoginManager(app)
login_manager.login_message = _l('Please log in to access this page.')


login_manager.login_view = 'login'
login_manager.login_message = _l('Please log in to access this page.')

from app import routes, models, errors


if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
    if app.config['MAIL_USE_TLS']:
        secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

