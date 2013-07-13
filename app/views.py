from flask import render_template, request, abort, Markup
from app import app, db
from app.models import Scraper
import urllib2

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/slide2.html', methods = ['GET', 'POST'])
def slide2():
    if request.method == 'GET':
      url = request.args.get('url')
      if url is None:
        abort(404, 'need url :(')
      html = Markup(urllib2.urlopen(url).read().decode('utf-8'))
      return render_template('slide2.html', url = url, external_html = html)
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
      
      new_scraper = Scraper(url = url, name = name)
      new_scraper.set_params(params)

      db.session.add(new_scraper)
      db.session.commit()
      return render_template('index.html')
