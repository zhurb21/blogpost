# Generated by Django 3.1.4 on 2020-12-11 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('var7_app', '0002_task_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='note',
        ),
    ]
