# -*- coding:utf-8 -*-
from django.http import HttpResponse

def first_page(request):
    str ='"<p><B>世界</B>,你好！</p>"' \
         '"<p><B>世界</B>,你好！</p>"' \
         '"<p><B>世界</B>,你好！</p>"';
    return HttpResponse(str)