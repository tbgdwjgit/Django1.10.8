__author__ = 'Test-YLL'

# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf

# ����POST��������
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
