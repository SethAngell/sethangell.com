from django.contrib import admin
from .models import LandingPage, Experience

# Register your models here.

class LandingPageAdmin(admin.ModelAdmin):
    pass

class ExperienceAdmin(admin.ModelAdmin):
    pass

admin.site.register(LandingPage, LandingPageAdmin)
admin.site.register(Experience, ExperienceAdmin)
