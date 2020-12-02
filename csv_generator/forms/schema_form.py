from django import forms
from django.utils.translation import gettext_lazy as _
from csv_generator.models import Schema


class SchemaForm(forms.ModelForm):
    class Meta:
        model = Schema
        fields = ['name', 'column_separator', 'string_character']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'column_separator': forms.Select(
                attrs={'class': 'form-control', 'required': True}),
            'string_character': forms.Select(
                attrs={'class': 'form-control', 'required': True}),
        }
        labels = {
            'name': _('Name'),
            'column_separator': _('Column separator'),
            'string_character': _('String character')
        }
