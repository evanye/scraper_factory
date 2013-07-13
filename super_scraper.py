from bs4 import BeautifulSoup
import urllib2
import re

html = urllib2.urlopen("http://facts.randomhistory.com/interesting-facts-about-cats.html").read()

def produceObjects(html, demarker):
	ans = []
	soup = BeautifulSoup(html)
	texts = soup.find_all(demarker)
	sentence = ""
	for text in texts:
		split_texts = re.split('<[a-z/]*>', text.encode('utf-8'))
		for new_text in split_texts:
			dict = re.findall(r'<?[a-zA-Z0-9./]*>?', new_text)
			list = [x for x in dict if not x is '']
			if (len(list) > 0):
				if (list[0][:1] is not '<'):
					string = ' '.join(str(item) for item in list)
					if string[-1:] is '.':
						sentence += string
						if len(sentence) > 4:
							ans.append(str(sentence))
							sentence = ""
					else:
						if len(string) > 4:
							sentence += string 
	return ans

objs = produceObjects(html, "li")
				