from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from .forms import ApplyOffForm
from .algo import makes_duty


@login_required
@require_safe
def main(request):
    if request.user.duty:
        duties = request.user.duty
        context = {
            'duties': duties,
        }
        return render(request, 'calendars/main.html', context)
    return redirect('calendars:make-duty')


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
        year = int(request.POST['year'])
        month = int(request.POST['month'])
        prev_month_duty = request.POST['dd']
        duty = makes_duty(prev_month_duty, year, month)
        request.user.duty = duty
        request.user.save()
        context = {
            'duties': duty,
        }
        return redirect('calendars:main')

    else:
        pass
    context = {

    }
    return render(request, 'calendars/make-duty.html', context)
