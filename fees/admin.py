from django.contrib import admin

from .models import Fee


@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):

    list_display = (
        'student',
        'academic_year',
        'total_fees',
        'paid_amount',
        'pending_amount',
        'payment_status',
        'payment_date',
    )

    search_fields = (
        'student__student_id',
        'student__first_name',
        'student__last_name',
        'academic_year',
    )

    list_filter = (
        'payment_status',
        'academic_year',
    )