from django.db import models
from django.core.validators import MinValueValidator

from students.models import Student


class Fee(models.Model):

    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Partial', 'Partial'),
        ('Pending', 'Pending'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='fees'
    )

    academic_year = models.CharField(
        max_length=20
    )

    total_fees = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0)
        ]
    )

    paid_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0)
        ]
    )

    pending_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    payment_status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS_CHOICES,
        default='Pending'
    )

    payment_date = models.DateField(
        null=True,
        blank=True
    )

    remarks = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = [
            '-created_at'
        ]

    def save(self, *args, **kwargs):

        if self.paid_amount > self.total_fees:
            self.paid_amount = self.total_fees

        self.pending_amount = (
            self.total_fees - self.paid_amount
        )

        if self.paid_amount >= self.total_fees:

            self.payment_status = 'Paid'

        elif self.paid_amount > 0:

            self.payment_status = 'Partial'

        else:

            self.payment_status = 'Pending'

        super().save(*args, **kwargs)

    def __str__(self):

        return (
            f"{self.student.student_id} - "
            f"{self.academic_year}"
        )