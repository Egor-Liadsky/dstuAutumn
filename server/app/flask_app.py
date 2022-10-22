from flask import Flask, request
from server.database import handler

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        email = request.args.get('email')
        phone = request.args.get('phone')
        result = requests.DbOperator().select_user(email, phone)
        print(result)
        return 'klk'


@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        r = request.json
        handler.Db().new_user(email=r['email'], public_name=r['name'], phone_number=r['phone'], secret_key='')
        return '-- User registered'


@app.route('/', methods=['GET'])
def index():
    return "Hello world"


@app.route('/secret_key', methods=['GET'])
def secret_key():
        return {"result": requests.DbOperator().set_secret_key(request.args['secret_key'])}


@app.route('/new_user', methods=['POST'])
def secret_key():
        return {"result": requests.DbOperator().new_user(request.args['user'], request.args['secret_key'],
                                                         request.args['public_key'], request.args['public_name'], )}


