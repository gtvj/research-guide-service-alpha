from app import app
from flask import render_template, request, redirect
from get_fragments import *
from get_guides import *
from get_content_for_guides import *


# Service routes
@app.route('/')
def home():
    return render_template('home.html', title='Research guide service')


@app.route('/fragments/<path:ref>')
def fragments(ref):
    return get_fragments(ref)


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


# No reference provided to endpoint
@app.route('/guides/')
@app.route('/fragments/')
@app.route('/guides_content/')
def no_guides():
    return render_template('error.html', title='No reference provided', endpoint=request.path)


# Service playground
@app.route('/service_playground/', methods=['POST', 'GET'])
def service_playground():
    if request.method == 'POST':
        destination = "/%s/%s" % (request.form['endpoint_type'], request.form['catalogue_reference'])
        return redirect(destination)
    else:
        return render_template('endpoint_playground.html')
