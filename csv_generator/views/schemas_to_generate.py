from django.views.generic import ListView

from csv_generator.models import GeneratedScheme, Schema
from csv_generator.views.access_mixin import SchemasAccessMixin

SCHEMAS_LIMIT_PER_PAGE = 10


class SchemasToGenerateView(SchemasAccessMixin, ListView):
    schema_id = 'schema_id'
    context_object_name = 'generated_schemas'
    model = GeneratedScheme
    template_name = 'schemas/schemas_generator.html'
    paginate_by = SCHEMAS_LIMIT_PER_PAGE
    ordering = ['id']

    def get_queryset(self):
        return GeneratedScheme.objects.filter(scheme=Schema.objects.get(id=self.schema_id))
