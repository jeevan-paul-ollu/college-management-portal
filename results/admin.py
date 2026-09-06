from django.contrib import admin

from .models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):

    list_display = (
        'student',
        'subject',
        'internal_marks',
        'assignment_marks',
        'mid_marks',
        'semester_marks',
        'total',
        'grade',
        'result',
    )

    search_fields = (
        'student__student_id',
        'student__first_name',
        'student__last_name',
        'subject__subject_code',
        'subject__subject_name',
    )

    list_filter = (
        'grade',
        'result',
    )