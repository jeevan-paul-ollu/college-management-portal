from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Result
from .forms import ResultForm


@login_required
def result_list(request):

    results = Result.objects.select_related(
        'student',
        'subject'
    ).all()

    search = request.GET.get(
        'search',
        ''
    )

    grade = request.GET.get(
        'grade',
        ''
    )

    result_status = request.GET.get(
        'result',
        ''
    )

    if search:

        results = results.filter(
            Q(
                student__student_id__icontains=search
            )
            |
            Q(
                student__first_name__icontains=search
            )
            |
            Q(
                student__last_name__icontains=search
            )
            |
            Q(
                subject__subject_code__icontains=search
            )
            |
            Q(
                subject__subject_name__icontains=search
            )
        )

    if grade:

        results = results.filter(
            grade=grade
        )

    if result_status:

        results = results.filter(
            result=result_status
        )

    context = {
        'results': results,
        'search': search,
        'selected_grade': grade,
        'selected_result': result_status,
    }

    return render(
        request,
        'results/result_list.html',
        context
    )


@login_required
def result_create(request):

    if request.method == 'POST':

        form = ResultForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(
                'result_list'
            )

    else:

        form = ResultForm()

    return render(
        request,
        'results/result_form.html',
        {
            'form': form
        }
    )


@login_required
def result_detail(request, pk):

    result = get_object_or_404(
        Result,
        pk=pk
    )

    return render(
        request,
        'results/result_detail.html',
        {
            'result': result
        }
    )


@login_required
def result_update(request, pk):

    result = get_object_or_404(
        Result,
        pk=pk
    )

    if request.method == 'POST':

        form = ResultForm(
            request.POST,
            instance=result
        )

        if form.is_valid():

            form.save()

            return redirect(
                'result_list'
            )

    else:

        form = ResultForm(
            instance=result
        )

    return render(
        request,
        'results/result_form.html',
        {
            'form': form,
            'result': result
        }
    )


@login_required
def result_delete(request, pk):

    result = get_object_or_404(
        Result,
        pk=pk
    )

    if request.method == 'POST':

        result.delete()

        return redirect(
            'result_list'
        )

    return render(
        request,
        'results/result_confirm_delete.html',
        {
            'result': result
        }
    )