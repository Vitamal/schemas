from django.urls import include, path

from csv_generator.views import UserLoginView, SchemasListView, SchemaCreateView, SchemaUpdateView, SchemaDeleteView, \
    SchemasLogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='schemas_login'),
    path('schemas/', SchemasListView.as_view(), name='schemas_list'),
    path('schemas/create', SchemaCreateView.as_view(), name='schemas_create'),
    path('schemas/edit/<int:schema_id>', SchemaUpdateView.as_view(), name='schemas_edit'),
    path('schemas/delete/<int:schema_id>', SchemaDeleteView.as_view(), name='schemas_delete'),
    path('schemas/logout/', SchemasLogoutView.as_view(), name='logout'),
]