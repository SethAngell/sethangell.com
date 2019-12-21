from django.urls import path


from . import views

urlpatterns = [
    path('<slug:slug>',views.blog_detail, name='article_detail'), # new
]