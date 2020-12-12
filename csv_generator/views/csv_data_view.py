import pandas as pd
from django.shortcuts import render

from csv_generator.models import GeneratedFile, Schema


def data_view(request, generated_scheme_id):
    generated_file = GeneratedFile.objects.get(id=generated_scheme_id)
    schema = generated_file.schema
    file_path = generated_file.file_name
    data = pd.read_csv(filepath_or_buffer=file_path, quotechar=schema.string_character, sep=schema.column_separator)
    data_html = data.to_html()
    context = {'loaded_data': data_html}

    return render(request, "schemas/table.html", context=context)
