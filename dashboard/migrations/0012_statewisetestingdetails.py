# Generated by Django 3.1.1 on 2020-09-06 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_population_india_census2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatewiseTestingDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=20)),
                ('totalsamples', models.CharField(max_length=10)),
                ('negative', models.CharField(max_length=10)),
                ('positive', models.CharField(max_length=10)),
            ],
        ),
    ]