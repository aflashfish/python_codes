from django.db import models

# Create your models here.


class BoardUsers(models.Model):
    username = models.CharField(max_length=120)
    email = models.EmailField()
    comment = models.TextField()
    ip = models.CharField(max_length=120)
    ie_browser = models.CharField(max_length=120, default="IEBrowser")
    created_time = models.DateTimeField()

