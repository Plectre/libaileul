# Generated by Django 4.0.4 on 2022-08-03 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='pilote',
            new_name='nom',
        ),
    ]
