from django.urls import path
from . import views
urlpatterns = [path("get-users", views.UserDetailsAPI.as_view()),
               path("register", views.RegisterUser.as_view()),
               path("login", views.LoginUser.as_view())

               ]