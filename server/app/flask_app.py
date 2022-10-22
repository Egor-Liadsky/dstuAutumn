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


@app.route('/create_task', methods=['POST'])
def create_task():
    if request.method == 'POST':
        from_id = request.args.get('from_id')
        to_id = request.args.get('to_id')
        title = request.args.get('title')
        text = request.args.get('text')
        is_secret = request.args.get('is_secret')
        time_start = request.args.get('time_start')
        time_end = request.args.get('time_end')
        result = requests.DbOperator().create_task(from_id=int(from_id), to_id=int(to_id), title=title,
                                                   text=text, is_secret=bool(is_secret), time_start=time_start, time_end=time_end)
        return result


@app.route('/update_task', methods=['POST'])
def update_task():
    if request.method == 'POST':
        task_id = request.args.get('task_id')
        from_id = request.args.get('from_id')
        to_id = request.args.get('to_id')
        title = request.args.get('title')
        text = request.args.get('text')
        is_secret = request.args.get('is_secret')
        progress_start = request.args.get('progress_start')
        progress_end = request.args.get('progress_end')
        time_start = request.args.get('time_start')
        time_end = request.args.get('time_end')
        result = requests.DbOperator().update_task(task_id=int(task_id), from_id=int(from_id), to_id=int(to_id), title=title,
                                                 text=text, is_secret=bool(is_secret), progress_start=int(progress_start),
                                                 progress_end=int(progress_end), time_start=time_start, time_end=time_end)
        return result


@app.route('/select_all_users', methods=['GET'])
def get_all_users():
    result = requests.DbOperator().select_all_user()
    return result


@app.route('/select_user_info', methods=['GET'])
def user_info():
    user_id = request.args.get('user_id')
    result = requests.DbOperator().select_user_info(id=int(user_id))
    return result


@app.route('/select_task', methods=['GET'])
def select_task():
    task_id = request.args.get('task_id')
    result = requests.DbOperator().select_task(task_id=int(task_id))
    return result


@app.route('/select_user_task', methods=['GET'])
def select_user_task():
    user_id = request.args.get('user_id')
    result = requests.DbOperator().select_user_task(user_id=int(user_id))
    return result


