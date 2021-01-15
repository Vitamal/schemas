import os
from pathlib import Path

import boto3

from schemas.project.settingsproxy import MEDIA_ROOT, DJANGOENV, S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, \
    AWS_SECRET_ACCESS_KEY
from django.http import HttpResponse, Http404

s3 = boto3.client('s3',
                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY, )


def download(request, path):
    file_path = os.path.join(MEDIA_ROOT, path)
    print('************** file name', path.split('/')[-1])
    if DJANGOENV == 'production':
        file_path = os.path.join(MEDIA_ROOT, path.split('/')[-1])
        print('************** file_path', file_path)
        print('************** S3_BUCKET_NAME', S3_BUCKET_NAME)
        # make the directory if it isn`t exit
        Path("{}".format(MEDIA_ROOT)).mkdir(parents=True, exist_ok=True)
        try:
            # s3.download_file(S3_BUCKET_NAME, path.split('/')[-1], file_path)
            with open(file_path, 'wb') as f:
                s3.download_fileobj(S3_BUCKET_NAME, path.split('/')[-1], f)
        except Exception:
            print('File not found.')
            raise Http404

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        print('The file is not found.')
        raise Http404
