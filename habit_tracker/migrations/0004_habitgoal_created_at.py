# Generated by Django 4.1.1 on 2022-09-08 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0003_habitgoal_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitgoal',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]