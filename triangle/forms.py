from django import forms


class Hipo(forms.Form):
    cathetus1 = forms.IntegerField(label='cathetus1', min_value=0)
    cathetus2 = forms.IntegerField(label='cathetus2', min_value=0)

