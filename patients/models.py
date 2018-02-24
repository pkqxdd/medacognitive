from django.db import models


class Patient(models.Model):
    first_name=models.CharField("First Name",max_length=30)
    last_name=models.CharField("Last Name",max_length=30)
    med = models.TextField("Medicine")


class Survey(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    med_name = models.TextField("Med name")
    med_comment = models.TextField("Comment")
