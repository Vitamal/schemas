from django.contrib import messages
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from django.views.generic.edit import ModelFormMixin, UpdateView

from csv_generator.forms import SchemaColumnForm, SchemaForm
from csv_generator.models import Schema, SchemaColumn
from csv_generator.views.access_mixin import SchemasAccessMixin


# class SchemaCreateUpdateMixin(SchemasAccessMixin, ModelFormMixin):
#     model = Schema
#     template_name = 'schemas/formset.html'
#     context_object_name = 'schema'
#     object = None
#
#     def get_success_url(self):
#         return reverse('schemas_list')
#
#     def form_valid(self, form):
#         self.object = form.save()
#
#         if not self.object.created_by:
#             self.object.created_by = getattr(self, 'request').user
#         self.object.changed_by = getattr(self, 'request').user
#         self.object.user = getattr(self, 'request').user
#
#         schema_column = form.cleaned_data
#         for name in Schema._meta.get_fields():
#             if name.name in schema_column:
#                 print('remove the: ', name.name)
#                 schema_column.pop(name.name)
#         self.object.schema_column = schema_column
#         return super().form_valid(form)


class SchemaCreateView(CreateView):
    model = Schema
    template_name = 'schemas/schemas_create_update.html'
    context_object_name = 'schema'
    object = None
    form_class = SchemaForm
    SchemaColumnInlineFormset = inlineformset_factory(Schema, SchemaColumn, form=SchemaColumnForm, extra=1)
    formset = SchemaColumnInlineFormset

    def get_success_url(self):
        return reverse('schemas_list')

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        schema_column_formset = self.formset()

        return self.render_to_response(
            self.get_context_data(form=form, schema_column_formset=schema_column_formset)
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        schema_column_formset = self.formset(self.request.POST)

        if (form.is_valid() and schema_column_formset.is_valid()):
            return self.form_valid(form, schema_column_formset)
        print('==============================', schema_column_formset.is_valid(), form.is_valid())
        print(messages.error(request, "Error"))
        return self.form_invalid(form, schema_column_formset)

    def form_valid(self, form, schema_column_formset):
        """
        Called if all forms are valid. Creates a Schema instance along
        with associated schema_column and then redirects to a success page.
        """
        self.object = form.save()
        schema_column_formset.instance = self.object
        schema_column_formset.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, schema_column_formset):
        """
        Called if whether a form is invalid. Re-renders the context
        data with the data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form, schema_column_formset=schema_column_formset)
        )

    def get_context_data(self, **kwargs):
        """ Add formset to the context_data. """
        context = super(SchemaCreateView, self).get_context_data(**kwargs)

        if self.request.POST:
            context['form'] = self.form_class(self.request.POST)
            context['schema_column_formset'] = self.formset(self.request.POST)
        else:
            context['form'] = self.form_class()
            context['schema_column_formset'] = self.formset()

        return context


class SchemaUpdateView(UpdateView):
    pk_url_kwarg = 'schema_id'
    form_class = SchemaForm
