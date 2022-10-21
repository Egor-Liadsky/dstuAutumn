# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def index():
    return "Hello world"

