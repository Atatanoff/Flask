#! usr/bin/env python
# save this as app.py
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/live')
def live():
    return render_template('live.html')
