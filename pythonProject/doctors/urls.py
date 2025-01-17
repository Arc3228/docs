from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list_view, name='doctor-list'),
    path('add/', views.add_doctor_view, name='add-doctor'),
    path('<int:pk>/book/', views),]