from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("landing page")

def location_selection(request):
    return HttpResponse("input zip and state")

def candidate_list(request):
    return HttpResponse("list of candidates")

def candidate_page(request):
    return HttpResponse("you be viewing candidate page")