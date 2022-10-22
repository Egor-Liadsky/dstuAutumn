from flask import Flask, request
from server.database import requests, handler
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        email = request.args.get('email')
        phone = request.args.get('phone')
        result = requests.DbOperator().select_user(email, phone)
        return f'{result}'


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        email = request.args.get('email')
        public_name = request.args.get('name')
        phone_number = request.args.get('phone').replace('+', '')
        result = requests.DbOperator().new_user(email=email, secret_key='', public_name=public_name, phone_number=phone_number)
        return result


@app.route('/', methods=['GET'])
def index():
    return "Hello world"


@app.route('/secret_key', methods=['GET'])
def secret_key():
    # return {"result": requests.DbOperator().set_secret_key(request.args['secret_key'])}
    return None


@app.route('/new_user', methods=['POST'])
def new_user():
        return {"result": requests.DbOperator().new_user(request.args['user'], request.args['secret_key'],
                                                         request.args['public_key'], request.args['public_name'], )}


