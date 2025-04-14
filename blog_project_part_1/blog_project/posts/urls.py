from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.add_posts, name="add_posts"),
    path("edit/<int:id>/", views.edit_post, name="edit_post"),
    path("delete/<int:id>/", views.delete_post, name="delete_post"),
]
