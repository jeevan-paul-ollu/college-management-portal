from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.academics_home,
        name='academics_home'
    ),

    path(
        'add/',
        views.subject_create,
        name='subject_create'
    ),

    path(
        '<int:pk>/',
        views.subject_detail,
        name='subject_detail'
    ),

    path(
        '<int:pk>/edit/',
        views.subject_update,
        name='subject_update'
    ),

    path(
        '<int:pk>/delete/',
        views.subject_delete,
        name='subject_delete'
    ),

]