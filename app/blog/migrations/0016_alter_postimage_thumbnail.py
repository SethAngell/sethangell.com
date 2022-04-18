# Generated by Django 4.0.2 on 2022-04-18 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0015_postimage_thumbnail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postimage",
            name="thumbnail",
            field=models.ImageField(
                blank=True,
                editable=False,
                null=True,
                upload_to="blog_images/thumbnails",
            ),
        ),
    ]
