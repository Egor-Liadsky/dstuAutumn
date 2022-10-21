from flask import Flask

app = Flask(__name__)

@app.errorhandler(404)
def not_found():
    return '404'


@app.errorhandler(400)
def not_found():
    return '400'