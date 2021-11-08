from django.urls import path
from . import views

app_name = 'calendars'
urlpatterns = [
    path('main/', views.main, name='main'),
    path('apply-off/', views.apply_off, name='apply-off'),
    path('make-duty/<int:year>/<int:month>/', views.make_duty, name='make_duty'),
    path('wardduty/', views.ward_duty, name='ward_duty'),
    path('worker/<int:year>/<int:month>/<int:day>/', views.worker, name='worker'),
]
