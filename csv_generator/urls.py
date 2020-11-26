from django.urls import include, path

from csv_generator.views import UserLoginView
from csv_generator.views.schemas_list_view import SchemasListView

urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('scheme_list/', SchemasListView.as_view, name='schemas_list')
]