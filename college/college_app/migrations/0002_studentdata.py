# Generated by Django 3.1.5 on 2021-04-21 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('ten', models.IntegerField(max_length=20)),
                ('twelve', models.IntegerField(max_length=20)),
                ('degree', models.IntegerField(max_length=20)),
            ],
        ),
    ]