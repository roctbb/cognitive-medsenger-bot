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

@app.route('/')
def index():
    return render_template('diagnostics.html')

app.run(host=HOST, port=PORT)