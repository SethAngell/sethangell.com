# Generated by Django 2.2.6 on 2019-10-19 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LandingPage",
            fields=[
                ("home_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("bio", models.TextField()),
                ("avatar", models.ImageField(upload_to="")),
                ("resume", models.FileField(upload_to="")),
            ],
        ),
    ]
