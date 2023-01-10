#! usr/bin/env python
# save this as app.py
from flask import Flask
from flask import render_template
from .static.game_of_life import *

app = Flask(__name__)

ROW = 15
COL = 15

GameOfLife(ROW, COL)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/live')
def live():
    game = GameOfLife()
    if game.counter: game.form_new_generation()
    game.counter += 1
    return render_template('live.html', life = game)
