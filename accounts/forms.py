from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class NurseForm(UserCreationForm):


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

class NurseChangeForm(UserChangeForm):

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