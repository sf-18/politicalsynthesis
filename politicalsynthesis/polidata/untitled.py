import urllib.request
import simplejson
from io import StringIO

def get_image(candidate_name):
	fetcher = urllib.request.build_opener()
	startIndex = 0
	searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s" % (candidate_name)
	f = fetcher.open(searchUrl)
	deserialized_output = simplejson.load(f)

	imageUrl = deserialized_output['responseData']['results'][0]['unescapedUrl']
	file = StringIO(urllib.urlopen(imageUrl).read())
	return file 

print(get_image('taylor swift'))
