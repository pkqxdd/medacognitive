from django.db import models


class Patient(models.Model):
    first_name=models.CharField("First Name",max_length=30)
    last_name=models.CharField("Last Name",max_length=30)
    med_names = models.TextField("Current Medications")
    med_time = models.TextField("Time to take meds")
    med_left = models.TextField("How Much Left")
