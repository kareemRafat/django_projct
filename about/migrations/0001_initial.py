# Generated by Django 5.0.3 on 2024-03-19 20:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, null=True, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('tall', models.DecimalField(decimal_places=2, max_digits=2)),
                ('registered_at', models.DateTimeField(verbose_name=datetime.datetime(2024, 3, 19, 22, 26, 21, 107518))),
                ('profile', models.ImageField(upload_to='images/%y/%m/%d')),
            ],
        ),
    ]
