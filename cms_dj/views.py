from django.shortcuts import render
from django.http import HttpResponse #引入response包，相当于python的print，不过是输出到网页
from django.http import  HttpRequest as request
from django.views.decorators.csrf import csrf_exempt
from cms_dj.models import cms_dj_login
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
import os
import datetime
from django.core import serializers
from cms_dj import models
# coding:utf-8
# Create your views here.


def index(request): #定义了一个index函数，第一个参数必须是request，处理网页发送过来的请求
    return render(request,'login.html') #函数返回值

def add(request):
    a = request.GET.get('a',0)
    b = request.GET.get('b',0)
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    c = int(a)+int(b)
    return HttpResponse(str(c))

def test(request):
    return render(request,'home.html')

def test_render(request):
    string = u'喝了咯'
    return render(request,'home.html',{'string' : string})

def home(request):
    TutorialList = ['html','css','jquery','python','django']
    return render(request,'home.html',{'TutorialList':TutorialList})

def home2(request):
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    return render(request,'home.html',{'info_dict': info_dict})

@csrf_exempt
def login(request):
    print (request.method)
    cms_dj_username = request.POST.get('logname')
    print(cms_dj_username)
    request.session['username'] = cms_dj_username
    cms_dj_password = request.POST.get('logpass')
    print(cms_dj_password)
    #return HttpResponse('hello world')
    try:
        user = cms_dj_login.objects.get(cms_dj_username__iexact = cms_dj_username)
        if user:
            if user.cms_dj_password == cms_dj_password:
                #return artical(request)
                #return HttpResponse('登陆成功')
                return show(request)
            else:
                return HttpResponse('登录失败')
        else:
            return HttpResponse('账号不存在')
    except Exception as e:
        print(e)
    return cms_dj_username

def artical(request):
    return render(request,'search.html')

@csrf_exempt
def upload_file(request):
    if request.session['username'] == None and request.session['username'] == '':
        return HttpResponse('请先登录')
    else:
        url = request.POST.get('url')
        tag = request.POST.get('tag')
        tag_special = request.POST.get('tag_special')
        # cms_dj_url = request.POST.get('u')
        # models.cms_dj_artical.objects.create(cms_dj_url=url,cms_dj_tag=tag,cms_dj_addtime=datetime.datetime.now().strftime('%Y-%m-%d'),cms_dj_author=123)
        if request.method == "POST":  # 请求方法为POST时，进行处理
            myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
            if not myFile:
                return HttpResponse("no files for upload!")
            destination = open(os.path.join("F:\\untitled\\static\\img", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
            print(myFile.name)
            for chunk in myFile.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()
            models.cms_dj_artical.objects.create(cms_dj_url=url, cms_dj_tag=tag,
                                                 cms_dj_addtime=datetime.datetime.now().strftime('%Y-%m-%d'),
                                                 cms_dj_author=request.session.get('username', None),
                                                 cms_dj_imgsrc="../../static/img/" + myFile.name,
                                                 cms_dj_tag_special=tag_special)
            return HttpResponse("upload over!")
        return HttpResponse("upload over!")


@csrf_exempt
def show(request):
    #print(request.session['username'])
    if request.session['username'] == None and request.session['username'] == '':
        return HttpResponse('请先登录')
    else:
        ...
        # src = models.cms_dj_artical.objects.values_list('cms_dj_tag', flat=True).filter(id=0)
        # return render(request,'show.html',src)
        # src_list = models.cms_dj_artical.objects.values_list('cms_dj_tag', flat=True).filter(id=0)
        ...#可以删掉
        model_list = models.cms_dj_artical.objects.all()
        # return render(request,'show.html',{'model_list':model_list})
        return render(request, 'index.html', {'model_list': model_list})


def page_not_found(request):
    return render('404.html')

@csrf_exempt
def search(request):
    #tag = 'admin'
    tag = request.GET.get('search')
    print(tag)
    #search_result = models.cms_dj_artical.objects.filter(cms_dj_tag=tag).values_list().all() #直接返回结果集 不是json格式
    search_result = models.cms_dj_artical.objects.filter(cms_dj_tag=tag)
    print(search_result)
    json_data = serializers.serialize('json',search_result)
    #return render(request,'search_result.html',{'search_result': search_result})#渲染结果集到前端页面
    print(json_data)
    return HttpResponse(json_data)
    #pass
    #return HttpResponse(search_list)

@csrf_exempt
def search_sw(request):
    return render(request,'search.html')