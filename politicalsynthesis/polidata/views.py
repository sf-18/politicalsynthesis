from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.http import HttpResponse, HttpResponseRedirect

from .forms import LocationForm, RaceForm

from django.template import loader

from .candidate_query import get_candidates

from .summaries import get_candidate_topic_summary

from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()



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
	issues = {'Abortion':'','Defense':'',}
	candidate_first_last = candidate_name[candidate_name.index(',')+2:].lower().capitalize()+' '+candidate_name[:candidate_name.index(',')].lower().capitalize()
	#'Budget':'','Environment':'','Crime':'',
	#'Finance':'','Death_Penalty':'','Defense':'','Education':'','Russia':'','North_Korea':'',
	#'China':'','Saudi_Arabia':'','Guns':'','Gender_Equality':'','Healthcare':'','Immigration':''}
	for issue in issues:
		issues[issue] = get_candidate_topic_summary(candidate_name,issue)
	#pic_path = get_candidate_image(candidate_name)
	context = {'candidate': candidate_name, 'issues':issues, 'candidate_first_last':candidate_first_last}
	return HttpResponse(template.render(context,request))

def get_candidate_image(candidate_name):
	arguments = {"keywords": candidate_name, "limit":1,"print_urls":True}
	paths = response.download(arguments)
	return paths


