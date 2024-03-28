# Generated by Django 5.0.3 on 2024-03-28 23:23

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0007_remove_user_dep_id_user_dep_alter_user_registered_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dep',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department', to='about.department'),
        ),
        migrations.AlterField(
            model_name='user',
            name='registered_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 29, 1, 23, 26, 651581)),
        ),
    ]