# Generated by Django 4.0.4 on 2022-07-31 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangar', '0008_alter_articles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
