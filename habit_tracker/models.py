from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class HabitGoal(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='habits')
    habit_action = models.CharField(
        max_length=100, help_text="i.e. read, meditate, code, etc")
    goal_qty = models.IntegerField()
    unit = models.CharField(
        max_length=50, help_text="i.e. pages, minutes, lines, etc")


class DailyRecord(models.Model):
    habit = models.ForeignKey(
        'HabitGoal', on_delete=models.CASCADE, related_name="habits", blank=True, null=True)
    date = models.DateField(null=True)
    notes = models.TextField(max_length=512, default="")
    daily_qty = models.IntegerField

    @property
    def get_notes(self):
        if self.notes:
            return self.notes
        else:
            return "no excuses today"

    def __str__(self):
        pass
