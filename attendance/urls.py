from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.attendance_list,
        name='attendance_list'
    ),

    path(
        'add/',
        views.attendance_create,
        name='attendance_create'
    ),

    path(
        '<int:pk>/edit/',
        views.attendance_update,
        name='attendance_update'
    ),

    path(
    'report/<int:student_id>/',
    views.attendance_report,
    name='attendance_report'
),

    path(
        '<int:pk>/delete/',
        views.attendance_delete,
        name='attendance_delete'
    ),

]