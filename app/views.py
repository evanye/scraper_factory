from flask import render_template, request, abort, Markup
from app import app, db
from app.models import Scraper
import urllib2

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/splash.html')
def splash():
    url = request.args.get('url')
    print request.args
    if u'name' not in request.args:
      return render_template('splash.html', url = url)
    name = request.args.get('name')
    return render_template('slide2.html', url = url, name = name)

@app.route('/slide2.html', methods = ['GET', 'POST'])
def slide2():
    if request.method == 'GET':
        url = request.args.get('url')
        name = request.args.get('name')
        if url is None or name is None:
          abort(404, 'need url and name :(')
        req = urllib2.Request(url)
        req.add_header('User-Agent', "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11")
        html = Markup(urllib2.urlopen(req).read().decode('utf-8'))
        return render_template('slide2.html', url = url, name = name, external_html = html)
    elif request.method == 'POST':
        url = request.form['url']
        name = request.form['name']
        
        param_list = {}
        value_list = {}
        print request.form
        for name in request.form:
          if name == u'url' or name == u'name':
            continue
          item = request.form[name]
          if 'param' in name:
            id = name.replace('param', '')
            param_list[id] = item
          elif 'value' in name:
            id = name.replace('value', '')
            value_list[id] = item

        params = {}
        for key in param_list:
          params[param_list[key]] = value_list[key]
        print params
        new_scraper = Scraper(url = url, name = name)
        new_scraper.set_params(params)

        db.session.add(new_scraper)
        db.session.commit()
        return render_template('index.html')
