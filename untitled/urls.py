"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from cms_dj import views as views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^add/$',views.add,name = 'add'),
    url(r'^add2/(\d+)/(\d+)/$',views.add2,name = 'add2'),
    url(r'^test',views.test,name='test'),
    url(r'^hello',views.test_render,name = 'test_render'),
    url(r'^home',views.home,name = 'home'),
    url(r'^login',views.login,name = 'login'),
    url(r'^search',views.search,name = 'search'),
    #url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^uploadFile',views.upload_file,name = 'upload'),
    url(r'^show',views.show,name = 'show'),
    url(r'^search_sw',views.search_sw,name = 'show'),

]
