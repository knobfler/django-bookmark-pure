from django.db import models

# Create your models here.
from django.urls import reverse


class Bookmark(models.Model):
    site_title = models.CharField(max_length=100)
    site_url = models.URLField('site_url')

    class Meta:
        ordering = ['site_title']

    def __str__(self):
        return self.site_title

    def get_absolute_url(self):
        return reverse('bookmark:detail', args=[str(self.id)])

