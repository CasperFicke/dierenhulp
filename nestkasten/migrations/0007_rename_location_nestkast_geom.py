# Generated by Django 4.1.3 on 2023-06-29 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nestkasten', '0006_alter_fourageergebied_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nestkast',
            old_name='location',
            new_name='geom',
        ),
    ]