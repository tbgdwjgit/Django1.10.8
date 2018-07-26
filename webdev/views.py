# -*- coding:utf-8 *-
from django.http import HttpResponse

def first_page(request):
    str = '<B>测试</B>'
    return HttpResponse("<p>世界，你好！！！！</p>" + str)