from app import db
import simplejson as json

class Scraper(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(32), index = True, unique = True)
    url = db.Column(db.String(512), index = True)
    time = db.Column(db.Time)
    params = db.Column(db.String(4096))
    dataset = db.relationship('Data', backref = 'dataset', lazy = 'dynamic')

    def set_params(self, param_hash):
        self.params = json.dumps(param_list)

    def get_params(self):
        return json.loads(self.params)
    
    def __repr__(self):
        return "<API {0}, URL {1}, time {2}, params {3}".format(self.name, self.url, self.time, self.params)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    timestamp = db.Column(db.DateTime, index = True)
    data = db.Column(db.String(4096))
    scraper = db.Column(db.Integer, db.ForeignKey('scraper.id'))

    def set_data(self, data_hash):
        self.data = json.dumps(data_hash)

    def get_data(self):
        return json.loads(self.data)

    def __repr__(self):
        return "<DataSet: name {0}, time {1}, data {2}".format(self.scraper.name, self.timestamp, self.data)
