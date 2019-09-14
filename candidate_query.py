import os 
from pyopenfec import Candidate
import datetime
import pandas as pd

#Candidate.fetch returns generator with Candidate dictionaries (hold election information, name, party)
os.environ["OPENFEC_API_KEY"] = "tsMqfMtorhNrs79eAgIMolCFkdw03lz5WfFpwlA0"


now = datetime.datetime.now()
zipcode_data = pd.read_csv('zccd_hud.csv')

def get_district(zipcode):
	return zipcode_data.query("zip=="+str(zipcode)).cd

def get_candidates(state, zipcode, office):
	#senate elections
	if office is 'H':
		district = get_district(zipcode)
		return Candidate.fetch(cycle=now.year, office=office, candidate_status='C', district=district)
	#state or presidential 
	elif office is 'S':
		return Candidate.fetch(cycle=now.year, office=office, candidate_status='C', state=state)
	return Candidate.fetch(cycle=now.year, office=office, candidate_status='C')


