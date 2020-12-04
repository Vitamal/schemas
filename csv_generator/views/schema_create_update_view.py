from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic.edit import ModelFormMixin, UpdateView

from csv_generator.forms import SchemaForm
from csv_generator.forms.schema_column_form import SchemaColumnInlineFormset
from csv_generator.models import Schema
from csv_generator.views.access_mixin import SchemasAccessMixin
from django.forms.models import model_to_dict


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

    # def form_formset_valid(self, form, schema_column_formset):
    #     """
    #     Called if all forms are valid. Creates a Schema instance along
    #     with associated schema_column and then redirects to a success page.
    #     """
    #     self.object = form.save()
    #     schema_column_formset.instance = self.object
    #     formset_object = schema_column_formset.save()
    #     self.add_object_creator(self.object)
    #     for obj in formset_object:
    #         self.add_object_creator(obj)
    #     return HttpResponseRedirect(self.get_success_url())

    def get_modified_schema_column_formset(self, schema_column_formset):
        return schema_column_formset

    def form_valid(self, form):
        context = self.get_context_data()
        schema_column_formset = context['schema_column_formset']

        schema_column_formset = self.get_modified_schema_column_formset(schema_column_formset)
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
            form.add_error(error=schema_column_formset.errors, field=None)
            return super().form_invalid(form)


    def get_schema_column_formset(self, context):
        raise NotImplementedError()

    def get_context_data(self, **kwargs):
        """
            Add formset to the context_data.
        """
        context = super().get_context_data(**kwargs)
        context['schema_column_formset'] = self.get_schema_column_formset(context)
        # if self.request.POST:
        #     context['form'] = self.form_class(self.request.POST)
        #     context['schema_column_formset'] = SchemaColumnInlineFormset(self.request.POST)
        # else:
        #     context['form'] = self.form_class()
        #     context['schema_column_formset'] = SchemaColumnInlineFormset()
        return context


class SchemaCreateView(SchemaCreateUpdateMixin, CreateView):

    def get_schema_column_formset(self, context):
        if self.request.POST:
            return SchemaColumnInlineFormset(self.request.POST)
        else:
            return SchemaColumnInlineFormset()

    # def get(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     schema_column_formset = SchemaColumnInlineFormset()
    #     return self.render_to_response(
    #         self.get_context_data(form=form, schema_column_formset=schema_column_formset)
    #     )
    #
    # def post(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     schema_column_formset = SchemaColumnInlineFormset(self.request.POST)
    #     if form.is_valid() and schema_column_formset.is_valid():
    #         return self.form_formset_valid(form, schema_column_formset)
    #     return self.render_to_response(
    #         self.get_context_data(form=form, schema_column_formset=schema_column_formset)
    #     )


class SchemaUpdateView(SchemaCreateUpdateMixin, UpdateView):
    pk_url_kwarg = 'schema_id'

    def get_schema_column_formset(self, context):
        schema = self.get_object()
        schema_columns = schema.schemacolumn_set.all()
        initial = self.to_list_of_dict(schema_columns)
        if self.request.POST:
            return SchemaColumnInlineFormset(self.request.POST, initial=initial, instance=self.object)
        else:
            return SchemaColumnInlineFormset(initial=initial, instance=self.object)

    def get_object(self, queryset=None):
        schema = super().get_object(queryset)
        return schema

    def to_list_of_dict(self, schema_columns):
        obj_list = []
        exclude_fields = ['id', 'created_by', 'changed_by']
        for instance in schema_columns:
            obj_list.append(model_to_dict(instance, fields=[field.name for field in instance._meta.fields if
                                                            field.name not in exclude_fields]))
        return obj_list

    def get_modified_schema_column_formset(self, schema_column_formset):
        print('************************', schema_column_formset)
        return schema_column_formset

