from django.urls import include, path

from csv_generator.views import UserLoginView, SchemasListView, SchemaCreateView, SchemaUpdateView

urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('schemas/', SchemasListView.as_view(), name='schemas_list'),
    path('schemas/create', SchemaCreateView.as_view(), name='schemas_create'),
    path('schemas/edit/<int:schema_id>', SchemaUpdateView.as_view(), name='schemas_edit'),
]