from django import forms

class LocationForm(forms.Form):
	zip_code = forms.CharField(label='zipcode', max_length=15)
	