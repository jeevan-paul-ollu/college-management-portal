from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from students.models import Student
from faculty.models import Faculty
from academics.models import Subject
from attendance.models import Attendance
from results.models import Result
from fees.models import Fee
from notices.models import Notice
from timetable.models import Timetable


@login_required
def dashboard(request):

    total_students = Student.objects.count()

    total_faculty = Faculty.objects.count()

    total_subjects = Subject.objects.count()

    total_attendance = Attendance.objects.count()

    total_results = Result.objects.count()

    total_fees = Fee.objects.count()

    total_notices = Notice.objects.count()

    total_timetable = Timetable.objects.count()


    recent_students = Student.objects.all().order_by(
        '-created_at'
    )[:5]


    recent_faculty = Faculty.objects.all().order_by(
        '-created_at'
    )[:5]


    recent_notices = Notice.objects.all().order_by(
        '-notice_date'
    )[:5]


    paid_fees = Fee.objects.filter(
        payment_status='Paid'
    ).count()


    partial_fees = Fee.objects.filter(
        payment_status='Partial'
    ).count()


    pending_fees = Fee.objects.filter(
        payment_status='Pending'
    ).count()


    context = {

        'total_students': total_students,

        'total_faculty': total_faculty,

        'total_subjects': total_subjects,

        'total_attendance': total_attendance,

        'total_results': total_results,

        'total_fees': total_fees,

        'total_notices': total_notices,

        'total_timetable': total_timetable,

        'recent_students': recent_students,

        'recent_faculty': recent_faculty,

        'recent_notices': recent_notices,

        'paid_fees': paid_fees,

        'partial_fees': partial_fees,

        'pending_fees': pending_fees,
    }


    return render(
        request,
        'dashboard.html',
        context
    )