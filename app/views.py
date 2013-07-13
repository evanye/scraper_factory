from flask import render_template, request, abort
from app import app
import urllib2

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/slide2.html')
def slide2():
    url = request.args.get('url')
    if url is None:
        return abort(404, 'rar need url')
    html = urllib2.urlopen(url).read()
    return render_template('slide2.html', external_html = html)