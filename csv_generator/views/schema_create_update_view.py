from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView

from csv_generator.models import Schema


class SchemaCreateView(TemplateView):
    template_name = 'schemas/schemas_create_update.html'

    def create_schema(self, name, column_separator, string_character, column_name, sc_type, from_num, to_num, order):
        schema_column = {'column_name': column_name, 'type': sc_type, 'from_num': from_num, 'to_num': to_num,
                         'order': order}
        schema = Schema.objects.create(name=name, column_separator=column_separator, string_character=string_character,
                                       schema_column=schema_column)
        if not schema.created_by:
            schema.created_by = getattr(self, 'request').user
        schema.changed_by = getattr(self, 'request').user
        schema.user = getattr(self, 'request').user
        schema.save()

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST.get('name')
            column_separator = request.POST.get('column_separator')
            string_character = request.POST.get('string_character')
            column_name = request.POST.get('column_name')
            sc_type = request.POST.get('type')
            from_num = request.POST.get('from_num')
            to_num = request.POST.get('to_num')
            order = request.POST.get('order')
            if self.form_validation(name, column_separator, string_character, column_name, sc_type, from_num, to_num, order):
                self.create_schema(name, column_separator, string_character, column_name, sc_type, from_num, to_num, order)
            return HttpResponseRedirect('/schemas/')
        return render(request, self.template_name)

    def form_validation(self, name, column_separator, string_character, column_name, sc_type, from_num, to_num, order):
        if not name:
            raise ValidationError(
                'Invalid values: %(value)',
                code='invalid',
                params={'value': 'Name'},
            )

        # for to_field, from_field in to_num, from_num:
        #     if to_field or from_field:
        #         if not to_field or not from_field or to_field <= from_field :
        #             raise ValidationError(
        #                 'Invalid values: %(value)',
        #                 code='invalid',
        #                 params={'value': 'From: To:'},
        #             )
        return True
