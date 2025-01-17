from django.db import models
from .models import Doctor
from ..accounts.models import Account


class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=200)
    working_hours = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='doctor_avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} ({self.specialty})"

    from django.db import models

    class Appointment(models.Model):
        user = models.ForeignKey(Account, on_delete=models.CASCADE)
        doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
        datetime = models.DateTimeField()
        STATUS_CHOICES = (
            ('active', 'Active'),
            ('past', 'Past')
        )
        status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

        def __str__(self):
            return f"Appointment for {self.user.first_name} with Dr. {self.doctor.full_name}"