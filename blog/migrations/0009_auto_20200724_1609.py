# Generated by Django 2.2.6 on 2020-07-24 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='preview',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]