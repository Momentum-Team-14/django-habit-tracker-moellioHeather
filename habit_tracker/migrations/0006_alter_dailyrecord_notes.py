# Generated by Django 4.1.1 on 2022-09-11 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0005_dailyrecord_daily_qty_alter_dailyrecord_habit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyrecord',
            name='notes',
            field=models.TextField(blank=True, default='', max_length=512, null=True),
        ),
    ]
