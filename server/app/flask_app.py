# -*- coding: utf-8 -*-
from flask import Flask
from server.setting import flask

app = Flask(__name__)


@app.route('', methods=['GET'])
def index():
    return None


if __name__ == '__main__':
    app.run(host=flask.HOST_USRL, port=8080)
