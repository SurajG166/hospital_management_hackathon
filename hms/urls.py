from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.serve_home_page)
]