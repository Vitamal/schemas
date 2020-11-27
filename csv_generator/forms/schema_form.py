from django import forms

from csv_generator.models import Schema


class SchemaForm(forms.ModelForm):

    class Meta:
        model = Schema
        fields = ['name', 'column_separator', 'string_character', 'schema_column']

