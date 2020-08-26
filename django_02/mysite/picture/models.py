from django.db import models
from datetime import date
from uuid import uuid4
import os
from django.urls import reverse


def path_and_rename(instance, filename):
    upload_to = 'mypictures'
    ext = filename.rsplit('.', maxsplit=1)[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


# Create your models here.
class Picture(models.Model):
    title = models.CharField("标题", max_length=100, blank=True, default='')
    # 当你使用ImageField或FileField的时候，你必须定义upload_to选项
    image = models.ImageField("图片", upload_to=path_and_rename, blank=True)
    date = models.DateField(default=date.today)
    body = models.TextField(default='')

    def __str__(self):
        return self.title

    # 对于使用Django自带的通用视图非常重要
    def get_absolute_url(self):
        return reverse('picture:pic_detail', args=[str(self.id)])
