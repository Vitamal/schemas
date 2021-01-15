"""
upload file to AWS S3
"""
import os
from pathlib import Path

import boto3
from django.http import Http404

from schemas.project.settingsproxy import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, S3_BUCKET_NAME, \
    MEDIA_ROOT

s3 = boto3.client('s3',
                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY, )


def upload_file(file_name):
    name = file_name.split('/')[-1]
    s3.upload_file(file_name, S3_BUCKET_NAME, name)


def download_file(path):
    file_name = path.split('/')[-1]
    file_path = os.path.join(MEDIA_ROOT, file_name)
    # make the directory if it isn`t exit
    Path("{}".format(MEDIA_ROOT)).mkdir(parents=True, exist_ok=True)
    print('***************************** ',Path("{}".format(MEDIA_ROOT)).exists())
    try:
        with open(file_path, 'wb') as f:
            s3.download_fileobj(S3_BUCKET_NAME, file_name, f)
    except Exception:
        print('File not found.')
        raise Http404
    return file_path
