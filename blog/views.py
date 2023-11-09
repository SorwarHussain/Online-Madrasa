from django.shortcuts import render
from .models import *
# Create your views here.
def post(request):
    blog=Blog.objects.all()
    context={
        'blog':blog
    }
    #print(blog)
    return render(request,'blog/wrap.html',context)
    
def post_details(request,str):
    blog=Blog.objects.get(title=str)
    context={
        'blog':blog
    }
    print(blog)
    return render(request,'blog/wrap_details.html',context)