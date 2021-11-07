from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import ApplyOffForm
from .algo_team_day_first import get_schedule
import datetime


@login_required
@require_safe
def main(request):
    dt_now = datetime.datetime.now()
    year = str(dt_now.year)
    month = str(dt_now.month)
    try:
        duties = request.user.duty[year+month]
    except:
        duties = ' ' * 31
    context = {
        'duties': duties,
        'duty-count-d': duties.count('D'),
        'duty-count-e': duties.count('E'),
        'duty-count-n': duties.count('N'),
        'duty-count-o': duties.count('O'),
    }
    return render(request, 'calendars/main.html', context)
    

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
        if month == 1:
            key = str(year-1) + '12'
        else:
            key = str(year) + str(month-1)
        users = get_user_model()
        myTeam = users.objects.filter(team=request.user.team)
        last_duties = []
        for i in range(6):
            try:
                person = myTeam[i]
                last_duties.append(person.duty.get(key)[-2:])
            except:
                last_duties.append('OO')
        # prev_month_duty = request.POST['dd']
        duties = get_schedule(last_duties, year, month)
        for i in range(6):
            person = myTeam[i]
            person.duty = {str(year) + str(month) : duties[i]}
            person.save()
        # context = {
        #     'duties': duties,
        #     'myTeam': myTeam,
        # }
        return redirect('calendars:main')

    else:
        pass
    context = {
        
    }
    return render(request, 'calendars/make-duty.html', context)

# 병동 듀티 보는 페이지
@login_required
@require_safe
def ward_duty(request):
    ward = request.user.ward
    users = get_user_model()
    wards = users.objects.filter(ward=ward)
    context = {
        'myWard': wards,
    }
    return render(request, 'calendars/ward-duty.html', context)

