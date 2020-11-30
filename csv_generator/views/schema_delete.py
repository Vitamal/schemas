from django.urls import reverse_lazy
from django.views.generic import DeleteView

from csv_generator.models import Schema
from csv_generator.views.access_mixin import SchemasAccessMixin


class SchemaDeleteView(SchemasAccessMixin, DeleteView):
    model = Schema
    pk_url_kwarg = 'schema_id'
    success_url = reverse_lazy('schemas_list')
    template_name = 'schemas/schema_delete.html'
