from django.urls import path

from . import views


app_name = "students"

urlpatterns = [
     path('', views.homeView, name='index'),
     path('all/student/', views.all_student_display, name='all_display'),
     path('visitor/', views.notAuthenticUser, name='visitor'),
     path('add/', views.addStudent, name='addStudent'),
     path('student:detail:id:<int:pk>/', views.detailsView, name='detail'),
     path("deleting/student:id:<int:pk>/", views.deleteStudent, name='deleteStudent'),
     path('updating/student/id:<int:pk>/', views.editStudent, name='editStudent'),
]
