# Generated by Django 4.1.3 on 2023-06-29 13:41

from django.db import migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nestkasten', '0004_alter_fourageergebied_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nestkast',
            name='location',
            field=djgeojson.fields.PointField(blank=True, null=True),
        ),
    ]
