from django.db import models
from students.models import Student
from academics.models import Subject


class Attendance(models.Model):

    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )

    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = (
            'student',
            'subject',
            'date',
        )

        ordering = [
            '-date'
        ]

    def __str__(self):
        return (
            f"{self.student.student_id} - "
            f"{self.subject.subject_code} - "
            f"{self.date}"
        )