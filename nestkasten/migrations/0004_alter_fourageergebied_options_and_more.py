# Generated by Django 4.1.3 on 2023-06-29 13:41

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nestkasten', '0003_fourageergebied_nestkast_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fourageergebied',
            options={'verbose_name': 'Fourageergebied', 'verbose_name_plural': 'Fourageergebieden'},
        ),
        migrations.AlterField(
            model_name='fourageergebied',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='nestkast',
            name='location',
            field=djgeojson.fields.PointField(),
        ),
    ]