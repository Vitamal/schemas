from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import ModelFormMixin, UpdateView

from csv_generator.forms import SchemaForm
from csv_generator.models import Schema
from csv_generator.views.access_mixin import SchemasAccessMixin


class SchemaCreateUpdateMixin(SchemasAccessMixin, ModelFormMixin):
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
        self.object.user = getattr(self, 'request').user

        schema_column = form.cleaned_data
        for name in Schema._meta.get_fields():
            if name.name in schema_column:
                print('remove the: ', name.name)
                schema_column.pop(name.name)
        self.object.schema_column = schema_column
        return super().form_valid(form)


# class SchemaCreateView(SchemaCreateUpdateMixin, CreateView):
#     form_class = SchemaForm
class SchemaCreateView(TemplateView):
    template_name = 'schemas/schemas_create_update.html'



class SchemaUpdateView(SchemaCreateUpdateMixin, UpdateView):

    pk_url_kwarg = 'schema_id'
    form_class = SchemaForm


