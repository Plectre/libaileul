# Generated by Django 4.0.4 on 2022-06-21 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logbook', '0007_logbook_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logbook',
            name='user',
            field=models.CharField(default='kiki', max_length=50),
        ),
    ]
