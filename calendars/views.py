from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .forms import ApplyOffForm


@login_required
@require_safe
def main(request):
    # 인증되어 있지 않다면 로그인 창으로 유도
    data = list('DODODEDDNDDNDDDNDDODDEDDDODDND')
    duties = []
    for duty in data:
        if duty == 'D':
            duties.append('DAY')
        elif duty == 'O':
            duties.append('OFF')
        elif duty == 'N':
            duties.append('NIGHT')
        else:
            duties.append('EVENING')

    context = {
        'duties': duties,
    }
    return render(request, 'calendars/main.html', context)


@login_required
def ward(request):
    context = {

    }
    return render(request, 'claender/ward.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def apply_off(request):
    if request.method=='POST':
        form = ApplyOffForm(request.POST)
        if form.is_valid():
            off = form.save(commit=False)
            off.user = request.user
            off.save()
            return redirect('calendars:main')
    else:
        form = ApplyOffForm()
    context = {
        'form': form,
    }
    return render(request, 'calendars/apply-off.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def make_duty(request):
    if request.method=='POST':
        pass
    else:
        pass
    context = {

    }
    return render(request, 'calendars/make-duty.html', context)