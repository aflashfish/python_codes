import time
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .models import AddArticle, AddArticle2


# Create your views here.
class AddArticleView(View):

    def get(self, request):
        return render(request, "add_article.html")

    def post(self, request):
        data = AddArticle()
        data.title = request.POST.get("title")
        data.author = "测试作者"
        data.part = "测试类"
        data.public_time = time.strftime('%Y-%m-%d %H:%M:%S.000000', time.localtime(time.time()))
        data.read_num = "100"
        data.comment_num = "12"
        data.body = request.POST.get("body")
        data.save()
        return redirect(reverse('index'))


def article_detail(request, id):
    # 取出相应的文章
    article = AddArticle.objects.get(id=id)
    # 需要传递给模板的对象
    context = {'article': article}
    # print(context)
    # 载入模板，并返回context对象
    return render(request, 'article_detail.html', context)


def article2_detail(request, id):
    article = AddArticle2.objects.get(id=id)
    context = {'article': article}
    # print(article.body)
    # 载入模板，并返回context对象
    return render(request, 'article_detail.html', context)


def post_list(request):
    article = AddArticle2.objects.all().order_by('-public_time')
    context = {'articles': article}
    return render(request, 'post_list.html', context)

