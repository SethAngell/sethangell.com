from django.db import models

# Create your models here.


class LandingPage(models.Model):
    home_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    bio = models.TextField()
    avatar = models.ImageField()
    resume = models.FileField()

    def __str__(self):
        return self.name


class Experience(models.Model):
    exp_id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=40)
    title = models.CharField(max_length=65)
    description = models.TextField()
    present = models.BooleanField()
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return self.company
