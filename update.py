from app import db
from app.models import Scraper, Data
from super_scraper import crawl
from datetime import datetime

for scraper in Scraper.query.all():
    result = crawl(scraper.url, scraper.get_params())
    entry = Data(timestamp = datetime.now(), scraper = scraper)
    entry.set_data(result)
    db.add(entry)
db.commit()