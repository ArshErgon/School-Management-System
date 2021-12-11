from django.urls import path

from . import views


urlpatterns = [
     path('', views.homeView, name='index'),
     path('visitor/', views.notAuthenticUser, name='visitor'),
     path('add/', views.addStudent, name='addStudent'),
     path('detail/<int:pk>/', views.detailsView, name='detail'),
]
