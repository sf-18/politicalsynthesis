from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from .forms import LocationForm
from django.template import loader


def index(request):
	template = loader.get_template('polidata/index.html')
	if request.method == 'POST':
		form = LocationForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/polidata/candidate_list')
	else:
		form = LocationForm()
	return HttpResponse(template.render({'form':form}, request))


def location_selection(request):
    return HttpResponse("input zip and state")

def candidate_list(request):
    return HttpResponse("list of candidates")

def candidate_page(request):
    return HttpResponse("you be viewing candidate page")