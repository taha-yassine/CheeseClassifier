from django import forms

class IndexForm (forms.Form):
    image = forms.ImageField()