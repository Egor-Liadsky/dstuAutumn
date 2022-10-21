# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('', methods=['GET'])
def index():
    return None


@app.errorhandler(404)
def not_found():
    return '404'


@app.errorhandler(400)
def not_found():
    return '400'


if __name__ == '__main__':
    app.run(host=., port=8080)
