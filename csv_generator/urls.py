from django.urls import include, path

from csv_generator.views import UserLoginView, SchemasListView, SchemaCreateView, SchemaDeleteView, \
    SchemasLogoutView, SchemaUpdateView, SchemasToGenerateView, process_generate, data_view, download

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='schemas_login'),
    path('', SchemasListView.as_view(), name='schemas_list'),
    path('create/', SchemaCreateView.as_view(), name='schemas_create'),
    path('edit/<int:schema_id>', SchemaUpdateView.as_view(), name='schemas_edit'),
    path('delete/<int:schema_id>', SchemaDeleteView.as_view(), name='schemas_delete'),
    path('logout/', SchemasLogoutView.as_view(), name='logout'),
    path('generator/<int:schema_id>', SchemasToGenerateView.as_view(), name='schema_to_generate'),
    path('process_generate/', process_generate, name='process_generate'),
    path('scv_data/<int:generated_scheme_id>', data_view, name='data_view'),
    path('scv_data/download/<path:path>', download, name='download'),
]
