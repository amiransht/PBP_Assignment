# Generated by Django 4.1.1 on 2022-09-28 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='is_finished',
        ),
    ]
