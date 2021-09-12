import random
import string

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

DEFAULT_ID = 1


def rand_slug():
    return ''.join(random.choice(string.ascii_letters) for _ in range(6))


class Post(models.Model):
    slug = models.SlugField(blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=DEFAULT_ID)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.title)
        super().save(*args, **kwargs)
