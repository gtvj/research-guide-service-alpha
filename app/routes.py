from app import app
from flask import render_template
import json

@app.route('/')
def home():
    return render_template('home.html', title='Research guide service: Flask implementation')

@app.route('/guides/<ref>')
def guides(ref):
    with open('./app/data/references_in_guides_backlinked_deduped.json') as guides:
        guides = json.load(guides)

        if ref in guides:
            return guides[ref]
            
        return 'Nowt'
        
    