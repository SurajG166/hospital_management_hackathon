from django.urls import path
from . import views

urlpatterns = [
    path('', views.serve_home_page),
    path('login/',views.serve_login_page, name = 'login_page')
]