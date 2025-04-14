from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('students/', views.students, name='students'),
   path('delete_student/<int:roll_no>/', views.delete_student, name='delete_student'),
]
