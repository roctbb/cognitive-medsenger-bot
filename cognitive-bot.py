import json
import time
from threading import Thread
from flask import Flask, request, render_template
from config import *
import threading
import datetime
from flask_sqlalchemy import SQLAlchemy
from agents_api import *

app = Flask(__name__)
#db_string = "postgres://{}:{}@{}:{}/{}".format(DB_LOGIN, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE)
#app.config['SQLALCHEMY_DATABASE_URI'] = db_string
#db = SQLAlchemy(app)

@app.route('/status', methods=['POST'])
def status():
    data = request.json

    if data['api_key'] != APP_KEY:
        return 'invalid key'

    answer = {
        "is_tracking_data": False,
        "supported_scenarios": ['memoryclinic'],
        "tracked_contracts": []
    }

    return json.dumps(answer)

@app.route('/init', methods=['POST'])
def init():
    data = request.json

    if data['api_key'] != APP_KEY:
        return 'invalid key'

    send_message(data['contract_id'], "Пройдите тестирование на уровень когнитивных навыков.", "/testing", "Пройти", only_patient=True, action_big=True)
    return 'ok'

@app.route('/settings', methods=['GET'])
def settings():
    key = request.args.get('api_key', '')

    if key != APP_KEY:
        return "<strong>Некорректный ключ доступа.</strong> Свяжитесь с технической поддержкой."

    return "In development"

@app.route('/message', methods=['POST'])
def save_message():
    data = request.json
    key = data['api_key']

    if key != APP_KEY:
        return "<strong>Некорректный ключ доступа.</strong> Свяжитесь с технической поддержкой."

    return "ok"

@app.route('/', methods=['GET'])
def index():
    return 'waiting for the thunder!'


@app.route('/remove', methods=['POST'])
def remove():
    return 'ok'

@app.route('/testing')
def testing():
    return render_template('diagnostics.html')

def url(to):
    return "http://" + EXTERNAL_HOST + ":" + PORT + to

app.jinja_env.globals.update(url=url)
if USE_SSL:
    app.run(host=HOST, port=PORT, ssl_context=SSL_CONTEXT)
else:
    app.run(host=HOST, port=PORT, debug=True)
