from django.contrib import admin
from .models import BlogPost, PostImage

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    pass

admin.site.register(BlogPost, BlogPostAdmin)

class PostImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(PostImage, PostImageAdmin)
