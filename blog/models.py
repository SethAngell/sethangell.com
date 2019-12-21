from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from .md2html import on_save_attribute_extraction

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=256, blank=True)
    body = models.TextField()
    slug = models.SlugField(null=False, unique=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def seperate_into_chunks(self, text_field):
        sectioned_post = text_field.split("\n")
        print(sectioned_post[0])

    def save(self, *args, **kwargs):  # new
        self.title = on_save_attribute_extraction(self.body)["title"]
        if not self.slug:
            self.slug = slugify(self.title)
            print(self.body)
        return super().save(*args, **kwargs)