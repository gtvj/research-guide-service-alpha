from app import app
from flask import render_template
from get_guides import *
with open('./app/data/references_in_guides_backlinked_deduped.json') as guides:
    guides = json.load(guides)


@app.route('/')
def home():
    return render_template('home.html', title='Research guide service: Flask implementation')


@app.route('/guides/')
def no_guides():
    return 'No reference provided'


@app.route('/guides/<path:ref>')
def related_guides(ref):
    return get_guides(ref, guides)
