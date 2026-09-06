from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Student
from .forms import StudentForm

@login_required
def student_list(request):

    students = Student.objects.all().order_by('student_id')

    search = request.GET.get('search', '')
    department = request.GET.get('department', '')
    course = request.GET.get('course', '')
    year = request.GET.get('year', '')

    if search:
        students = students.filter(
            Q(student_id__icontains=search) |
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(email__icontains=search)
        )

    if department:
        students = students.filter(
            department=department
        )

    if course:
        students = students.filter(
            course=course
        )

    if year:
        students = students.filter(
            year=year
        )

    departments = Student.objects.values_list(
        'department',
        flat=True
    ).distinct().order_by('department')

    courses = Student.objects.values_list(
        'course',
        flat=True
    ).distinct().order_by('course')

    years = Student.objects.values_list(
        'year',
        flat=True
    ).distinct().order_by('year')

    context = {
        'students': students,
        'departments': departments,
        'courses': courses,
        'years': years,
        'search': search,
        'selected_department': department,
        'selected_course': course,
        'selected_year': year,
    }

    return render(
        request,
        'students/student_list.html',
        context
    )

@login_required
@login_required
def student_create(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:

        form = StudentForm()

    return render(
        request,
        'students/student_form.html',
        {
            'form': form
        }
    )

@login_required
def student_detail(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )

    return render(
        request,
        'students/student_detail.html',
        {'student': student}
    )

@login_required
def student_update(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:

        form = StudentForm(instance=student)

    return render(
        request,
        'students/student_form.html',
        {
            'form': form,
            'student': student
        }
    )

@login_required
def student_delete(request, pk):

    student = get_object_or_404(
        Student,
        pk=pk
    )

    if request.method == 'POST':

        student.delete()
        return redirect('student_list')

    return render(
        request,
        'students/student_confirm_delete.html',
        {'student': student}
    )