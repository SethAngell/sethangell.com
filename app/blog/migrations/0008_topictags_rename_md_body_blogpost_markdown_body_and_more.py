# Generated by Django 4.0.2 on 2022-02-12 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_auto_20200619_1551"),
    ]

    operations = [
        migrations.CreateModel(
            name="TopicTags",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name="blogpost",
            old_name="md_body",
            new_name="markdown_body",
        ),
        migrations.AddField(
            model_name="blogpost",
            name="visibility",
            field=models.CharField(
                choices=[("PU", "Public"), ("PR", "Private")],
                default="PR",
                max_length=2,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="title",
            field=models.CharField(max_length=256),
        ),
        migrations.AddField(
            model_name="blogpost",
            name="tags",
            field=models.ManyToManyField(to="blog.TopicTags"),
        ),
    ]
