# Generated by Django 2.2.6 on 2020-01-07 04:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_auto_20200107_0343"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="created_date",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="blogpost",
            name="updated",
            field=models.DateField(auto_now=True),
        ),
    ]