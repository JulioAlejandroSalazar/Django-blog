from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, blank=True, default="")
    country = models.CharField(max_length=100, blank=True, default="")
    birth_date = models.DateField(blank=True, null=True)
    short_description = models.CharField(max_length=100, blank=True, default="")
    generic_link = models.CharField(max_length=500, blank=True, default="")
    github_link = models.CharField(max_length=200, blank=True, default="")
    instagram_link = models.CharField(max_length=200, blank=True, default="")
    facebook_link = models.CharField(max_length=200, blank=True, default="")
    bio = models.TextField(blank=True, default="")
    profile_pic = models.ImageField(blank=True, null=True, upload_to="profile_pic", default="profile_pic/default_profile_pic.png")

    def __str__(self):
        return str(self.user.username)