from django import forms

class RegisterForm(forms.Form):
	cityname=forms.CharField()
	countryname=forms.CharField()