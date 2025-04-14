from django.urls import path
from . import views
urlpatterns = [
    path("", views.home),
    path("about/", views.about),
    path("contact/", views.contact),
    path("template_filter/", views.template_filter),
]
