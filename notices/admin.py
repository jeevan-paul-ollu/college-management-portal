from django.contrib import admin
from .models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'notice_date',
        'is_active',
        'created_at',
    )

    search_fields = (
        'title',
        'description',
    )

    list_filter = (
        'category',
        'is_active',
        'notice_date',
    )