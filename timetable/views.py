from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Timetable
from .forms import TimetableForm


@login_required
def timetable_list(request):

    timetable = Timetable.objects.select_related(
        'subject',
        'faculty'
    ).all()

    day = request.GET.get('day', '')
    department = request.GET.get('department', '')
    search = request.GET.get('search', '')

    if day:
        timetable = timetable.filter(day=day)

    if department:
        timetable = timetable.filter(
            department__icontains=department
        )

    if search:
        timetable = timetable.filter(
            Q(subject__subject_name__icontains=search)
            |
            Q(subject__subject_code__icontains=search)
            |
            Q(faculty__first_name__icontains=search)
            |
            Q(faculty__last_name__icontains=search)
            |
            Q(room_number__icontains=search)
        )

    context = {
        'timetable': timetable,
        'selected_day': day,
        'department': department,
        'search': search,
    }

    return render(
        request,
        'timetable/timetable_list.html',
        context
    )


@login_required
def timetable_create(request):

    if request.method == 'POST':

        form = TimetableForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('timetable_list')

    else:

        form = TimetableForm()

    return render(
        request,
        'timetable/timetable_form.html',
        {'form': form}
    )


@login_required
def timetable_detail(request, pk):

    timetable = get_object_or_404(
        Timetable,
        pk=pk
    )

    return render(
        request,
        'timetable/timetable_detail.html',
        {'timetable': timetable}
    )


@login_required
def timetable_update(request, pk):

    timetable = get_object_or_404(
        Timetable,
        pk=pk
    )

    if request.method == 'POST':

        form = TimetableForm(
            request.POST,
            instance=timetable
        )

        if form.is_valid():

            form.save()

            return redirect('timetable_list')

    else:

        form = TimetableForm(
            instance=timetable
        )

    return render(
        request,
        'timetable/timetable_form.html',
        {
            'form': form,
            'timetable': timetable
        }
    )


@login_required
def timetable_delete(request, pk):

    timetable = get_object_or_404(
        Timetable,
        pk=pk
    )

    if request.method == 'POST':

        timetable.delete()

        return redirect('timetable_list')

    return render(
        request,
        'timetable/timetable_confirm_delete.html',
        {'timetable': timetable}
    )