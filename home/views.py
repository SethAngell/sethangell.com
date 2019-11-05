from django.shortcuts import render
from .models import LandingPage, Experience
from django.db.models import Case, When

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
        '-current_job',
        '-past_job',

    )
    context = {
        "info": info,
        "experience": experience
    }
    return render(request, "home/HomeTemp.html", context)