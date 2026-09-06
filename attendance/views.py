from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from django.db.models import Q

from .models import Attendance
from .forms import AttendanceForm


@login_required
def attendance_list(request):

    attendance_records = Attendance.objects.select_related(
        'student',
        'subject'
    ).all()

    search = request.GET.get(
        'search',
        ''
    )

    status = request.GET.get(
        'status',
        ''
    )

    if search:

        attendance_records = attendance_records.filter(

            Q(student__student_id__icontains=search) |

            Q(student__first_name__icontains=search) |

            Q(student__last_name__icontains=search) |

            Q(subject__subject_code__icontains=search) |

            Q(subject__subject_name__icontains=search)

        )

    if status:

        attendance_records = attendance_records.filter(
            status=status
        )

    context = {
        'attendance_records': attendance_records,
        'search': search,
        'selected_status': status,
    }

    return render(
        request,
        'attendance/attendance_list.html',
        context
    )


@login_required
def attendance_create(request):

    if request.method == 'POST':

        form = AttendanceForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'attendance_list'
            )

    else:

        form = AttendanceForm()

    return render(
        request,
        'attendance/attendance_form.html',
        {
            'form': form
        }
    )


@login_required
def attendance_update(request, pk):

    attendance = get_object_or_404(
        Attendance,
        pk=pk
    )

    if request.method == 'POST':

        form = AttendanceForm(
            request.POST,
            instance=attendance
        )

        if form.is_valid():

            form.save()

            return redirect(
                'attendance_list'
            )

    else:

        form = AttendanceForm(
            instance=attendance
        )

    return render(
        request,
        'attendance/attendance_form.html',
        {
            'form': form,
            'attendance': attendance
        }
    )


@login_required
def attendance_delete(request, pk):

    attendance = get_object_or_404(
        Attendance,
        pk=pk
    )

    if request.method == 'POST':

        attendance.delete()

        return redirect(
            'attendance_list'
        )

    return render(
        request,
        'attendance/attendance_confirm_delete.html',
        {
            'attendance': attendance
        }
    )
@login_required
def attendance_report(request, student_id):

    from students.models import Student

    student = get_object_or_404(
        Student,
        pk=student_id
    )

    attendance_records = Attendance.objects.filter(
        student=student
    ).select_related(
        'subject'
    )

    subjects = []

    subject_ids = attendance_records.values_list(
        'subject_id',
        flat=True
    ).distinct()

    for subject_id in subject_ids:

        subject_records = attendance_records.filter(
            subject_id=subject_id
        )

        total_classes = subject_records.count()

        present_classes = subject_records.filter(
            status='Present'
        ).count()

        absent_classes = subject_records.filter(
            status='Absent'
        ).count()

        if total_classes > 0:

            percentage = (
                present_classes / total_classes
            ) * 100

        else:

            percentage = 0

        subject = subject_records.first().subject

        subjects.append({
            'subject': subject,
            'total_classes': total_classes,
            'present_classes': present_classes,
            'absent_classes': absent_classes,
            'percentage': round(
                percentage,
                2
            ),
        })


    total_classes = attendance_records.count()

    present_classes = attendance_records.filter(
        status='Present'
    ).count()

    absent_classes = attendance_records.filter(
        status='Absent'
    ).count()


    if total_classes > 0:

        overall_percentage = (
            present_classes / total_classes
        ) * 100

    else:

        overall_percentage = 0


    context = {
        'student': student,
        'subjects': subjects,
        'total_classes': total_classes,
        'present_classes': present_classes,
        'absent_classes': absent_classes,
        'overall_percentage': round(
            overall_percentage,
            2
        ),
    }

    return render(
        request,
        'attendance/attendance_report.html',
        context
    )