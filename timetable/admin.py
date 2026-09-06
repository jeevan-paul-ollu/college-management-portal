from django.contrib import admin
from .models import Timetable


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):

    list_display = (
        'day',
        'subject',
        'faculty',
        'start_time',
        'end_time',
        'room_number',
        'department',
        'semester',
    )

    search_fields = (
        'subject__subject_name',
        'subject__subject_code',
        'faculty__first_name',
        'faculty__last_name',
        'room_number',
        'department',
    )

    list_filter = (
        'day',
        'department',
        'semester',
    )