from django.contrib.syndication.views import Feed
from django.urls import reverse

from .models import BlogPost


class LatestPosts(Feed):
    title = "DoubleL Press"
    link = "/blog/"
    description = "The 5 most recently published posts on DoubleL Press"

    def items(self):
        return BlogPost.objects.order_by("-created_date").filter(visibility="PU")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.preview


class AllPosts(Feed):
    title = "DoubleL Press"
    link = "/blog/"
    description = "DoubleL Press in it's entirety :)"

    def items(self):
        return BlogPost.objects.order_by("-created_date").filter(visibility="PU")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.preview
