# Generated by Django 3.0.8 on 2020-08-04 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0005_todo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]