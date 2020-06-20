from django.shortcuts import render
from .md2html import sanitized_html_for_site
from .models import BlogPost, PostImage

# Create your views here.
def blog_detail(request, slug):
    blog_post = BlogPost.objects.get(slug=slug)
    blog_images = PostImage.objects.filter(post=blog_post)

    print(blog_images)


    context = load_context_with_all_image_tags_and(blog_post, blog_images)
    print(context)

    # context = {
    #     "blog_post": blog_post,
    #     "image": blog_images
    # }
    return render(request, "blog/blog_detail.html", context)

def blog_index(request):
    blogs = BlogPost.objects.order_by('-created_date')

    context = {
        "blog_posts" : blogs
    }

    return render(request, "blog/blog_index.html", context)

def load_context_with_all_image_tags_and(post, images):
    staging_context = {"blog_post": post}

    for obj in images:
        staging_context[str(obj.reference)] = obj

    return staging_context

