from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    short_description = models.CharField(max_length=100, blank=True, null=True)
    generic_link = models.CharField(max_length=500, blank=True, null=True)
    github_link = models.CharField(max_length=200, blank=True, null=True)
    instagram_link = models.CharField(max_length=200, blank=True, null=True)
    facebook_link = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(blank=True, null=True, upload_to="profile_pic", default="profile_pic/default_profile_pic.png")
    post_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return str(self.user.username)