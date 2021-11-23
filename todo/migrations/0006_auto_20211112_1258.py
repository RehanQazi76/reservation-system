# Generated by Django 3.2.3 on 2021-11-12 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20211112_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
        migrations.AddField(
            model_name='task',
            name='date_from',
            field=models.DateTimeField(blank=True, null=True, verbose_name='From'),
        ),
    ]
