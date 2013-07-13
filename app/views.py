from flask import render_template, request, abort, Markup
from app import app
import urllib2

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/slide2.html', methods = ['GET', 'POST'])
def slide2():
    url = request.args.get('url')
    if url:
      html = Markup(urllib2.urlopen(url).read().decode('utf-8'))
      return render_template('slide2.html', external_html = html)

    form = request.form
    print form
