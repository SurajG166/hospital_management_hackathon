from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("home/", views.serve_home_page),
    path("login/", views.serve_login_page, name="login_page"),
    path("validate_login/", views.validate_login, name="validate_login"),
    path("patient_home/", views.patient_home, name="patient_home"),
    path("doctor_home/", views.doctor_home, name="doctor_home"),
    path("hospital_home/", views.hospital_home, name="hospital_home"),
    path(
        "prescription_form/",
        views.serve_prescription_form,
        name="serve_prescription_form",
    ),
]
