# Generated by Django 3.1.1 on 2020-09-06 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_individualdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individualdetails',
            name='age',
            field=models.CharField(max_length=3),
        ),
    ]