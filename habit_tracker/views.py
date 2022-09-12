from django.shortcuts import render, redirect, get_object_or_404
from .models import HabitGoal, DailyRecord
from .forms import HabitGoalForm, DailyRecordForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'home.html')


def habit_list(request):
    habits = HabitGoal.objects.all()
    return render(request, 'habit_tracker/habit_list.html',
                  {'habits': habits})


@login_required
def habit_detail(request, pk):
    habit = get_object_or_404(HabitGoal, pk=pk)
    records = DailyRecord.objects.filter(habit=pk).order_by('-date')
    return render(request, 'habit_tracker/habit_detail.html', {'habit': habit, 'records': records})


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
def editHabit(request, pk):
    habit = HabitGoal.objects.get(pk=pk)
    form = HabitGoalForm(instance=habit)
    if request.method == "POST":
        form = HabitGoalForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, 'habit_tracker/habit_form.html', {'form': form})


@login_required
def newDailyRecord(request, pk):
    habit = get_object_or_404(HabitGoal, pk=pk)
    if request.method == 'POST':
        form = DailyRecordForm(data=request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.habit = habit
            record.save()
            return redirect('habit_detail', pk=pk)
    else:
        form = DailyRecordForm()
        # context =
    return render(request, 'habit_tracker/record_form.html', {'form': form})


@login_required
def editRecord(request, pk):
    record = DailyRecord.objects.get(pk=pk)
    form = DailyRecordForm(instance=record)
    if request.method == "POST":
        form = DailyRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, 'habit_tracker/record_form.html', {'form': form})


@login_required
def delete(request, pk):
    context = {}
    return render(request, 'habit_tracker/delete.html', context)
