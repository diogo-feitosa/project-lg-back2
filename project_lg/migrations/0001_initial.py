# Generated by Django 3.2.9 on 2021-11-12 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('startDate', models.DateField(max_length=30)),
                ('endDate', models.DateField(max_length=30)),
                ('value', models.FloatField(max_length=30)),
                ('risk', models.CharField(choices=[(0, 'low'), (1, 'medium'), (2, 'high')], max_length=1)),
            ],
        ),
    ]
