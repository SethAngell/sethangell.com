# Generated by Django 4.0.2 on 2022-03-11 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_alter_blogpost_preview"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="title",
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
