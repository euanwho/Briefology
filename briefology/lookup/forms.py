from django import forms

class LookupForm(forms.Form):
    word = forms.CharField(label='word', max_length=100)

class ExtendedLookupForm(LookupForm):
    pass