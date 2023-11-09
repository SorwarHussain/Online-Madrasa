from django.db import models
from django.contrib.auth.models import User
from profile.models import *
# Create your models here.
class Checkout(models.Model):
    cuser=models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    course=models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    usercourse=models.ForeignKey(UserCourse, on_delete=models.CASCADE, blank=True, null=True)
    cname=models.CharField(max_length=100) #, blank=True,null=True)
    cemail=models.EmailField(max_length=100,blank=True,null=True)
    cnumber=models.CharField(max_length=100)
    #cbiodatano=models.CharField(max_length=100)
    
    #bkash
    cBkashNumber=models.CharField(max_length=200,blank=True,null=True)
    cBkashTransactionID=models.CharField(max_length=200,blank=True,null=True)
    #rocket
    cRocketNumber=models.CharField(max_length=200,blank=True,null=True)
    cRocketTransactionID=models.CharField(max_length=200,blank=True,null=True)
    #nagad
    cNagadNumber=models.CharField(max_length=200,blank=True,null=True)
    cNagadTransactionID=models.CharField(max_length=200,blank=True,null=True)
    #status>>given(done) or not given
    estatus=models.BooleanField(null=True, blank=True)
    def __str__(self):
        return self.cname
