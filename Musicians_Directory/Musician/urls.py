from django.urls import path
from .views import musician_list

urlpatterns = [path("", musician_list, name="musician_list")]
