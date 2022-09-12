from django.db import models
from django.db.models import Q
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# Create your models here.


class CustomUser(AbstractUser):
    pass


class HabitGoal(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='habits', null=True)
    habit_action = models.CharField(
        max_length=100, help_text="i.e. read, meditate, code, etc")
    goal_qty = models.IntegerField()
    unit = models.CharField(
        max_length=50, help_text="i.e. pages, minutes, lines, etc")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'{self.habit_action} {self.goal_qty} {self.unit} daily'


class DailyRecord(models.Model):
    habit = models.ForeignKey(
        'HabitGoal', on_delete=models.CASCADE, related_name="records", blank=True, null=True)
    date = models.DateField(null=True)
    daily_qty = models.IntegerField()
    notes = models.TextField(max_length=512, default="", blank=True, null=True)

    @property
    def get_notes(self):
        if self.notes:
            return self.notes
        else:
            return "no excuses today"

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['date'], name='one_entry_daily')
    #     ]

    # def clean(self):

    #     if self.date & self.date == self.date:
    #         raise ValidationError(
    #             {'date': _('You may only record one entry per habit each day')})

    def __str__(self):
        return f'{self.daily_qty} {self.habit.unit} {self.habit.habit_action} on {self.date}'
