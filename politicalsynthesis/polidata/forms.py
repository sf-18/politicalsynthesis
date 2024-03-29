from django import forms

class LocationForm(forms.Form):
	states = [['AL','AL'], ['AK','AK'], ['AZ','AZ'], ['AR','AR'], ['CA','CA'], ['CO','CO'], ['CT','CT'], ['DE','DE'], ['FL','FL'], ['GA','GA']
	, ['HI','HI'], ['ID','ID'], ['IL','IL'], ['IN','IN'], ['IA','IA'], ['KS','KS'], ['KY','KY'], ['LA','LA'], ['ME','ME'], ['MD','MD'], ['MA','MA'], ['MI','MI']
	, ['MN','MN'], ['MS','MS'], ['MO','MO'], ['MT','MT'], ['NE','NE'], ['NV','NV'], ['NH','NH'], ['NJ','NJ'], ['NM','NM'], ['NY','NY'], ['NC','NC'], ['ND','ND']
	, ['OH','OH'], ['OK','OK'], ['OR','OR'], ['PA','PA'], ['RI','RI'], ['SC','SC'], ['SD','SD'], ['TN','TN'], ['TX','TX'], ['UT','UT'], ['VT','VT'], ['VA','VA'], ['WA','WA']
	, ['WV','WV'], ['WI','WI'], ['WY','WY']]
	zip_code = forms.CharField(label='Zip Code', max_length=15)
	state = forms.ChoiceField(choices=states)

class RaceForm(forms.Form):
	positions = [['P', 'President'],['H', 'Representative'], ['S', 'Senate']]
	race = forms.ChoiceField(choices=positions)