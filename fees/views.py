from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Fee
from .forms import FeeForm


@login_required
def fee_list(request):

    fees = Fee.objects.select_related(
        'student'
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

        fees = fees.filter(
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
                academic_year__icontains=search
            )
        )

    if status:

        fees = fees.filter(
            payment_status=status
        )

    context = {
        'fees': fees,
        'search': search,
        'selected_status': status,
    }

    return render(
        request,
        'fees/fees.html',
        context
    )


@login_required
def fee_create(request):

    if request.method == 'POST':

        form = FeeForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                'fee_list'
            )

    else:

        form = FeeForm()

    return render(
        request,
        'fees/fee_form.html',
        {
            'form': form
        }
    )


@login_required
def fee_detail(request, pk):

    fee = get_object_or_404(
        Fee,
        pk=pk
    )

    return render(
        request,
        'fees/fee_detail.html',
        {
            'fee': fee
        }
    )


@login_required
def fee_update(request, pk):

    fee = get_object_or_404(
        Fee,
        pk=pk
    )

    if request.method == 'POST':

        form = FeeForm(
            request.POST,
            instance=fee
        )

        if form.is_valid():

            form.save()

            return redirect(
                'fee_list'
            )

    else:

        form = FeeForm(
            instance=fee
        )

    return render(
        request,
        'fees/fee_form.html',
        {
            'form': form,
            'fee': fee
        }
    )


@login_required
def fee_delete(request, pk):

    fee = get_object_or_404(
        Fee,
        pk=pk
    )

    if request.method == 'POST':

        fee.delete()

        return redirect(
            'fee_list'
        )

    return render(
        request,
        'fees/fee_confirm_delete.html',
        {
            'fee': fee
        }
    )