import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import DevelopmentConfig, ProductionConfig

app = Flask(__name__)
if os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object(ProductionConfig)
else:
    app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
ma = Marshmallow(app)

from app import models, api

# Set up logging
# Format thx to Miguel Grinberg - e.g. https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling
if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/events_app.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('API startup')
