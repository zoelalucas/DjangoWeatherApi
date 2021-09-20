from django import forms

class LocationForm(forms.Form):
    location=forms.CharField(max_length=500)

    