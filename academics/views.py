from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Subject
from .forms import SubjectForm


@login_required
def academics_home(request):

    subjects = Subject.objects.all().order_by(
        'subject_code'
    )

    search = request.GET.get(
        'search',
        ''
    )

    department = request.GET.get(
        'department',
        ''
    )

    semester = request.GET.get(
        'semester',
        ''
    )

    if search:

        subjects = subjects.filter(
            Q(subject_code__icontains=search) |
            Q(subject_name__icontains=search) |
            Q(course__icontains=search)
        )

    if department:

        subjects = subjects.filter(
            department=department
        )

    if semester:

        subjects = subjects.filter(
            semester=semester
        )

    departments = Subject.objects.values_list(
        'department',
        flat=True
    ).distinct().order_by(
        'department'
    )

    context = {
        'subjects': subjects,
        'departments': departments,
        'search': search,
        'selected_department': department,
        'selected_semester': semester,
    }

    return render(
        request,
        'academics/academics_home.html',
        context
    )


@login_required
def subject_create(request):

    if request.method == 'POST':

        form = SubjectForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                'academics_home'
            )

    else:

        form = SubjectForm()

    return render(
        request,
        'academics/subject_form.html',
        {
            'form': form
        }
    )


@login_required
def subject_detail(request, pk):

    subject = get_object_or_404(
        Subject,
        pk=pk
    )

    return render(
        request,
        'academics/subject_detail.html',
        {
            'subject': subject
        }
    )


@login_required
def subject_update(request, pk):

    subject = get_object_or_404(
        Subject,
        pk=pk
    )

    if request.method == 'POST':

        form = SubjectForm(
            request.POST,
            instance=subject
        )

        if form.is_valid():

            form.save()

            return redirect(
                'academics_home'
            )

    else:

        form = SubjectForm(
            instance=subject
        )

    return render(
        request,
        'academics/subject_form.html',
        {
            'form': form,
            'subject': subject
        }
    )


@login_required
def subject_delete(request, pk):

    subject = get_object_or_404(
        Subject,
        pk=pk
    )

    if request.method == 'POST':

        subject.delete()

        return redirect(
            'academics_home'
        )

    return render(
        request,
        'academics/subject_confirm_delete.html',
        {
            'subject': subject
        }
    )