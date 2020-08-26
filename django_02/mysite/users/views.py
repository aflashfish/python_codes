from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import auth
from django.views.generic import View
from .forms import RegistrationForm, LoginForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':

        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']

            # 使用内置User自带create_user方法创建用户，不需要使用save()
            user = User.objects.create_user(username=username, password=password, email=email)

            # 如果直接使用objects.create()方法后不需要使用save()
            user_profile = UserProfile(user=user)
            user_profile.save()

            return HttpResponseRedirect("/accounts/login/")

    else:
        form = RegistrationForm()

    return render(request, 'users/registration.html', {'form': form})


class SigninView(View):
    """
    登录
    """

    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = auth.authenticate(username=username, password=password)
            if user:
                request.session['user_id'] = user.id
                # 用cookie保存用户信息
                # response = HttpResponseRedirect('/index/')
                # 将username写入浏览器cookie,失效时间为360秒
                # response.set_cookie('username', username, 3600)
                # return response
                return redirect(reverse('blog:blog_index'))
            else:
                print("用户名或者密码错误")
                # messages.add_message(request, messages.INFO, '用户名或者密码错误')
                messages.info(request, "用户名或者密码错误")
                return redirect(reverse('users:users/login.html'))
        else:
            return render(request, 'users/login.html',
                          {'form': form, 'message': 'Wrong password. Please try again.'})


def userinfo(request, id):
    """
    个人用户信息
    :param request:
    :return:
    """
    user = User.objects.get(id=id)
    context = {'user': user}
    return render(request, 'users/userinfo.html', context)
