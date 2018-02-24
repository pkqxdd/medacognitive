from django.db import models

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField("First Name", max_length=30)
    last_name = models.CharField("Last Name", max_length=30)
    patient_list = models.TextField("List of Patients")
