from bs4 import BeautifulSoup
import urllib2
import re

html = urllib2.urlopen("http://facts.randomhistory.com/interesting-facts-about-cats.html").read()
soup = BeautifulSoup(html)
texts = soup.find_all('li')

for text in texts:
	split_texts = re.split('<[a-z/]*>', text.encode('utf-8'))
	for new_text in split_texts:
		dict = re.findall(r'(?<!<)[a-zA-Z0-9./]*(?!<)', new_text)
		list = [x for x in dict if not x is '']
		print '======================='
		if len(list) > 4:
			print list
		print '======================='