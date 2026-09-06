from django.db import models


class Notice(models.Model):

    CATEGORY_CHOICES = [
        ('General', 'General'),
        ('Academic', 'Academic'),
        ('Exam', 'Exam'),
        ('Event', 'Event'),
        ('Placement', 'Placement'),
        ('Holiday', 'Holiday'),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField()

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='General'
    )

    notice_date = models.DateField()

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-notice_date', '-created_at']

    def __str__(self):
        return self.title