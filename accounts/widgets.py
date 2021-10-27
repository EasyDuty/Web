from django import forms

class DatePickerWidget(forms.DateInput):
    template_name = "widgets/datepicker.html"