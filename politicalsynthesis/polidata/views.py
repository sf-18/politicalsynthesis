from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.http import HttpResponse, HttpResponseRedirect

from .forms import LocationForm

from django.template import loader

from .candidate_query import get_candidates

#default location is Boston, MA
location = {'zip': '02215', 'state': 'MA'}

def index(request):
	template = loader.get_template('polidata/index.html')
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
	return HttpResponse("Electtions")
def candidate_list(request):
	#return HttpRespone("Hello")
    return HttpResponse(get_candidates(location['state'], int(location['zip']), 'H'))

def candidate_page(request):
    return HttpResponse("you be viewing candidate page")