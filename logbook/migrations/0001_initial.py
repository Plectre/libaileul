# Generated by Django 4.0.4 on 2022-06-11 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('aircraft', models.CharField(max_length=50)),
                ('ident', models.CharField(max_length=10)),
                ('from_airport', models.CharField(max_length=200)),
                ('to_airport', models.CharField(max_length=200)),
                ('start', models.CharField(max_length=20)),
                ('stop', models.CharField(max_length=20)),
                ('flyTime', models.CharField(max_length=20)),
            ],
        ),
    ]
