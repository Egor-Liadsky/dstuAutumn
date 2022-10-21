from flask import Flask, request
from server.database import handler

app = Flask(__name__)


@app.route('/login', methods=['GET'])
def login():
    request.args.get('username')
    request.args.get('password')
    return '890'


@app.route('/', methods=['GET'])
def index():
    return "Hello world"


@app.route('/secret_key', methods=['GET'])
def secret_key():
        return {"result": requests.DbOperator().set_secret_key(request.args['secret_key'])}


@app.route('/new_user', methods=['POST'])
def secret_key():
        return {"result": requests.DbOperator().new_user(request.args['user'], request.args['secret_key'], request.args['public_key'], request.args['public_name'])}


