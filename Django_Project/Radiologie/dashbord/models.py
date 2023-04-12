from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
Service_choises = (
    ("Control de rutina", "Control de rutina"),
    ("Radiografie", "Radiografie"),
    ("Detartraj", "Detartraj"),
    ("Tratament laser", "Tratament laser"),
    )

Time_choises = (
    ("8:00", "8:00"),
    ("9:00", "9:00"),
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
)

"""varianta 1"""
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now, blank=True)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=Service_choises, default="Control de rutina")
    created_at = models.DateTimeField(default=datetime.now, blank=True)


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)   # many to many
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)  # many to many
    confirmed = models.BooleanField(default=False)
    start = models.CharField(max_length=50, choices=Time_choises)
    date = models.DateField('Appointment_date', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

"""  varianta 2"""

