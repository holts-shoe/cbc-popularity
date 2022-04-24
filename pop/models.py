from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    full_page_url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    date_created = models.DateTimeField('Date created')
    num_replies = models.IntegerField(default=0)
    image_url = models.CharField(max_length=200)
    def __str__(self):
        return self.full_page_url