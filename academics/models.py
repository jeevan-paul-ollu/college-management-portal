from django.db import models


class Subject(models.Model):

    SEMESTER_CHOICES = [
        ('1', 'Semester 1'),
        ('2', 'Semester 2'),
        ('3', 'Semester 3'),
        ('4', 'Semester 4'),
        ('5', 'Semester 5'),
        ('6', 'Semester 6'),
        ('7', 'Semester 7'),
        ('8', 'Semester 8'),
    ]

    subject_code = models.CharField(
        max_length=20,
        unique=True
    )

    subject_name = models.CharField(
        max_length=150
    )

    department = models.CharField(
        max_length=100
    )

    course = models.CharField(
        max_length=100
    )

    semester = models.CharField(
        max_length=1,
        choices=SEMESTER_CHOICES
    )

    credits = models.IntegerField()

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.subject_code} - {self.subject_name}"