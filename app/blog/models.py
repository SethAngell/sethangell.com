from io import BytesIO

import markdown
from django.core.files import File
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from PIL import Image

# TODO: blog.BlogPost: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
# HINT: Configure the DEFAULT_AUTO_FIELD setting or the BlogConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.

# Create your models here.
class TopicTags(models.Model):
    tag_name = models.CharField(max_length=50)


class BlogPost(models.Model):
    title = models.CharField(max_length=256, blank=False)
    markdown_body = models.TextField()
    html_body = models.TextField(blank=True)
    tags = models.ManyToManyField(TopicTags)
    preview = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(null=False, unique=True, blank=True, max_length=256)
    created_date = models.DateField(auto_now_add=True, blank=True)
    updated = models.DateField(auto_now=True, blank=True)
    visibility = models.CharField(
        max_length=2, choices=[("PU", "Public"), ("PR", "Private")]
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def pretty_preview(self):
        words = self.markdown_body.split(" ")
        preview = ""

        while len(preview) < 150:
            preview += words.pop(0)

        return markdown.markdown(preview)

    def save(self, *args, **kwargs):  # new
        self.preview = self.pretty_preview()
        self.html_body = markdown.markdown(self.markdown_body)

        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class PostImage(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="images")
    reference = models.TextField(blank=False)
    alt_text = models.TextField(blank=False)
    image = models.ImageField(upload_to="blog_images")

    def __str__(self):
        return self.reference

    def generate_png_version(self, p_image, p_name):
        """
        Generates new DjangoFile object containing the converted and renamed image
        Note: Image is renamed after the reference var
        """
        # Adapted from https://bhch.github.io/posts/2018/12/django-how-to-editmanipulate-uploaded-images-on-the-fly-before-saving/
        g_image = Image.open(p_image)
        g_io = BytesIO()  # create a BytesIO object
        g_image.save(g_io, "PNG")  # save image to BytesIO object
        generated_image = File(
            g_io, name=f"{p_name}.png"
        )  # create a django friendly File object

        return generated_image

    def save(self, *args, **kwargs):
        if self.image:
            self.image = self.generate_png_version(self.image, self.reference)
        super().save(*args, **kwargs)
