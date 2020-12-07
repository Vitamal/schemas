from django.views.generic import ListView

from csv_generator.models import Schema
from csv_generator.views.access_mixin import SchemasAccessMixin

SCHEMAS_LIMIT_PER_PAGE = 10


class SchemasToGenerateView(SchemasAccessMixin, ListView):
    context_object_name = 'schemas'
    model = Schema
    template_name = 'schemas/schemas_generator.html'
    paginate_by = SCHEMAS_LIMIT_PER_PAGE
    ordering = ['id']

    def get_queryset(self):
        return Schema.objects.filter(created_by=self.request.user, status=False)
