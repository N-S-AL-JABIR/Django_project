from django.urls import path
from . import views

urlpatterns = [
    path("", views.album_list, name="album_list"),
    path("edit_album/<int:id>/", views.edit_album, name="edit_album"),
    path("edit_musician/<int:id>/", views.edit_musician, name="edit_musician"),
    path("delete/<int:id>/", views.delete_Musician, name="delete_Musician"),
]
