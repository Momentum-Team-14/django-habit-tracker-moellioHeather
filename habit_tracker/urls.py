from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('habit_list/', views.habit_list, name='habit_list'),
    path('new_habit_goal/', views.newHabitGoal, name='new_habit_goal'),
    path('habit_list/<int:pk>/record_daily/new',
         views.newDailyRecord, name='record_daily'),
    path('habit_list/<int:pk>', views.habit_detail, name="habit_detail"),
    path('edit_habit/<int:pk>', views.editHabit, name="edit_habit"),
    path('edit_record/<int:pk>', views.editRecord, name="edit_record"),
    path('delete/<int:pk>', views.delete, name="delete"),
]
