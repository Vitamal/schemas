"""
the utility to generate fake csv file
"""
import csv
import time
import boto3
from pathlib import Path

from django.conf import settings
from faker import Faker

from celery import shared_task
from celery.utils.log import get_task_logger
from csv_generator.models import GeneratedFile

logger = get_task_logger(__name__)

FULL_NAME = 'Full name'
JOB = 'Job'
DOMAIN = 'Domain name'
PHONE = 'Phone number'
COMPANY = 'Company name'
TEXT = 'Text'
INTEGER = 'Integer'
ADDRESS = 'Address'
DATE = 'Date'

faker = Faker()

s3 = boto3.client('s3',
                  aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, )


def fake_data_generator(num, column_type, from_nam, to_num):
    if column_type == FULL_NAME:
        item_list = [(faker.first_name() + faker.last_name()) for _ in range(num)]
    elif column_type == JOB:
        item_list = [faker.job() for _ in range(num)]
    elif column_type == DOMAIN:
        item_list = [faker.domain_name() for _ in range(num)]
    elif column_type == PHONE:
        item_list = [faker.phone_number() for _ in range(num)]
    elif column_type == COMPANY:
        item_list = [faker.company() for _ in range(num)]
    elif column_type == TEXT:
        item_list = [faker.text(max_nb_chars=20) for _ in range(num)]
    elif column_type == INTEGER:
        from_nam = from_nam if from_nam else 0
        to_num = to_num if to_num else 100
        item_list = [faker.random_int(from_nam, to_num) for _ in range(num)]
    elif column_type == ADDRESS:
        item_list = [faker.address() for _ in range(num)]
    elif column_type == DATE:
        item_list = [faker.date() for _ in range(num)]
    else:
        raise Exception("Sorry, the column data type is unknown.")
    return item_list


@shared_task
def generator_to_csv(records_number, schema_name, generated_item_id, column_separator, string_character, column_list):
    '''
    create the csv file with fake data
    '''

    csv.register_dialect('scheme_dialect', delimiter=column_separator, quotechar=string_character)
    column_name_list = [item['column_name'] for item in column_list]
    column_type_list = [item['type'] for item in column_list]
    list_of_columns = []
    for item in column_list:
        item_list = fake_data_generator(records_number, item['type'], item['from_field'], item['to_field'])
        list_of_columns.append(item_list)
    data_rows = list(zip(*list_of_columns))

    date_time = time.strftime("%Y%m%d-%H%M%S")
    file_name = "{}/{}_{}.csv".format(settings.MEDIA_ROOT, schema_name, date_time)

    # make the directory if it isn`t exit
    Path("{}".format(settings.MEDIA_ROOT)).mkdir(parents=True, exist_ok=True)
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file, 'scheme_dialect')
        writer.writerow(column_name_list)
        writer.writerows(data_rows)

    # upload file to AWS S3
    s3.upload_file(file_name, settings.S3_BUCKET_NAME, file_name.split('/')[-1])

    # updating generated_file instance
    generated_item = GeneratedFile.objects.get(id=generated_item_id)
    generated_item.is_generated = True
    generated_item.file_name = file_name
    generated_item.save()
