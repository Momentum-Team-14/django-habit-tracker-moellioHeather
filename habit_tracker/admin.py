from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, HabitGoal, DailyRecord

# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(HabitGoal)
admin.site.register(DailyRecord)


# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ['email', 'username', ]
