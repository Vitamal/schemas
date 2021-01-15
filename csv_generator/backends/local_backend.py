import os

from schemas.project.settingsproxy import MEDIA_ROOT


def upload_file(file_name):
    pass


def download_file(path):
    return os.path.join(MEDIA_ROOT, path)
