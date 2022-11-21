from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    post_image = models.ImageField(blank=True, null=True, upload_to="post_image")
    is_edited = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.title + ' | ' + str(self.author)