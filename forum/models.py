from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Profile(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    description = models.TextField()


class Post(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_text = models.TextField()
    is_publised = models.BooleanField(default=False)

    def __str__(self):
        return self.post_text
