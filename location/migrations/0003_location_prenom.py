# Generated by Django 4.0.4 on 2022-08-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_rename_pilote_location_nom'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='prenom',
            field=models.CharField(default='', max_length=50),
        ),
    ]
