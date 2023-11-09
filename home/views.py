
from django.shortcuts import render
from requests import request
from profile.models import *

from django.contrib import messages
from django.shortcuts import (get_object_or_404,                   render,HttpResponseRedirect)
# Create your views here.
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User

def home(request):
    course=Course.objects.all()
    freeCourse=Course.objects.filter(fee=0).count()
    paidCourse=course.count()-freeCourse
    instructor=Instructor.objects.all().count()
    UCourse=UserCourse.objects.all()
    UserCourseList=[]
    for x in UCourse:
        UserCourseList.append(x.id)    
    total_student=User.objects.filter(usercourse__in=UserCourseList[:len(UserCourseList)]).distinct().count()
    context={'course':course,
    'freeCourse':freeCourse,
    'paidCourse':paidCourse,
    'instructor':instructor,
    'total_student':total_student
    }
    return render(request,'home.html',context)
def about(request):
    return render(request,'about/about_wrap.html')
def question(request):
    return render(request,'question/question_wrap.html')


def connection(request):
     return render(request,'contact_request/contact_req.html')
def article(request):
    return render(request,'comingsoon/comingsoon_wrap.html')
    
def privacy_policy(request):
    return render(request,'privacy_policy/privacy_policy_wrap.html')
def terms_condition(request):
    return render(request,'terms_condition/terms_condition_wrap.html')