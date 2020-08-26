from django.urls import re_path, path
from . import views

app_name = 'blog'

urlpatterns = [

    re_path(r'blog/$', views.index, name='blog_index'),

]
