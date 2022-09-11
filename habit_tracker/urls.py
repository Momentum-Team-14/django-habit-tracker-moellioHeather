from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('habit_list/', views.habit_list, name='habit_list'),
    path('new_habit_goal/', views.newHabitGoal, name='new_habit_goal'),
    path('record_daily/', views.newDailyRecord, name='record_daily'),

]
