"""
the utility to generate fake csv file
"""
import io
import csv
from datetime import datetime
from django.contrib import messages

def generator_to_csv(schema_name, column_separator, string_character, column_list):

    with open(schema_name + '.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=column_separator)
        writer.writerow([column_name_list])
    pass
