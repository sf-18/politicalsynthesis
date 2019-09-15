"""
Summary should be a list of the abstracted summaries corresponding to the topic at keyword at thesame index.
""" 
import json
summary_file_path = "/summaries/"

def write_to_json(keywords, summary, candidate_name):
	data = {}
	for keyword in keywords:
		data[keyword] = summary
	with open(summary_file_path + candidate_name + '.json') as fp:
		json.dump(data, fp)
