from django.shortcuts import render
from article.views import AddArticle, AddArticle2


# Create your views here.
def index(request):
    # url中直接访问时，返回首页
    articles = AddArticle.objects.all()
    articles2 = AddArticle2.objects.all()
    context = {'articles': articles,
               'articles2': articles2}
    return render(request, "index.html", context)
