"""ArticleBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from ArticleBlog.views import *
from article.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # 组匹配 两个括号代表姓名和年龄
    # re_path('^example/(\w+)/(\d{1,2})$', example)
    # 命名组匹配 （?P<参数>规则）
    re_path('^example/(?P<name>\w+)/(?P<age>\d{1,2})$', example),
    path('index/', index),
    path('person_info/', person_info),
    path('photos/', photos),
    path('diaries/', diaries),

]
