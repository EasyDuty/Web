from django import forms
from .models import ApplyOff

class ApplyOffForm(forms.ModelForm):

    class Meta:
        model = ApplyOff
        fields = ('day')