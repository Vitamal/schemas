from django.db import models
from . import BaseModel, Schema


class GeneratedScheme(BaseModel):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='schemas/')
    is_generated = models.BooleanField(default=False)
