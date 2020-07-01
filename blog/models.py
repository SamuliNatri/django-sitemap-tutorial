from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Post(models.Model):

    title = models.CharField(max_length=255,
                             unique=True)
    slug = models.SlugField(max_length=50,
                            unique=True,
                            default='')
    # HERE
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # HERE
    def get_absolute_url(self):
        return reverse('blog:detail',
                       args=[self.slug])