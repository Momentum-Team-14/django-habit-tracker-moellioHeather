from django.forms import ModelForm
from .models import CustomUser, HabitGoal


class HabitGoalForm(ModelForm):
    class Meta:
        model = HabitGoal
        fields = ['habit_action', 'goal_qty', 'unit']
