from bs4 import BeautifulSoup
import urllib2
import re

cat_url = "http://facts.randomhistory.com/interesting-facts-about-cats.html"
# produceObjects(html, ['li'], [], False, "CAT_FACT")
dog_url = "http://facts.randomhistory.com/2009/02/15_dogs.html"
# produceObjects(html, ['li'], [], False, "DOG_FACT")
dog_url2 = "http://www.petfinder.com/dogs/bringing-a-dog-home/facts-about-new-dog/"
# produceObjects(html, ['p'], [], False, "DOG_FACT")
bay_area_url = "http://www.buzzfeed.com/nataliemorin/26-awesome-things-the-bay-area-does-right"
# produceObjects(html, ['h2'],["span.buzz_superlist_number_inline"], True, "BAY_AREA_AWESOME_FACT")


def crawl(url, params):
	html = urllib2.urlopen(url).read()
	data = {}
	for item in params:
		"a|class1|class2|,,," = params[item]
		html_class = params[item].split('|')[0]
		classes = params[item].split('|')[1:]
		data.extend(produceObjects(html, html_class, classes, classes.length == 0, item))
	return data

def produceObjects(html, html_class, classes, isCSS, name):
	ans = []
	dict_ans = {}
	soup = BeautifulSoup(html)
	sentence = ""
	if isCSS:
		raw_texts = soup(html_class[0])
		for string in raw_texts: 
			string_elem = string.encode('utf-8')
			m = re.findall(r'<[a-zA-Z0-9]*\b[^>]*>(.*)</[a-zA-Z0-9]*>[a-zA-Z0-9]*', string_elem)
			mylist = [x for x in m if not x is '']
			for s in mylist:
				m2 =  re.findall(r'<[a-zA-Z0-9]*\b[^>]*>(.*)</[a-zA-Z0-9]*> ([a-zA-Z0-9 .%]*)', s)
				mylist2 = [x for x in m2 if not x is '']
				for s2 in mylist2:
					ans.append(s2[0] + " " + s2[1])

	if not isCSS:
		texts = soup.find_all(html_class[0]) #just html, assuming not css
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
	dict_ans[name] = ans
	return dict_ans

objs = produceObjects(html, ['li'], [], False, "CAT_FACT")
print objs
				