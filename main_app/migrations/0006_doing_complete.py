# Generated by Django 4.1 on 2022-08-11 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_place_todo_doing'),
    ]

    operations = [
        migrations.AddField(
            model_name='doing',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
