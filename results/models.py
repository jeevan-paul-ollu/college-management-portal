from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from students.models import Student
from academics.models import Subject


class Result(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='results'
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='results'
    )

    internal_marks = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(20)
        ]
    )

    assignment_marks = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    )

    mid_marks = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(20)
        ]
    )

    semester_marks = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(50)
        ]
    )

    total = models.FloatField(
        default=0
    )

    percentage = models.FloatField(
        default=0
    )

    grade = models.CharField(
        max_length=5,
        default='F'
    )

    result = models.CharField(
        max_length=10,
        default='Fail'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = (
            'student',
            'subject',
        )

        ordering = [
            '-created_at'
        ]

    def save(self, *args, **kwargs):

        self.total = (
            self.internal_marks +
            self.assignment_marks +
            self.mid_marks +
            self.semester_marks
        )

        self.percentage = self.total

        if self.total >= 90:
            self.grade = 'A+'
        elif self.total >= 80:
            self.grade = 'A'
        elif self.total >= 70:
            self.grade = 'B'
        elif self.total >= 60:
            self.grade = 'C'
        elif self.total >= 50:
            self.grade = 'D'
        else:
            self.grade = 'F'

        if self.total >= 40:
            self.result = 'Pass'
        else:
            self.result = 'Fail'

        super().save(*args, **kwargs)

    def __str__(self):

        return (
            f"{self.student.student_id} - "
            f"{self.subject.subject_code}"
        )