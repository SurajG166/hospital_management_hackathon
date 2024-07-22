from django.contrib import admin
from .models import Hospital, Doctor, Patient, Schedule, Report

admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Schedule)
admin.site.register(Patient)
admin.site.register(Report)
