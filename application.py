from flask import Flask

import os
import defaults

from dotenv import load_dotenv

import logging
from utilities.logger_utilities import setup_logger

from test_db.create_db import setup_db

load_dotenv('.env')
setup_logger(defaults.logger_config)

setup_db()

app = Flask(__name__)

with app.app_context():

    import api.api_getter as api_get
    import api.api_post as api_post
    import api.api_delete as api_delete

    app.register_blueprint(api_get.api_getter)
    app.register_blueprint(api_post.api_post)
    app.register_blueprint(api_delete.api_delete)

    @app.route('/')
    def index():
        return "Main page"
