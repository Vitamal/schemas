from django.db import models
from . import BaseModel, Schema


class GeneratedFile(BaseModel):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name='files')
    file_name = models.URLField()
    is_generated = models.BooleanField(default=False)
