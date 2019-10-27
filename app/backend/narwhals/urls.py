# todos/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('doctorList', views.DoctorList.as_view()),
    path('doctorDetails/<int:pk>/', views.DoctorDetails.as_view()),
]