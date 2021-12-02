from django.urls import path

from . import views


urlpatterns = [
     path("new-user/", views.SignUp, name='new_sign'),
     path("user/", views.SignIn, name='login'),
]
