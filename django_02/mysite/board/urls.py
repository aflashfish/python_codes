from django.urls import re_path, path
from . import views

app_name = 'board'

urlpatterns = [

    # 展示所有图片
    re_path(r'message', views.MessageView.as_view(), name='board_message'),
]