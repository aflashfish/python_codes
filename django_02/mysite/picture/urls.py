from django.urls import re_path, path
from . import views

app_name = 'picture'

urlpatterns = [

    # 展示所有图片
    re_path(r'^pic/pic_list', views.PicList.as_view(), name='pic_list'),
    # 上传图片
    re_path(r'^pic/upload/$',
            views.PicUpload.as_view(), name='pic_upload'),
    # 展示图片
    re_path(r'^pic/(?P<pk>\d+)/$',
            views.PicDetail.as_view(), name='pic_detail'),

    # 展示所有图
    re_path(r'^pic/showPictures/$', views.showPictures, name='show_pics')

]
