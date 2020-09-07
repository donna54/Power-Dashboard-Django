# Generated by Django 3.1.1 on 2020-09-06 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_hospitalbedsindia'),
    ]

    operations = [
        migrations.CreateModel(
            name='ICMRTestingLabs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('pincode', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
    ]