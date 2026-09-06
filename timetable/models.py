from django.db import models
from academics.models import Subject
from faculty.models import Faculty


class Timetable(models.Model):

    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ]

    day = models.CharField(
        max_length=10,
        choices=DAY_CHOICES
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='timetable_entries'
    )

    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        related_name='timetable_entries'
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    room_number = models.CharField(
        max_length=50
    )

    department = models.CharField(
        max_length=100
    )

    semester = models.CharField(
        max_length=20
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['day', 'start_time']

    def __str__(self):
        return f"{self.day} - {self.subject.subject_name}"