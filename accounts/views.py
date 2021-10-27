from django.shortcuts import get_object_or_404, render, redirect
from .forms import NurseChangeForm, NurseForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = NurseForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('calendars:main')
    else:
        form = NurseForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'calendars:main')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('calendars:main')


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('calendars:main')


@require_http_methods(['GET', 'POST'])
def update(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    if request.method == 'POST':
        form = NurseChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('calendars:main')
    else:
        form = NurseChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)



def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendars:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)