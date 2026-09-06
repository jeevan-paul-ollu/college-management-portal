from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Faculty
from .forms import FacultyForm



@login_required
def faculty_list(request):

    faculty_members = Faculty.objects.all().order_by(
        'faculty_id'
    )

    search = request.GET.get('search', '')
    department = request.GET.get('department', '')
    designation = request.GET.get('designation', '')

    if search:

        faculty_members = faculty_members.filter(

            Q(faculty_id__icontains=search) |
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(email__icontains=search)

        )

    if department:

        faculty_members = faculty_members.filter(
            department=department
        )

    if designation:

        faculty_members = faculty_members.filter(
            designation=designation
        )

    departments = Faculty.objects.values_list(
        'department',
        flat=True
    ).distinct().order_by('department')

    designations = Faculty.objects.values_list(
        'designation',
        flat=True
    ).distinct().order_by('designation')

    context = {

        'faculty_members': faculty_members,

        'departments': departments,

        'designations': designations,

        'search': search,

        'selected_department': department,

        'selected_designation': designation,

    }

    return render(
        request,
        'faculty/faculty_list.html',
        context
    )
@login_required
def faculty_create(request):

    if request.method == 'POST':

        form = FacultyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('faculty_list')

    else:

        form = FacultyForm()

    return render(
        request,
        'faculty/faculty_form.html',
        {'form': form}
    )


@login_required
def faculty_detail(request, pk):

    faculty = get_object_or_404(
        Faculty,
        pk=pk
    )

    return render(
        request,
        'faculty/faculty_detail.html',
        {'faculty': faculty}
    )


@login_required
def faculty_update(request, pk):

    faculty = get_object_or_404(
        Faculty,
        pk=pk
    )

    if request.method == 'POST':

        form = FacultyForm(
            request.POST,
            instance=faculty
        )

        if form.is_valid():
            form.save()
            return redirect('faculty_list')

    else:

        form = FacultyForm(
            instance=faculty
        )

    return render(
        request,
        'faculty/faculty_form.html',
        {
            'form': form,
            'faculty': faculty
        }
    )


@login_required
def faculty_delete(request, pk):

    faculty = get_object_or_404(
        Faculty,
        pk=pk
    )

    if request.method == 'POST':

        faculty.delete()
        return redirect('faculty_list')

    return render(
        request,
        'faculty/faculty_confirm_delete.html',
        {'faculty': faculty}
    )