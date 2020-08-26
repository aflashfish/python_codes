from django.urls import re_path, path
from . import views

app_name = 'article'

urlpatterns = [
    re_path(r'add_article/$', views.AddArticleView.as_view(), name='add_article'),
    re_path(r'article_detail/(\d+)/$', views.article_detail, name='article_detail'),
    re_path(r'article2_detail/(\d+)/$', views.article2_detail, name='article2_detail'),
    re_path(r'post_list/$', views.post_list, name='post_list'),
]
