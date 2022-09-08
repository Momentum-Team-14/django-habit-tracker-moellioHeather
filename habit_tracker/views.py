from django.shortcuts import render, redirect, get_object_or_404
from .models import HabitGoal, DailyRecord
from .forms import HabitGoalForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


@login_required
def newHabitGoal(request):
    if request.method == 'POST':
        form = HabitGoalForm
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('habit_goals')

    form = HabitGoalForm()
    context = {'form': form}
    return render(request, 'habit_tracker/habit_form.html', context)
