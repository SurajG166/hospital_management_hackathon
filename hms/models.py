from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    qualification = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    hospitals = models.ManyToManyField(Hospital, through='Schedule')

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    condition = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctors = models.ManyToManyField(Doctor, through='Report')

    def __str__(self):
        return self.name

class Schedule(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    schedule = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.doctor.name} at {self.hospital.name} - {self.schedule}"

class Report(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescription = models.TextField()
    date = models.DateField()
    diagnosis = models.TextField()

    def __str__(self):
        return f"Report for {self.patient.name} by {self.doctor.name} on {self.date}"
