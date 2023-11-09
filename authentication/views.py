from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth

# Create your views here.
def login(request):
      if request.method=='POST':
        user_name=request.POST['username']
        pass_word=request.POST['password']
        context={
                'user_name':user_name,
                'pass_word':pass_word
        }
        if User.objects.filter(username=user_name).exists():
          user=auth.authenticate(username=user_name,password=pass_word)
          my_user=User.objects.get(username=user_name)
          if user is not None:
             messages.success(request,"Login Successfully!") 
             auth.login(request,user)
             return redirect('home')    
          else:
            messages.error(request,"wrong credentials!. Please try again.")
            return render(request,'authentication/login.html',context)

        else:
            messages.error(request,"No account!")
            return render(request,'authentication/login.html',context)
      else:
       return render(request,'authentication/login.html')
def signup(request):
    if request.method=='POST':
        user_name=request.POST['user_name']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        context={
                'user_name':user_name,
                'pass1':pass1
        }
        if pass1==pass2:
          if User.objects.filter(username=user_name).exists():
               messages.error(request,"This username is already taken.")
               return render(request,'authentication/signup.html',context)
          elif len(pass1)<6 :
                 messages.error(request,"This password is too short. It must contain at least 6 characters.")
                 return render(request,'authentication/signup.html',context)
          else:
            user=User.objects.create_user(username=user_name,password=pass1)
            user.save()
            messages.success(request,"Successfully create your account.")          
            return redirect("login")

            
        else:
             messages.error(request,"Password not matching.")
             return render(request,'authentication/signup.html',context)
       

    else:
     return render(request,'authentication/signup.html')



