from django import forms

class SettingsForm(forms.Form):
	animals = forms.BooleanField(required=False)
	kids = forms.BooleanField(required=False)
	fails = forms.BooleanField(required=False)
	stereotypes = forms.BooleanField(required=False)
	language = forms.BooleanField(required=False)
	absurd = forms.BooleanField(required=False)