from django.db import models


class Faculty(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    faculty_id = models.CharField(
        max_length=20,
        unique=True
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=15
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    department = models.CharField(
        max_length=100
    )

    designation = models.CharField(
        max_length=100
    )

    qualification = models.CharField(
        max_length=200
    )

    joining_date = models.DateField()

    address = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.faculty_id} - {self.first_name} {self.last_name}"