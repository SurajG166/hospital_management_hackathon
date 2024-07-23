from django import forms
from .models import Report,Appointment


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["doctor", "patient", "diagnosis", "date", "prescription"]


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["doctor", "patient", "hospital", "date", "symptoms", "emergency"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "symptoms": forms.TextInput(attrs={"class": "form-control"}),
            "emergency": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
