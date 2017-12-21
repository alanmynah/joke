from lxml import html
import random
import requests

def make_joke():
	identifier = str(random.randint(1, 50000))
	page = requests.get('http://bash.org/?%s.html' % identifier)
	tree = html.fromstring(page.content)
	joke = tree.xpath('//p[@class="qt"]/text()')
	return joke

def get_joke():
	proper_joke = make_joke()
	while proper_joke == []:
		proper_joke = make_joke()
	return proper_joke

print (get_joke())