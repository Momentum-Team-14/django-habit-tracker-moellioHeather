from django.forms import ModelForm
from .models import HabitGoal, DailyRecord
from django.utils import timezone
from django import forms


class HabitGoalForm(ModelForm):
    class Meta:
        model = HabitGoal
        fields = ['habit_action', 'goal_qty', 'unit']


class DailyRecordForm(ModelForm):
    date = forms.DateField(widget=forms.SelectDateWidget(
        empty_label=("year", "month", "day")), initial=timezone.now())

    class Meta:
        model = DailyRecord
        fields = ['date', 'daily_qty', 'notes']
