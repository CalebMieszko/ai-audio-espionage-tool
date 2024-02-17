from flask import Flask
from app.views.audio import audio_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(audio_blueprint, url_prefix='/')
    return app
