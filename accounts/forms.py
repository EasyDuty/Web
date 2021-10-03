from calendars.models import Nurse
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class NurseForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    career = forms.IntegerField()
    ward = forms.CharField(max_length=100)
    team = forms.CharField(max_length=100)
    hospital = forms.CharField(max_length=100)

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password1',
            'password2',
            'name',
            'age',
            'career',
            'ward',
            'team',
            'hospital',
        )

class NurseChangeForm(NurseForm):

    class Meta:
        model = get_user_model()
        fields = (
            'name',
            'age',
            'career',
            'ward',
            'team',
            'hospital',
        )