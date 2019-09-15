from googlesearch import search
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
# from nltk.corpus import wordnet 

import re


def generate_urls(name, keyword, num_results):
	return search(name + keyword, stop=num_results)

def get_content(link):
	print(link)
	req = Request(link, headers={'User-Agent': 'Mozilla/5.0'}) # avoid block on urllib user agent
	raw_html = urlopen(req).read()
	soup = BeautifulSoup(raw_html, 'html.parser')
	return soup.get_text()

def visible(element):
	if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
		return False
	elif re.match('<!--.*-->', str(element.encode('utf-8'))):
		return False
	return True

def get_content(link):
	req = Request(link, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'}) # avoid block on urllib user agent
	raw_html = urlopen(req).read()
	soup = BeautifulSoup(raw_html, 'html.parser')
	data = soup.findAll('p')
	result = filter(visible, data)
	text = ""
	for res in result:
		snippet = res.get_text()
		if len(snippet) > 150:
			text+=snippet
	return text

keywords = ['healthcare','immigration', 'taxes', 'guns', 'climate change',
			'economy', 'abortion', 'gender and marriage equality', 'criminal justice', 'education',
			'defense', 'drugs', 'foreign policy', 'death penalty', 'defense']

# TODO - expanded keywords with nltk synsets

avoid = ['linkedin', 'twitter', 'facebook', 'wikipedia']

def get_candidate_content(candidate_name, topic):
	texts = []
	urls = generate_urls(candidate_name, topic, 25)
	for url in urls:
		if not any(site in url for site in avoid):
			texts.append(get_content(url))
	return texts

if __name__ == "__main__":
	print("here")
	print(get_candidate_content('donald trump', 'abortion'))
