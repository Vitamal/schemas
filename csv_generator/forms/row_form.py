from django import forms


class RowForm(forms.Form):
    number = forms.IntegerField()
