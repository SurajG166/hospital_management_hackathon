from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.serve_home_page),
    path("login/", views.serve_login_page, name="login_page"),
    path("validate_login/", views.validate_login, name="validate_login"),
    path("patient_home/<int:patient_id>/", views.patient_home, name="patient_home"),
    path("doctor_home/<int:doctor_id>/", views.doctor_home, name="doctor_home"),
    path("hospital_home/<int:hospital_id>/", views.hospital_home, name="hospital_home"),
    path(
        "prescription_form/<int:doctor_id>/",
        views.serve_prescription_form,
        name="serve_prescription_form",
    ),
    path("report/<int:report_id>", views.report_view, name="report_view"),
    path(
        "new_appointment/<int:patient_id>",
        views.create_appointment,
        name="new_appointment",
    ),
    # path("admin/", admin.site.urls, name="admin")
]
