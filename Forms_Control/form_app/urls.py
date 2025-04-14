from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("form-app/", views.form, name="form-app"),
    path("about/", views.about, name="about"),
    path("django_form/", views.django_form, name="django_form"),
    path("student_form/", views.student_form, name="student_form"),
]
