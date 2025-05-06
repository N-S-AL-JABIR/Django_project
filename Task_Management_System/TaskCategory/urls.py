from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_category, name="task_category"),
]
