from django.db import models
from . import BaseModel


class Schema(BaseModel):
    COMMA = ','
    SEMICOLON = ';'
    COLON = ':'
    COLUMN_SEPARATOR = [
        (COMMA, 'Comma (,)'),
        (SEMICOLON, 'Semicolon(;)'),
        (COLON, 'Colon(:)'),
    ]
    QUOTE = "'"
    DOUBLE_QUOTE = '"'
    STRING_CHARACTER = [
        (QUOTE, "Quote(')"),
        (DOUBLE_QUOTE, 'Double quote(")'),
    ]

    name = models.CharField(
        max_length=100,
        verbose_name='name'
    )
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

    def __str__(self):
        return self.name
