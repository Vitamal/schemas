from django.db import models

from schemas.project import settingsproxy


class Schema(models.Model):
    COMMA = ','
    SEMICOLON = ';'
    COLON = ':'
    COLUMN_SEPARATOR = [
        (COMMA, 'Comma'),
        (SEMICOLON, 'Semicolon'),
        (COLON, 'Colon'),
    ]
    QOUTE = "'"
    DOUBLE_QOUTE = '"'
    STRING_CHARACTER = [
        (QOUTE, 'Quote'),
        (DOUBLE_QOUTE, 'Double quote'),
    ]

    name = models.CharField(
        max_length=100,
        verbose_name='name'
    )
    user = models.ForeignKey(to=settingsproxy.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='user')
    column_separator = models.CharField(
        max_length=1,
        choices=COLUMN_SEPARATOR,
        default=COMMA,
        verbose_name='column separator'
    )
    string_character = models.CharField(
        max_length=1,
        choices=STRING_CHARACTER,
        verbose_name='string character'
    )
    schema_column = models.JSONField(null=False, blank=True, default=dict)

