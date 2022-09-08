# Generated by Django 4.1.1 on 2022-09-08 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HabitGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habit_action', models.CharField(help_text='i.e. read, meditate, code, etc', max_length=100)),
                ('goal_qty', models.IntegerField()),
                ('unit', models.CharField(help_text='i.e. pages, minutes, lines, etc', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habits', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DailyRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('notes', models.TextField(default='', max_length=512)),
                ('habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habits', to='habit_tracker.habitgoal')),
            ],
        ),
    ]