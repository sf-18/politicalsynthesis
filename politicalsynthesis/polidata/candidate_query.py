import os 
import datetime
import pandas as pd
import importlib
from pyopenfec.pyopenfec.candidate import Candidate

#Candidate.fetch returns generator with Candidate dictionaries (hold election information, name, party)
os.environ["OPENFEC_API_KEY"] = "SwKdYJaLQBdcL459r5MNiBJtLqZqChZ8bUNuEW7Q"


now = datetime.datetime.now()
zipcode_data = pd.read_csv('zccd_hud.csv')

def get_district(zipcode):
	return zipcode_data.query("zip=="+str(zipcode)).cd

def get_candidates(state, zipcode, office):
	#senate elections
	if office is 'H':
		district = get_district(zipcode)
		return module.Candidate.fetch(cycle=now.year, office=office, candidate_status='C', district=district)
	#state or presidential 
	elif office is 'S':
		return module.Candidate.fetch(cycle=now.year, office=office, candidate_status='C', state=state)
	return module.Candidate.fetch(cycle=now.year, office=office, candidate_status='C')


