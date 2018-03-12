from django.shortcuts import render
from web.models import Article
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404

# Create your views here.

def Test(request):
    return render(request, 'web/test.html', {'current_time': datetime.now()})

def home(request):
    post_list = Article.objects.all() # 获取全部的Article对象
    return render(request, 'web/home.html', {'post_list': post_list})

def Detail(request,id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'web/post.html',{'post':post})

def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")
