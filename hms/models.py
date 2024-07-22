from django.db import models

# Create your models here.
class Hospital(models.Model):
    id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    loc=models.CharField(max_length=200)

    # def _str_(self):
    #     return self.name

class Doctor(models.Model):
    id=models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    age=models.IntegerField()
    qualification = models.CharField(max_length=10)
    contact=models.IntegerField()
    

    # def _str_(self):
    #     return self.title
    
class patient(models.Model):
    id=models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    age=models.IntegerField()
    condition= models.CharField(max_length=10)
    contact=models.IntegerField()
    address=models.CharField(max_length=200)
    