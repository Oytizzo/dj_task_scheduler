from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    slug = models.SlugField(blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
