from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, HabitGoal

# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(HabitGoal)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', ]
