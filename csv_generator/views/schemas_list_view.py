from django.contrib.auth import get_user_model
from django.views.generic import ListView

from csv_generator.models import Schema

SCHEMAS_LIMIT_PER_PAGE = 20


class SchemasListView(ListView):
    context_object_name = 'schemas'
    model = Schema
    template_name = 'schemas/schemas_list.html'
    paginate_by = SCHEMAS_LIMIT_PER_PAGE
    ordering = ['id']
