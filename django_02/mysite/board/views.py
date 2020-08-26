from django.shortcuts import render
import re
from .models import BoardUsers
from django.views.generic import View
import time


class MessageView(View):

    def get(self, request):
        boards = BoardUsers.objects.all()
        context = {'boards': boards}
        return render(request, 'board_message.html', context)

    def post(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
        else:
            ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
        pattern = re.compile(r"\w+Browser|Chrome")
        getmessage = pattern.findall(request.META["HTTP_USER_AGENT"])
        body = request.POST.get("body")
        username = request.POST.get("username")
        email = request.POST.get("email")
        data = BoardUsers()
        data.username = username
        data.email = email
        data.comment = body
        data.ip = ip
        data.created_time = time.strftime('%Y-%m-%d %H:%M:%S.000000', time.localtime(time.time()))
        if getmessage:
            data.ie_browser = getmessage[0]
        data.save()
        return render(request, 'board_message.html')
