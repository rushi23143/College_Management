# Generated by Django 3.1.5 on 2021-05-22 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_app', '0008_auto_20210521_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenstudent',
            name='tenth',
            field=models.IntegerField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twelvestudent',
            name='twelth',
            field=models.IntegerField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
