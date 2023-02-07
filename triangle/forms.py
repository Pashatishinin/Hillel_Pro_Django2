from django import forms
from .models import Person
from django.forms import ModelForm


class Hipo(forms.Form):
    cathetus1 = forms.IntegerField(label='cathetus1', min_value=1)
    cathetus2 = forms.IntegerField(label='cathetus2', min_value=1)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "email"]
