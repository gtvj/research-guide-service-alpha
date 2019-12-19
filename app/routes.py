from app import app
from flask import render_template
from reference_parser import *
import json


@app.route('/')
def home():
    return render_template('home.html', title='Research guide service: Flask implementation')


@app.route('/guides/')
def no_guides():
    return 'No reference provided'


@app.route('/guides/<path:ref>')
def guides(ref):
    with open('./app/data/references_in_guides_backlinked_deduped.json') as guides:
        guides = json.load(guides)

        if is_legacy_subclass_series(ref):
            return 'Is a legacy subclass series'
        else:
            return 'Not a legacy subclass series'
