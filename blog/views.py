from django.shortcuts import render
from .md2html import sanitized_html_for_site
from .models import BlogPost

# Create your views here.
def blog_detail(request, slug):
    blog_post = BlogPost.objects.get(slug=slug)

    context = {
        "blog_post" : blog_post
    }

    return render(request, "blog/blog_detail.html", context)

def blog_index(request):
    blogs = BlogPost.objects.order_by('-created_date')

    context = {
        "blog_posts" : blogs
    }

    return render(request, "blog/blog_index.html", context)

