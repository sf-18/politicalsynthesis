from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.http import HttpResponse, HttpResponseRedirect

from .forms import LocationForm, RaceForm

from django.template import loader

from .candidate_query import get_candidates

import urllib2
import simplejson
import cStringIO

#default location is Boston, MA
location = {'zip': 'zip_code', 'state': 'state'}
race = ['']

def index(request):
	template = loader.get_template('polidata/polisyfront.html')
	if request.method == 'POST':
		form = LocationForm(request.POST)
		if form.is_valid():
			location['zip'] = form.cleaned_data['zip_code']
			location['state'] = form.cleaned_data['state']
			print(location['state'], location['zip'])
			return HttpResponseRedirect('/polidata/elections')
	else:
		form = LocationForm()
	return HttpResponse(template.render({'form':form}, request))
def elections(request):
	template = loader.get_template('polidata/listof.html')
	if request.method == 'POST':
		form = RaceForm(request.POST)
		if form.is_valid():
			race[0] = form.cleaned_data['race']
			print(race)
			return HttpResponseRedirect('/polidata/candidate_list')
	else:
		form = RaceForm() 
	context = {'form': form}
	return HttpResponse(template.render(context, request))


def candidate_list(request):
	template = loader.get_template('polidata/listofcandidates.html')
	print("Current state:", location['state'], "Current zip:", int(location['zip']), "Current race:", race[0])
	candidates = get_candidates(location['state'], int(location['zip']), race[0])
	print(candidates)
	cand = []
	for candidate in candidates:
		cand.append(str(candidate.name))
		print(candidate.name)
	context = {'cand': cand}
	print(cand)
	return HttpResponse(template.render(context, request))

def candidate_page(request, candidate_name):
	template = loader.get_template('polidata/polisycards.html')
	context = {'candidate': candidate_name}
	return HttpResponse(template.render(context,request))


def get_image(candidate_name):
	fetcher = urllib2.build_opener()
	startIndex = 0
	searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + candidate_name + "&start=" + startIndex
	f = fetcher.open(searchUrl)
	deserialized_output = simplejson.load(f)

	imageUrl = deserialized_output['responseData']['results'][0]['unescapedUrl']
	file = cStringIO.StringIO(urllib.urlopen(imageUrl).read())
	ge
	return file 
