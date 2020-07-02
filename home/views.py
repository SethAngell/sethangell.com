from django.shortcuts import render
from .models import LandingPage, Experience
from django.db.models import Case, When
from blog.models import BlogPost

# Create your views here.

def Homepage(request):
    info = LandingPage.objects.get(pk=1)
    # experience = Experience.objects.all().order_by('-start_year')
    experience = Experience.objects.annotate(
        current_job=Case(
            When(present=True, then=('start_year')),
            default=None
        ),
        past_job=Case(
            When(present=False, then=('start_year')),
            default=None
        )
    ).order_by(
        '-past_job',
        '-current_job',
    )
    recent_post = BlogPost.objects.latest('created_date')
    context = {
        "info": info,
        "experience": experience,
        "blog": recent_post
    }
    return render(request, "home/home.html", context)