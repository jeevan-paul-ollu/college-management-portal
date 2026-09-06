from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from .import views
urlpatterns = [

    path(
    'dashboard/',
    views.dashboard,
    name='dashboard'
),
    path(
    'attendance/',
    include('attendance.urls')
),
path(
    'results/',
    include('results.urls')
),
    path(
        'login/',
        auth_views.LoginView.as_view(
        template_name='registration/login.html'
        ),
        name='login'
    ),
    path(
    'logout/',
    auth_views.LogoutView.as_view(),
    name='logout'
),

    path(
        'admin/',
        admin.site.urls
    ),

    path(
        '',
        TemplateView.as_view(
            template_name='home.html'
        ),
        name='home'
    ),

    path(
        'students/',
        include('students.urls')
    ),

    path(
        'faculty/',
        include('faculty.urls')
    ),

    path(
        'academics/',
        include('academics.urls')
    ),

    path(
        'fees/',
        include('fees.urls')
    ),

    path(
        'notices/',
        include('notices.urls')
    ),
    path(
    'timetable/',
    include('timetable.urls')
),
]