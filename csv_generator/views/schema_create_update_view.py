from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView

from csv_generator.models import Schema


class SchemaCreateView(TemplateView):
    template_name = 'schemas/schemas_create_update.html'
    errors = {}

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
        if request.POST:
            name = request.POST.get('name')
            column_separator = request.POST.get('column_separator')
            string_character = request.POST.get('string_character')
            column_name = request.POST.getlist('column_name')
            sc_type = request.POST.getlist('type')
            from_num = request.POST.getlist('from_num')
            to_num = request.POST.getlist('to_num')
            order = request.POST.getlist('order')
            if self.form_validation(name, column_separator, string_character, column_name, sc_type, from_num, to_num,
                                    order):
                self.create_schema(name, column_separator, string_character, column_name, sc_type, from_num, to_num,
                                   order)
            else:
                context = self.get_context_data(
                    {'name': name, 'column_separator': column_separator, 'string_character': string_character,
                     'column_name': column_name, 'sc_type': sc_type, 'from_num': from_num, 'to_num': to_num,
                     'order': order})
                return render(request, self.template_name, context=context)
            return HttpResponseRedirect('/schemas/')
        return render(request, self.template_name)

    def form_validation(self, name, column_separator, string_character, column_name, sc_type, from_num, to_num, order):
        if not name:
            self.errors['name'] = 'Name is needed!'
            return False
        if not column_separator:
            self.errors['column_separator'] = 'The column separator is needed!'
            return False
        if not string_character:
            self.errors['string_character'] = 'The string character is needed!'
            return False
        for i in range(len(column_name)):
            if not column_name[i]:
                self.errors['column_name'] = 'The column name is needed!'
                return False
            if not sc_type[i]:
                self.errors['type'] = 'The type is needed!'
                return False
            if from_num[i] or to_num[i]:
                if not from_num[i] or not to_num[i] or int(to_num[i]) <= int(from_num[i]):
                    self.errors['from_to'] = 'The fields is invalid!'
                    return False
        return True

    def get_context_data(self, data, **kwargs):
        context = super().get_context_data(**kwargs)
        context['errors'] = self.errors
        context['form'] = data
        print('****************************', context)
        return context
