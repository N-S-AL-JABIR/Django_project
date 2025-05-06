from django.urls import path
from . import views

urlpatterns = [
    path("/", views.task, name="add_task"),
    path("view_task/", views.view_task, name="view_task"),
    path("edit_task/<int:id>", views.edit_task, name="edit_task"),
    path("delete_task/<int:id>", views.delete_task, name="delete_task"),
]
