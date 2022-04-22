from django.urls import path

from . import views
from .feeds import AllPosts, LatestPosts

urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("<slug:slug>", views.blog_detail, name="article_detail"),  # new
    path("topics/<str:tag>", views.FilterBlogsByTags, name="tags"),
    path("rss/latest", LatestPosts()),
    path("rss/all", AllPosts()),
]
