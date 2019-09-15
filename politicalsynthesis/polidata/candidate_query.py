import os 
import datetime
import pandas as pd
import importlib
from pyopenfec.pyopenfec import Candidate

import urllib2
import simplejson
import cStringIO



#Candidate.fetch returns generator with Candidate dictionaries (hold election information, name, party)
os.environ["OPENFEC_API_KEY"] = "SwKdYJaLQBdcL459r5MNiBJtLqZqChZ8bUNuEW7Q"


now = datetime.datetime.now()
zipcode_data = pd.read_csv('zccd_hud.csv')
year = now.year
while(year%2 == 1):
	year += 1

def get_district(zipcode):
	return zipcode_data.query("zip=="+str(zipcode)).cd

def get_candidates(state, zipcode, office):
	#senate elections
	if office is 'H':
		district = get_district(zipcode)
		return Candidate.fetch(cycle=year, office=office, candidate_status='C', district=district)
	#state or presidential 
	elif office is 'S':
		return Candidate.fetch(cycle=year, office=office, candidate_status='C', state=state)
	elif office is 'P':
		return Candidate.fetch(cycle=year, office=office, candidate_status='C')
	return Candidate.fetch(cycle=year, office=office, candidate_status='C')


