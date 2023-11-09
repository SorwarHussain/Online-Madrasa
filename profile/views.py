from django.shortcuts import render,redirect

from .models import *
from checkout.models import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models import Q
# Create your views here.
#@login_required
def course_details(request,str):
    course=Course.objects.get(slug=str)
    instructor = Instructor.objects.filter(course__slug=str)
    audience=Audience.objects.filter(course__slug=str)
    time_duration=Video.objects.filter(course__slug=str).aggregate(sum=Sum('length'))
    time=time_duration["sum"]
    h=int(time/60)
    m=time%60
    if time>=60:
        duration="{}h {}m"
        duration=duration.format(h,m)
    else:
        duration="{}m"
        duration=duration.format(m)
    if course.duration!=duration:
        course.duration=duration
        course.save()
    if request.user.is_authenticated:
        try:
            check_enrolled=UserCourse.objects.get(user=request.user,course=course)
        except UserCourse.DoesNotExist:
            check_enrolled=None
    else:
        check_enrolled=None
    enrol=course.usercourse_set.all().count()
    if course.enroled!=enrol:
        course.enroled=enrol
        course.save()
    if request.user.is_authenticated:
        try:
            check_enrolled_request=Checkout.objects.get(cuser=request.user,course=course)
        except Checkout.DoesNotExist:
            check_enrolled_request=None
    else:
        check_enrolled_request=None
    context={'course':course,
    'instructor':instructor,
    'audience':audience,
    'check_enrolled':check_enrolled,
    'check_enrolled_request':check_enrolled_request
    }  
    return render(request,'details Course/course.html',context)
def course_lecture(request,str,str1):
    video=Video.objects.get(slug=str1)
    course=Course.objects.get(slug=str)
    context={'course':course,'video':video}  
    return render(request,'course_lecture/course_lecture.html',context)

def list(request):
    course=Course.objects.all()
    context={
        'course':course
    }
    return render(request,'courses/wrap.html',context)
def free_courses(request):
    course=Course.objects.filter(fee=0)
    designation='ফ্রি'
    context={
        'course':course,
        'designation':designation
    }
    return render(request,'courses/wrap.html',context)
def paid_courses(request):
    course=Course.objects.filter(~Q(fee=0))
    designation='পেইড'
    context={
        'course':course,
        'designation':designation
    }
    return render(request,'courses/wrap.html',context)

def instructors(request):
    ustad=Instructor.objects.filter(gender='man')
    ustadi=Instructor.objects.filter(gender='women')
    context={
        'ustad':ustad,
        'ustadi':ustadi
    }  
    return render(request,'instructor/wrap_instructors.html',context)

def ustaz(request,str):
    ustaz=Instructor.objects.get(name=str)
    #print(ustaz.id)
    course=Course.objects.filter(instructor=ustaz.id)
    context={
    'ustaz':ustaz,
    'course':course
    }  
    return render(request,'instructor/wrap.html',context)
