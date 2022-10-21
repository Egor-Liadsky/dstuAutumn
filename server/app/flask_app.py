# -*- coding: utf-8 -*-
from flask import Flask
from server.settings import flask

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def index():
    return None

