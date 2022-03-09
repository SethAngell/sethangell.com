from django.contrib import admin

from .models import BlogPost, PostImage, TopicTags


# Register your models here.
class PostImageAdmin(admin.ModelAdmin):
    pass


class BlogPostAdmin(admin.ModelAdmin):
    pass


class TopicTagAdmin(admin.ModelAdmin):
    pass


admin.site.register(PostImage, PostImageAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(TopicTags, TopicTagAdmin)
