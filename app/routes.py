from app import app
from flask import render_template
from get_fragments import *
from get_guides import *
from get_content_for_guides import *


@app.route('/')
def home():
    return render_template('home.html', title='Research guide service: Flask implementation')


@app.route('/fragments/')
def nothing_to_fragment():
    return 'No reference provided'


@app.route('/fragments/<path:ref>')
def fragments(ref):
    return get_fragments(ref)


@app.route('/guides/')
def no_guides():
    return 'No reference provided'


@app.route('/guides/<path:ref>')
def related_guides(ref):
    return get_guides(ref)


@app.route('/guides_content/<path:ref>')
def guide_content_for_reference(ref):
    guides = get_guides(ref)

    for fragment in guides:
        for i in guides[fragment]:
            guides[fragment][i] = get_content_for_guide(i, content_of_guides)

    return guides
