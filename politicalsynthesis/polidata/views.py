from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.http import HttpResponse, HttpResponseRedirect

from .forms import LocationForm, RaceForm

from django.template import loader

#from .candidate_query import get_candidates

#default location is Boston, MA
location = {'zip': 'zip_code', 'state': 'state'}
race = ''

def index(request):
	template = loader.get_template('polidata/polisyfront.html')
	if request.method == 'POST':
		form = LocationForm(request.POST)
		if form.is_valid():
			location['zip'] = form.cleaned_data['zip_code']
			location['state'] = form.cleaned_data['state']
			return HttpResponseRedirect('/polidata/elections')
	else:
		form = LocationForm()
	return HttpResponse(template.render({'form':form}, request))
def elections(request):
	template = loader.get_template('polidata/listof.html')
	if request.method == 'POST':
		form = RaceForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['race'] == 'P':
				race = 'P'
			elif form.cleaned_data['race'] == 'H':
				race = 'H'
			else:
				race = 'S'
			return HttpResponseRedirect('/polidata/candidate_list')
	else:
		form = RaceForm() 
	context = {'races':['H', 'S', 'P'], 'form': form}
	return HttpResponse(template.render(context, request))
def candidate_list(request):
	return HttpResponse("Hello")
    #return HttpResponse(get_candidates(location['state'], int(location['zip']), 'H'))

def candidate_page(request):
    return HttpResponse("you be viewing candidate page")