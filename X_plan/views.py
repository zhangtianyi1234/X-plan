#encoding:utf-8

#导入django相关包
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template,Context,RequestContext
from django.shortcuts import render_to_response,redirect

#导入项目相关包

def homepage(request):
    return render_to_response('homepage.html')

def login(request):
    return render_to_response('login.html')

def register(request):
    return render_to_response('register.html')

def globe(request):
    return render_to_response('globe.html')

def listall(request):
    return render_to_response('listall.html')
