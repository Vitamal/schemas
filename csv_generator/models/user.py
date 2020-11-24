from django.contrib.auth.models import AbstractUser
from django.db import models

from csv_generator.models.schema import Schema


class User(AbstractUser):
    schema = models.ForeignKey(Schema, models.SET_NULL, null=True, blank=True, )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
