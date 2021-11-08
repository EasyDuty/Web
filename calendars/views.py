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
        duties = '' * 31
    context = {
        'duties': duties,
        'duty_count_d': duties.count('D'),
        'duty_count_e': duties.count('E'),
        'duty_count_n': duties.count('N'),
        'duty_count_o': duties.count('O'),
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
@require_http_methods(['POST'])
def make_duty(request, year, month):
    if request.method=='POST':
        month += 1
        team_num = 3
        people = 6
        dt_now = datetime.datetime.now()

        # 저번 달 정보 불러오기
        if month == 1:
            key = str(year-1) + '12'
        else:
            key = str(year) + str(month-1)
        users = get_user_model()
        myWard = users.objects.filter(ward=request.user.ward)
        teams = []


       # 병동에 있는 팀 목록 생성
        for i in myWard:
            if i.team in teams:
                continue
            else:
                teams.append(i.team)
        for t in range(team_num):
            myTeam = users.objects.filter(team=teams[t], ward=request.user.ward)
            last_duties = []
            careers = []
            for i in range(6):
                try:
                    person = myTeam[i]
                    last_duties.append(person.duty.get(key)[-2:])
                except:
                    last_duties.append('OO')
                careers.append(dt_now.year - int(person.career.year))

        # 듀티 생성
            duties = get_schedule(last_duties, year, month)
            # print(duties)
            for i in range(people):
                person = myTeam[i]
                person.duty = {str(year) + str(month) : duties[i]}
                person.save()
        return redirect('calendars:ward_duty')
    return
    

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

