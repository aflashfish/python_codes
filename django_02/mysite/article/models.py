from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class AddArticle(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    public_time = models.DateTimeField()
    part = models.CharField(max_length=200)
    read_num = models.IntegerField()
    comment_num = models.IntegerField()
    body = models.TextField()


class AddArticle2(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    public_time = models.DateTimeField()
    part = models.CharField(max_length=200)
    read_num = models.IntegerField()
    comment_num = models.IntegerField()
    body = HTMLField()

