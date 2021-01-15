import importlib
import os

from schemas.project import settingsproxy
from django.http import HttpResponse, Http404
from pathlib import Path
from schemas.project.settingsproxy import MEDIA_ROOT


def download(request, path):
    backend = importlib.import_module(getattr(settingsproxy, 'BACKEND_STORAGE'))
    file_path = backend.download_file(path)
    print('***************************** ', Path("{}".format(MEDIA_ROOT)).exists())
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        print('The file is not found.')
        raise Http404
