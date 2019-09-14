from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .forms import LocationForm


def index(request):
    if request.method == 'POST':
    	form = LocationForm(request.POST)
    	if form.isValid():
    		return HttpResponseRedirect('/candidate_list')
    else:
    	form = LocationForm()
    return HttpResponse("Hello")

from django.template import loader

def index(request):
    template = loader.get_template('polidata/index.html')
    context = {"state" : "state_name"}
    return HttpResponse(template.render(context, request))


def location_selection(request):
    return HttpResponse("input zip and state")

def candidate_list(request):
    return HttpResponse("list of candidates")

def candidate_page(request):
    return HttpResponse("you be viewing candidate page")