from django.http import HttpResponse
from django.shortcuts import render
import os

def sou(request):
    return HttpResponse('hello')

file_path=os.path.abspath(__file__)
pro_path=os.path.dirname(file_path)
dir_path=os.path.dirname(pro_path)


def html(request):
    file_adress=os.path.join(dir_path,"sample.html")
    fp=open(file_adress,"r")
    data=fp.read()
    return HttpResponse(data)

def rend_demo(request):
    return render(request,"sample.html")

def sam_demo(request):
    return render(request,"sample.html")






