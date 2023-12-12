from django.urls import path
from . import views

urlpatterns = [
    path('Signup/',views.Signup,name="signup"),
    path('Login/',views.Login,name="login"),
    path('Logout/',views.logoutpage,name="logout"),


]