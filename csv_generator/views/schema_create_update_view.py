from abc import ABCMeta

from django.urls import reverse
from django.views.generic import CreateView

from csv_generator.forms import SchemaForm
from csv_generator.models import Schema
from csv_generator.views.access_mixin import SchemasAccessMixin


class SchemaCreateUpdateMixin(SchemasAccessMixin, metaclass=ABCMeta):
    model = Schema
    template_name = 'schemas/schemas_create_update.html'
    context_object_name = 'schema'
    object = None

    def get_success_url(self):
        return reverse('schemas_list')

    def form_valid(self, form):
        self.object = form.save()
        if not self.object.created_by:
            self.object.created_by = getattr(self, 'request').user
        self.object.changed_by = getattr(self, 'request').user


class SchemaCreateView(SchemaCreateUpdateMixin, CreateView):
    form_class = SchemaForm
