from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from csv_generator.models import Schema, SchemaColumn, GeneratedFile
from csv_generator.tasks import generator_to_csv


def process_generate(request):
    if request.method == 'GET':
        return HttpResponseRedirect(request.path_info)
    elif request.method == 'POST':
        schema_id = request.POST['schema_id']
        if request.POST['records_number']:
            records_number = int(request.POST['records_number'])
            schema = Schema.objects.get(id=schema_id)
            schema_columns = SchemaColumn.objects.filter(schema=schema).values_list('name', 'type', 'from_field',
                                                                                    'to_field', 'order', named=True)
            schema_name = schema.name
            column_separator = schema.column_separator
            string_character = schema.string_character
            column_list = []
            for item in schema_columns:
                column = {'column_name': item.name, 'type': item.type, 'from_field': item.from_field,
                          'to_field': item.to_field, 'order': item.order}
                column_list.append(column)
            column_list = sorted(column_list, key=lambda i: i['order'])
            file_name = generator_to_csv(records_number, schema_name, column_separator, string_character, column_list)
            generated_schema = GeneratedFile.objects.create(schema=schema, is_generated=True, file_name=file_name)
            print('+++++++++++++++++++', generated_schema.file_name)
        return redirect('schema_to_generate', schema_id=schema_id)
