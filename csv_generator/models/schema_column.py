from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from . import BaseModel
from django.utils.translation import gettext_lazy as _


class SchemaColumn(BaseModel):
    FULL_NAME = 'Full name'
    JOB = 'Job'
    DOMAIN = 'Domain name'
    PHONE = 'Phone number'
    COMPANY = 'Company name'
    TEXT = 'Text'
    INTEGER = 'Integer'
    ADDRESS = 'Address'
    DATE = 'Date'

    TYPE = [
        (FULL_NAME, _('Full name')),
        (JOB, _('Job')),
        (DOMAIN, _('Domain name')),
        (PHONE, _('Phone number')),
        (COMPANY, _('Company name')),
        (TEXT, _('Text')),
        (INTEGER, _('Integer')),
        (ADDRESS, _('Address')),
        (DATE, _('Date')),
    ]

    name = models.CharField(max_length=100, verbose_name='column_name')

    type = models.CharField(max_length=100, choices=TYPE, verbose_name='type')

    from_field = models.IntegerField(null=True, blank=True, verbose_name='from_field',
                                     validators=[MinValueValidator(0), MaxValueValidator(1000)])

    to_field = models.IntegerField(null=True, blank=True, verbose_name='to_field',
                                   validators=[MinValueValidator(0), MaxValueValidator(1000)])

    order = models.IntegerField(null=True, blank=True, verbose_name='order',
                                validators=[MinValueValidator(0), MaxValueValidator(1000)])

    schema = models.ForeignKey('csv_generator.Schema', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
