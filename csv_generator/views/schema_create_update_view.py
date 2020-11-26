from abc import ABCMeta

from django.urls import reverse

from csv_generator.models import Schema
from csv_generator.views.access_mixin import SchemasAccessMixin


class SchemaCreateUpdateMixin(SchemasAccessMixin, metaclass=ABCMeta):
    model = Schema
    template_name = 'create_update_schema.html'
    context_object_name = 'schema'
    object = None

    def get_success_url(self):
        return reverse('schemas_list')
