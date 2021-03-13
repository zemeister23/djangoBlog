from django.shortcuts import render
from  django.http import HttpResponse
from .models import BlogPost

def index(request):
    post_list = BlogPost.objects.all()
    return render(request,"blog_fayllari/index.html",{"blog_list":post_list})

def about(request):
    return render(request,"blog_fayllari/about.html")
