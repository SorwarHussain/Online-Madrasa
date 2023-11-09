from django.shortcuts import render
from profile.models import *
# Create your views here.
def dashboard_fu(request):
    return render(request,'dashboard/1.html')
def permission_fu(request):
    return render(request,'dashboard/2.html')
def mycourses(request):
    mycourse=UserCourse.objects.filter(user=request.user)
    course=Course.objects.all()
    print(mycourse)
    context={
        'mycourse':mycourse,
        'course':course
    }
    return render(request,'courses/wrap.html',context)