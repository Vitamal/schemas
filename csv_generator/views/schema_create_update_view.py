from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic.edit import ModelFormMixin, UpdateView

from csv_generator.forms import SchemaForm
from csv_generator.forms.schema_column_form import SchemaColumnInlineFormset
from csv_generator.models import Schema
from csv_generator.views.access_mixin import SchemasAccessMixin


class SchemaCreateUpdateMixin(SchemasAccessMixin, ModelFormMixin):
    model = Schema
    template_name = 'schemas/schemas_create_update.html'
    context_object_name = 'schema'
    object = None
    form_class = SchemaForm

    def get_success_url(self):
        return reverse('schemas_list')

    def add_object_creator(self, obj):
        if not obj.created_by:
            obj.created_by = getattr(self, 'request').user
        obj.changed_by = getattr(self, 'request').user
        obj.save()

    def form_valid(self, form):
        context = self.get_context_data()
        schema_column_formset = context['schema_column_formset']
        if schema_column_formset.is_valid():
            self.object = form.save(commit=False)
            self.add_object_creator(self.object)
            schema_column_formset.instance = self.object
            formset_object = schema_column_formset.save(commit=False)
            for obj in formset_object:
                self.add_object_creator(obj)
            schema_column_formset.save()
            return super().form_valid(form)
        else:
            form.add_error(error='Please fill Schema column fields correctly!', field=None)
            return super().form_invalid(form)

    def get_schema_column_formset(self, context):
        raise NotImplementedError()

    def get_context_data(self, **kwargs):
        """
            Add formset to the context_data.
        """
        context = super().get_context_data(**kwargs)
        context['schema_column_formset'] = self.get_schema_column_formset(context)
        return context


class SchemaCreateView(SchemaCreateUpdateMixin, CreateView):

    def get_schema_column_formset(self, context):
        if self.request.POST:
            return SchemaColumnInlineFormset(self.request.POST)
        else:
            return SchemaColumnInlineFormset()


class SchemaUpdateView(SchemaCreateUpdateMixin, UpdateView):
    pk_url_kwarg = 'schema_id'

    def get_schema_column_formset(self, context):
        schema = self.get_object()
        if self.request.POST:
            return SchemaColumnInlineFormset(self.request.POST, queryset=schema.schemacolumn_set.all(),
                                             instance=self.object)
        else:
            return SchemaColumnInlineFormset(queryset=schema.schemacolumn_set.all(), instance=self.object)

    def get_object(self, queryset=None):
        schema = super().get_object(queryset)
        return schema
