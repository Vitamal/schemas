from django.views.generic import ListView

from csv_generator.models import GeneratedFile, Schema
from csv_generator.views.access_mixin import SchemasAccessMixin

SCHEMAS_LIMIT_PER_PAGE = 10


class SchemasToGenerateView(SchemasAccessMixin, ListView):
    """
    the view with all generated_files instances  and with form to generate new file
    """
    context_object_name = 'generated_files'
    model = GeneratedFile
    template_name = 'schemas/schemas_generator.html'
    paginate_by = SCHEMAS_LIMIT_PER_PAGE
    ordering = ['id']

    def get_schema_id(self):
        return self.kwargs.get('schema_id')

    def get_queryset(self):
        return GeneratedFile.objects.filter(schema=Schema.objects.get(id=self.get_schema_id())).order_by('id')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['schema_id'] = self.get_schema_id()
        return context
