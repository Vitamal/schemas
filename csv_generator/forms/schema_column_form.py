from django import forms
from django.utils.translation import gettext_lazy as _
from csv_generator.models import Schema, SchemaColumn


class SchemaColumnForm(forms.ModelForm):
    class Meta:
        model = SchemaColumn
        fields = ['name', 'type', 'from_field', 'to_field', 'order']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'type': forms.Select(
                attrs={'class': 'form-control', 'required': True}),
            'from_field': forms.NumberInput(
                attrs={'class': 'form-control', 'required': False, 'min_value': 0, 'max_value': 100}),
            'to_field': forms.NumberInput(
                attrs={'class': 'form-control', 'required': False, 'min_value': 1, 'max_value': 100}),
            'order': forms.NumberInput(
                attrs={'class': 'form-control', 'required': False, 'min_value': 0, 'max_value': 100}),
        }
        labels = {
            'name': _('Column Name'),
            'type': _('Type'),
            'from_field': _('From:'),
            'to_field': _('To:'),
            'order': _('Order'),
        }

    def clean(self):
        '''
            check the values of 'To' and 'From' fields if they exist
        '''

        cleaned_data = super().clean()
        to_field = cleaned_data.get("to_field")
        from_field = cleaned_data.get('from_field')

        if to_field or from_field:
            if not to_field or not from_field or to_field <= from_field:
                msg = _('The "From:" or "To:" fields is not valid!')
                self.add_error('to_field', msg)
                self.add_error('from_field', msg)
