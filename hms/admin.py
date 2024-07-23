from django.contrib import admin
from .models import Hospital, Doctor, Patient, Schedule, Report, Appointment

admin.site.register(Hospital)
admin.site.register(Doctor)
admin.site.register(Schedule)
admin.site.register(Patient)
admin.site.register(Report)
admin.site.register(Appointment)


admin.site.site_header = "MEDISYNC"
admin.site.site_title = "Hospital Admin Portal"
admin.site.index_title = "MEDISYNC Hospital Administration"
