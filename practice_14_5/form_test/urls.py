from django.urls import path
from . import views

urlpatterns = [
    path("", views.form_test, name="form_test"),
]
