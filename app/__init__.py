from flask import Flask
from config import Config


app = Flask(__name__)
# Initializing Application Configuration
app.config.from_object(Config)

from app import routes