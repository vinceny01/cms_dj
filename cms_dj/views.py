from django.shortcuts import render
from django.http import HttpResponse #引入response包，相当于python的print，不过是输出到网页
from django.http import  HttpRequest as request
from django.views.decorators.csrf import csrf_exempt
from cms_dj.models import cms_dj_login
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
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
    cms_dj_username = request.POST['logname']
    print(cms_dj_username)
    cms_dj_password = request.POST['logpass']
    print(cms_dj_password)
    #return HttpResponse('hello world')
    try:
        user = cms_dj_login.objects.get(cms_dj_username__iexact = cms_dj_username)
        if user:
            if user.cms_dj_password == cms_dj_password:
                #return HttpResponse('登陆成功')
                return artical(request)
            else:
                return HttpResponse('登录失败')
        else:
            return HttpResponse('账号不存在')
    except Exception as e:
        print(e)
    return HttpResponse('hello')

def artical(request):
    return render(request,'index.html')