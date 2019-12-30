from app import app
from flask import render_template
from get_fragments import *


@app.route('/')
def home():
    return render_template('home.html', title='Research guide service: Flask implementation')


@app.route('/guides/')
def no_guides():
    return 'No reference provided'


@app.route('/guides/<path:ref>')
def guides(ref):
    return get_fragments(ref)
