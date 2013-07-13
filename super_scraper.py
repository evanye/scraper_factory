from bs4 import BeautifulSoup
import urllib2
import re

cat_url = "http://facts.randomhistory.com/interesting-facts-about-cats.html"
dog_url = "http://facts.randomhistory.com/2009/02/15_dogs.html"
dog_url2 = "http://www.petfinder.com/dogs/bringing-a-dog-home/facts-about-new-dog/"
bay_area_url = "http://www.buzzfeed.com/nataliemorin/26-awesome-things-the-bay-area-does-right"

html = urllib2.urlopen(bay_area_url).read()



def produceObjects(html, html_classes, classes, isCSS):
	ans = []
	soup = BeautifulSoup(html)
	sentence = ""
	if isCSS:
		css_texts = soup.select(classes[0]) #css 
		raw_texts = soup(html_classes[0], text = re.compile(r'<[a-zA-Z0-9]*\b[^>]*>(.*?)</[a-zA-Z0-9]*>'))
		for text in css_texts:
			for string in raw_texts: 
				string_elem = string.encode('utf-8')
				text_elem = text.encode('utf-8')
				m = re.findall(r'<[a-zA-Z0-9]*\b[^>]*>(.*?)</[a-zA-Z0-9]*>', text_elem)
				mylist = [x for x in m if not x is '']
				mylist2 = [y for y in n if not y is '']
				for s in mylist:
					for t in mylist2:
						ans.append(s + " " + t)
	if not isCSS:
		texts = soup.find_all(html_classes[0]) #just html, assuming not css
		for text in texts:
			#for deep_text in text.find_all(demarkers[1]):
			split_texts = re.split('<[a-z/]*>', text.encode('utf-8'))
			for new_text in split_texts:
				dict = re.findall(r'<?[a-zA-Z0-9./]*>?', new_text)
				mylist = [x for x in dict if not x is '']
				if (len(mylist) > 0):
					if (mylist[0][:1] is not '<'):
						string = ' '.join(str(item) for item in mylist)
						if string[-1:] is '.':
							sentence += string
							if len(sentence) > 4:
								ans.append(str(sentence))
								sentence = ""
						else:
							if len(string) > 4:
								sentence += string 
	return ans

objs = produceObjects(html, ['h2'],["span.buzz_superlist_number_inline"], True)
print objs
				