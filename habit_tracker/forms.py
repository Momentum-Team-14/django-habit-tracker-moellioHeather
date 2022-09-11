from django.forms import ModelForm
from .models import HabitGoal, DailyRecord


class HabitGoalForm(ModelForm):
    class Meta:
        model = HabitGoal
        fields = ['habit_action', 'goal_qty', 'unit']


class DailyRecordForm(ModelForm):
    class Meta:
        model = DailyRecord
        fields = ['date', 'daily_qty', 'notes']
