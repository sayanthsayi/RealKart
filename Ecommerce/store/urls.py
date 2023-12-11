from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name="home"),
    path('brands/<str:slug>',views.Brands,name="brands"),
    path('productview/<str:slug>',views.ProductView,name="productview"),
]