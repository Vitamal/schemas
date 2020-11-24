from django.urls import include, path

from csv_generator.views import UserLoginView

urlpatterns = [
    path('login/', UserLoginView.as_view()),
]