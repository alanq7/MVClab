from django.db import models
from django.utils.text import slugify


class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=150)
    rating = models.PositiveIntegerField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title