# Generated by Django 3.1.5 on 2021-04-22 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college_app', '0005_auto_20210422_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='degreestudent',
            name='export_to_CSV',
        ),
        migrations.RemoveField(
            model_name='tenstudent',
            name='export_to_CSV',
        ),
        migrations.RemoveField(
            model_name='twelvestudent',
            name='export_to_CSV',
        ),
    ]
