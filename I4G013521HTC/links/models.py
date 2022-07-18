from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from .managers import ActiveLinkManager
# Create your models here.

class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description= models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, unique=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    objects = models.Manager()
    public = ActiveLinkManager()
