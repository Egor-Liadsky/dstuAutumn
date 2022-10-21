from flask import Flask, request
from server.database import handler
app = Flask(__name__)


@app.route('/test', methods=['GET'])
def index():
    return "Hello world"

@app.route('/secret_key', methods=['GET'])
def secret_key():
        return {"result": handler.Db().set_secret_key(request.args[secret_key])}