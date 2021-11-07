from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User

class customUserAdmin(UserAdmin):
   
    fieldsets = (
        ('test', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username',)}),
        ('Nurse', {'fields': ('name', 'birth', 'career', 'ward', 'team', 'hospital', 'is_manager')}),
        ('permission', {'fields': ('is_staff', 'is_superuser', 'is_active', 'date_joined')})
    )


admin.site.register(User, customUserAdmin)