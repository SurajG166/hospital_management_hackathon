from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Hospital, Doctor, Patient, Schedule, Report, Appointment
from .forms import ReportForm,AppointmentForm


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
                return render(request, "login.html")

        elif login_type == "Hospital":
            try:
                hospital = Hospital.objects.get(username=username, password=password)
                return redirect("/admin/")
            except Hospital.DoesNotExist:
                messages.error(request, "Invalid login info: try again!")
                return render(request, "login.html")

        else:
            messages.error(request, "Invalid login type selected.")
            return render(request, "login.html")


def patient_home(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    reports = Report.objects.filter(patient=patient)
    return render(request, "patient.html", {"patient": patient, "reports": reports})


def doctor_home(request, doctor_id=1):
    reports = None
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == "POST":
        patient_id = request.POST.get("patient_id")
        if patient_id:
            selected_patient = get_object_or_404(Patient, id=patient_id)
            reports = Report.objects.filter(doctor=doctor, patient=selected_patient)
    doctor = get_object_or_404(Doctor, id=doctor_id)
    schedules = Schedule.objects.filter(doctor=doctor)
    patients = Patient.objects.all()
    return render(
        request,
        "doctor.html",
        {
            "doctor": doctor,
            "schedules": schedules,
            "patients": patients,
            "reports": reports,
        },
    )


def hospital_home(request, hospital_id):
    hospital = get_object_or_404(Hospital, id=hospital_id)
    return render(request, "hospital_admin.html", {"hospital": hospital})


def serve_prescription_form(request, doctor_id):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("doctor_home", doctor_id=doctor_id)
    else:
        form = ReportForm()
    patients = Patient.objects.all()
    return render(
        request,
        "prescription_form.html",
        {"patients": patients, "form": form, "doctor_id": doctor_id},
    )


def report_view(request, report_id):
    report = Report.objects.get(id=report_id)
    return render(request, "report.html", {"report": report})


def create_appointment(request, patient_id):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("patient_home", patient_id = patient_id)  
    else:
        form = AppointmentForm()

    return render(request, "new_appointment.html", {"form": form})
