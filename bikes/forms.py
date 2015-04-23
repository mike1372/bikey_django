from django import forms

class CadenceForm(forms.Form):
    cadence = forms.CharField(label='Please select your cadence:', max_length=3)
