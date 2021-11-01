from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import ApplyOffForm
from .algo import makes_duty
import datetime


@login_required
@require_safe
def main(request):
    dt_now = datetime.datetime.now()
    year = str(dt_now.year)
    month = str(dt_now.month)
    if request.user.duty.get(year+month):
        duties = request.user.duty[year+month]
    else:
        duties = ' ' * 30
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
        year = int(request.POST['year'])
        month = int(request.POST['month'])
        prev_month_duty = request.POST['dd']
        duty = makes_duty(prev_month_duty, year, month)
        request.user.duty = {str(year) + str(month) : duty}
        request.user.save()
        context = {
            'duties': duty,
        }
        return redirect('calendars:main')

    else:
        pass
        # users = get_user_model()
        # teams = users.objects.filter(team=request.user.team)
    context = {

    }
    return render(request, 'calendars/make-duty.html', context)

# 팀원 듀티 보는 페이지
@login_required
@require_safe
def team_duty(request):
    team = request.user.team
    users = get_user_model()
    teams = users.objects.filter(team=team)
    context = {
        'teams': teams,
    }
    return render(request, 'calendars/team_duty.html', context)

