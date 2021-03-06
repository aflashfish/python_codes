"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views

# 对于显示静态文件非常重要
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^tinymce/', include('tinymce.urls')),
    path('', blog_views.index, name='index'),
    path('blog/', include("blog.urls")),
    path('article/', include("article.urls")),
    path(r'accounts/', include('users.urls')),
    path(r'picture/', include('picture.urls')),
    path(r'board/', include('board.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
