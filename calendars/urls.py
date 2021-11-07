from django.urls import path
from . import views

app_name = 'calendars'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('apply-off/', views.apply_off, name='apply-off'),
    path('make-duty/', views.make_duty, name='make-duty'),
    path('wardduty/', views.ward_duty, name='ward_duty'),
]
