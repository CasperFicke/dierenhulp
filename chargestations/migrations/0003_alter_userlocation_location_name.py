# Generated by Django 4.1.3 on 2023-06-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chargestations', '0002_userlocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlocation',
            name='location_name',
            field=models.CharField(max_length=100),
        ),
    ]