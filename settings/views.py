from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from requests import request
# Create your views here.

@login_required
def general(request):
    return render(request,'settings/general/general_wrap.html')
@login_required
def delete_account(request):
    if request.method == 'POST':
        user=User.objects.get(id=request.user.id)
        user.delete()
        messages.success(request,"Your account successfully deleted.")  
        return redirect('home') 
   
    return render(request,'settings/general/confirm_delete_account_wrap.html')
         


    