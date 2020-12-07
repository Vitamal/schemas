from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from csv_generator.models import Schema, SchemaColumn
from csv_generator.utils.generator import generator_to_csv


def process_generate(request):
    if request.method == 'GET':
        return HttpResponseRedirect(request.path_info)
    elif request.method == 'POST':
        records_number = request.POST['records_number']
        schemas = Schema.objects.filter(created_by=request.user, status=False)
        for schema in schemas:
            schema_columns = SchemaColumn.objects.filter(schema=schema).values_list('name', 'type', 'from_field',
                                                                                    'to_field', 'order', named=True)
            schema_name = schema.name
            column_separator = schema.column_separator
            string_character = schema.string_character
            column_list = []
            for item in schema_columns:
                column = {}
                column['column_name'] = item.name
                column['type'] = item.type
                column['from_field'] = item.from_field
                column['to_field'] = item.to_field
                column['order'] = item.order
                column_list.append(column)
            column_list = sorted(column_list, key = lambda i: i['order'])
            generator_to_csv(schema_name, column_separator, string_character, column_list)
        return redirect('schemas_generator')
