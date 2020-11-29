from django import forms
from django.utils.translation import gettext_lazy as _
from csv_generator.models import Schema


class SchemaForm(forms.ModelForm):
    column_name = forms.CharField(
        label=_('Column name'),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    type = forms.ChoiceField(
        label=_('Type'),
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=[
            ('full_name', _('Full name')),
            ('job', _('Job')),
            ('domain', _('Domain name')),
            ('phone', _('Phone number')),
            ('company', _('Company name')),
            ('text', _('Text')),
            ('integer', _('Integer')),
            ('address', _('Address')),
            ('date', _('Date')),
        ]
    )

    from_field = forms.IntegerField(
        label=_('From'),
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=0,
        max_value=1000,
        required=False
    )

    to_field = forms.IntegerField(
        label=_('To'),
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=1,
        max_value=1000,
        required=False
    )

    order = forms.IntegerField(
        label=_('Order'),
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=0,
        max_value=1000,
    )

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

    def clean(self):
        '''
            check the values of 'To' and 'From' fields if they exist
        '''

        cleaned_data = super().clean()
        to_field = cleaned_data.get("to_field")
        from_field = cleaned_data.get('from_field')

        if to_field or from_field:
            if not to_field or not from_field or to_field <= from_field :
                msg = _('The field is not valid!')
                self.add_error('to_field', msg)
                self.add_error('from_field', msg)
