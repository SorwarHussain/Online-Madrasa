from django.shortcuts import render,redirect

from profile.models import *
from .models import *
from django.contrib import messages
# Create your views here.
def checkout_fu(request,str):
    course=Course.objects.get(slug=str)
    user=request.user
    if course.fee==0:
       course=UserCourse(
        user=request.user,
        course=course,
       )
       course.save()
       return redirect('home')
    else:
      if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST['number']
            
        bkashn=request.POST['bkashn']
        bkashid=request.POST['bkashid']
        rocketn=request.POST['rocketn']
        rocketid=request.POST['rocketid']
        nagadn=request.POST['nagadn']
        nagadid=request.POST['nagadid']
       
        Checkoutdata=Checkout(cuser=user,course=course,cname=name,cemail=email,cnumber=number,cBkashNumber=bkashn,cBkashTransactionID=bkashid,cRocketNumber=rocketn,cRocketTransactionID=rocketid,cNagadNumber=nagadn,cNagadTransactionID=nagadid)
       
        Checkoutdata.save()
        messages.success(request,"আপনার আবেদন সম্পন্ন হয়েছে")
        return redirect('home')
    #print(course,course.fee)
    context={
      'user':user,
      'course':course
    }
    return render(request,'checkout/wrap.html',context)
