from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import widgets
from .widgets import DatePickerWidget

class NurseForm(UserCreationForm):
    name = forms.CharField(max_length=100, label='이름')
    birth = forms.DateField(label='생년월일', widget=DatePickerWidget)
    career = forms.DateField(label='입사일', widget=DatePickerWidget)
    ward = forms.CharField(max_length=100, label='병동')
    team = forms.CharField(max_length=100, label='팀')
    hospital = forms.CharField(max_length=100, label='병원')

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password1',
            'password2',
            'name',
            'birth',
            'career',
            'ward',
            'team',
            'hospital',
        )
        labels = {
            'username': ('ID'),
        }
        

class NurseChangeForm(UserChangeForm):
    name = forms.CharField(max_length=100, label='이름')
    birth = forms.DateField(label='생년월일', widget=DatePickerWidget)
    career = forms.DateField(label='입사일', widget=DatePickerWidget)
    ward = forms.CharField(max_length=100, label='병동')
    team = forms.CharField(max_length=100, label='팀')
    hospital = forms.CharField(max_length=100, label='병원')
    

    class Meta:
        model = get_user_model()
        fields = (
            'name',
            'birth',
            'career',
            'ward',
            'team',
            'hospital',
        )