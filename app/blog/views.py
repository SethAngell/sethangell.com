from django.shortcuts import render

from .models import BlogPost, PostImage


# Create your views here.
def blog_detail(request, slug):
    blog_post = BlogPost.objects.get(slug=slug)

    return render(request, "blog/blog_detail.html", {"post": blog_post})


def blog_index(request):
    blogs = BlogPost.objects.filter(visibility="PU").order_by("-created_date")

    context = {"posts": blogs}

    return render(request, "blog/blog_index.html", context)


def FilterBlogsByTags(request, tag):
    print(tag)
    blogs = BlogPost.objects.filter(tags__tag_name=tag)
    print(blogs)

    context = {"tag_name": tag, "posts": blogs}

    return render(request, "blog/blog_tags.html", context)


def load_context_with_all_image_tags_and(post, images):
    staging_context = {"blog_post": post}

    for obj in images:
        staging_context[str(obj.reference)] = obj

    return staging_context
