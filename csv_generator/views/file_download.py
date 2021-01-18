import os
from pathlib import Path

import boto3

from django.conf import settings
from django.http import HttpResponse, Http404

s3 = boto3.client('s3',
                  aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY, )


def download(request, path):
    filename = path.split('/')[-1]
    # make the directory if it isn`t exit
    Path("{}".format(settings.MEDIA_ROOT)).mkdir(parents=True, exist_ok=True)
    try:
        s3.download_file(settings.S3_BUCKET_NAME, filename, path)
    except Exception:
        print('File not found.')
        raise Http404


    if os.path.exists(path):
        with open(path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path)
            return response
    else:
        print('The file is not found.')
        raise Http404
