from django.shortcuts import render, redirect, get_object_or_404
from .models import HabitGoal, DailyRecord
from .forms import HabitGoalForm, DailyRecordForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'habit_tracker/home.html')


def habit_list(request):
    habits = HabitGoal.objects.all()
    return render(request, 'habit_tracker/habit_list.html',
                  {'habits': habits})


# @login_required
# def habit_detail(request, pk):
#     habit = get_object_or_404(HabitGoal, pk=pk)
#     return render(request, 'habit_tracker/habit_detail.html', {'habit': habit})


@login_required
def newHabitGoal(request):
    if request.method == 'POST':
        form = HabitGoalForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('habit_list')
    else:
        form = HabitGoalForm()
        context = {'form': form}
        return render(request, 'habit_tracker/habit_form.html', context)


@login_required
def newDailyRecord(request, pk):
    habit = habit.objects.get(pk=pk)
    if request.method == 'POST':
        form = DailyRecordForm()
        if form.is_valid():
            return redirect('habit_detail')
    else:
        form = DailyRecordForm()
        context = {'form': form}
        return render(request, 'habit_tracker/record_daily.html', context)


# def habit_detail(request, pk):
#     habits = HabitGoal.objects.get(pk=pk)
#     form = DailyRecord(instance=habit)
#     context = {""}
#     return render(request, 'records/habit_detail.html', {'habit': habit})
