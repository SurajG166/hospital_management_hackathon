from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Hospital, Doctor, Patient


def serve_home_page(request):
    return render(request, "home.html")


def serve_login_page(request):
    invalid_login_information = False
    return render(
        request, "login.html", {"invalid_login_information": invalid_login_information}
    )


def validate_login(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        login_type = request.POST.get("type")
        debug_string = login_type + "  haha"
        if login_type == "Patient":
            try:
                patient = Patient.objects.get(username=username, password=password)
                return redirect("patient_home", patient_id=patient.id)
            except Patient.DoesNotExist:
                messages.error(request, "Invalid login info: try again!")
                return render(request, "login.html")

        elif login_type == "Doctor":
            try:
                doctor = Doctor.objects.get(username=username, password=password)
                return redirect("doctor_home", doctor_id=doctor.id)
            except Doctor.DoesNotExist:
                messages.error(request, "Invalid login info: try again!")
                return render(request, "home.html")

        elif login_type == "Hospital":
            try:
                hospital = Hospital.objects.get(username=username, password=password)
                return redirect("hospital_home", hospital_id=hospital.id)
            except Hospital.DoesNotExist:
                messages.error(request, "Invalid login info: try again!")
                return render(request, "login.html")

        else:
            messages.error(request, "Invalid login type selected.")
            return render(request, "login.html", {"debug_string" : debug_string})


def patient_home(request, patient_id ):
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, "patient.html", {"patient": patient})


def doctor_home(request, doctor_id = 1):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, "doctor.html", {"doctor": doctor})


def hospital_home(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    return render(request, "hospital_admin.html", {"hospital": hospital})
