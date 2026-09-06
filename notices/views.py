from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Notice
from .forms import NoticeForm


@login_required
def notice_list(request):

    notices = Notice.objects.all()

    search = request.GET.get('search', '')
    category = request.GET.get('category', '')

    if search:
        notices = notices.filter(
            Q(title__icontains=search)
            |
            Q(description__icontains=search)
        )

    if category:
        notices = notices.filter(category=category)

    context = {
        'notices': notices,
        'search': search,
        'selected_category': category,
    }

    return render(
        request,
        'notices/notice_list.html',
        context
    )


@login_required
def notice_create(request):

    if request.method == 'POST':

        form = NoticeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('notice_list')

    else:
        form = NoticeForm()

    return render(
        request,
        'notices/notice_form.html',
        {'form': form}
    )


@login_required
def notice_detail(request, pk):

    notice = get_object_or_404(
        Notice,
        pk=pk
    )

    return render(
        request,
        'notices/notice_detail.html',
        {'notice': notice}
    )


@login_required
def notice_update(request, pk):

    notice = get_object_or_404(
        Notice,
        pk=pk
    )

    if request.method == 'POST':

        form = NoticeForm(
            request.POST,
            instance=notice
        )

        if form.is_valid():
            form.save()
            return redirect('notice_list')

    else:

        form = NoticeForm(
            instance=notice
        )

    return render(
        request,
        'notices/notice_form.html',
        {
            'form': form,
            'notice': notice
        }
    )


@login_required
def notice_delete(request, pk):

    notice = get_object_or_404(
        Notice,
        pk=pk
    )

    if request.method == 'POST':

        notice.delete()

        return redirect('notice_list')

    return render(
        request,
        'notices/notice_confirm_delete.html',
        {'notice': notice}
    )