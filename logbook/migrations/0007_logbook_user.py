# Generated by Django 4.0.4 on 2022-06-21 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0006_remove_logbook_nb_personne_logbook_duo'),
    ]

    operations = [
        migrations.AddField(
            model_name='logbook',
            name='user',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
