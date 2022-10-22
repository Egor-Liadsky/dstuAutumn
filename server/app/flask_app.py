from flask import Flask, request
from server.database import handler, requests

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


@app.route('/create_task', methods=['POST'])
def create_task():
    if request.method == 'POST':
        from_id = request.args.get('from_id')
        to_id = request.args.get('to_id')
        title = request.args.get('title')
        text = request.args.get('text')
        is_secret = request.args.get('is_secret')
        result = requests.DbOperator().create_task(from_id=from_id, to_id=to_id, title=title, text=text, is_secret=is_secret)
        return result





@app.route('/', methods=['GET'])
def index():
    return "Hello world"

