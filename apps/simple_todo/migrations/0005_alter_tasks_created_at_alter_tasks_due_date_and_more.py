# Generated by Django 4.0.3 on 2022-03-13 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_todo', '0004_alter_tasks_created_at_alter_tasks_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 13, 17, 18, 41, 996083)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='due_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='finised',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='remainder',
            field=models.DateTimeField(blank=True),
        ),
    ]
