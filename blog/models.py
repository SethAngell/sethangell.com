from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from .md2html import on_save_attribute_extraction, sanitized_html_for_site

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=256, blank=True)
    md_body = models.TextField()
    html_body = models.TextField(blank=True)
    preview = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(null=False, unique=True, blank=True, max_length=256)
    created_date = models.DateField(auto_now_add=True, blank=True)
    updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def seperate_into_chunks(self, text_field):
        sectioned_post = text_field.split("\n")

    def save(self, *args, **kwargs):  # new
        attributes = on_save_attribute_extraction(self.md_body, self.title)
        self.title = attributes["title"]
        self.preview = attributes["preview"]
        self.md_body = attributes["body"]
        self.html_body = sanitized_html_for_site(self.md_body)

        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class PostImage(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="images")
    reference = models.TextField(blank=False)
    alt_text = models.TextField(blank=False)
    image = models.ImageField()

    def __str__(self):
        return self.reference

