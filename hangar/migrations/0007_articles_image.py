# Generated by Django 4.0.4 on 2022-06-14 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangar', '0006_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
    ]
