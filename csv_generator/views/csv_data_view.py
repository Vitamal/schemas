import pandas
from django.shortcuts import render


def data_view(request):
    print("++++++++++++++++++", request.POST)
    csvfile = request.POST['csv_file']
    data = pandas.read_csv(csvfile.name)
    data_html = data.to_html()
    context = {'loaded_data': data_html}

    return render(request, "schemas/table.html", context)
