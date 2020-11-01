from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'site-home'),
    path('addStudent/', views.addStudent, name = 'site-addStudent'),
    path('viewStudent/', views.viewStudent, name = 'site-viewStudent'),
]
