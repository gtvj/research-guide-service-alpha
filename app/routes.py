from app import app
from flask import render_template, request, redirect
from get_fragments import *
from get_guides import *
from get_content_for_guides import *

@app.route('/ping')
def ping():
    return 'OK', 200

@app.route('/')
def root():
    return 'You should not be here. The base route is /research-guide-service'

# Service routes
@app.route('/research-guide-service/')
def home():
    return render_template('home.html', title='Research guide service')


@app.route('/research-guide-service/fragments/<path:ref>')
def fragments(ref):
    return get_fragments(ref)


@app.route('/research-guide-service/guides/<path:ref>')
def related_guides(ref):
    return get_guides(ref)


@app.route('/research-guide-service/guides_content/')
def no_content():
    return 'No reference provided'


@app.route('/research-guide-service/guides-content/<path:ref>')
def guide_content_for_reference(ref):
    guides = get_guides(ref)

    for fragment in guides:
        for i in guides[fragment]:
            guides[fragment][i] = get_content_for_guide(i)

    return guides


# No reference provided to endpoint
@app.route('/research-guide-service/guides/')
@app.route('/research-guide-service/fragments/')
@app.route('/research-guide-service/guides-content/')
def no_guides():
    return render_template('error.html', title='No reference provided', endpoint=request.path)


# Service playground
@app.route('/research-guide-service/service-playground/', methods=['POST', 'GET'])
def service_playground():
    if request.method == 'POST':
        destination = "/research-guide-service/%s/%s" % (request.form['endpoint_type'], request.form['catalogue_reference'])
        return redirect(destination)
    else:
        return render_template('endpoint_playground.html')
