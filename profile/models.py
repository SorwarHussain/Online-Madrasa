from django.db import models
from django.contrib.auth.models import User
#from checkout.models import *
# Create your models here.
GENDER = (
    ("man", "man"),
    ("women", "women"),
)
LEVEL=(
    ("All Levels","All Levels"),
    ("Beginner","Beginner"),
     ("Intermediate","Intermediate"),
    ("Expert","Expert"),   
)
class Instructor(models.Model):
    name=models.CharField(max_length=100)
    title= models.CharField(max_length = 200,default="")
    gender=models.CharField(max_length = 20,choices =GENDER,default = 'man')
    instructor_resume=models.TextField()
    def __str__(self):
        return self.name
class Audience(models.Model):
    point=models.CharField(max_length=700)
    def __str__(self):
        return self.point
#class Content(models.Model):
    #title=models.CharField(max_length=100)
        
class Course(models.Model):
    title = models.CharField(max_length = 200)
    slug=models.CharField(max_length=100,default="")
    fee=models.IntegerField()
    level=models.CharField(max_length = 20,choices =LEVEL,default = 'All Levels')
    duration=models.CharField(max_length = 20,default='10h 20m')
    enroled=models.IntegerField(default=10)
    instructor = models.ManyToManyField(Instructor)
    aboutCourse=models.TextField()
    link=models.CharField(max_length = 400,default='https://us04web.zoom.us/j/79969674890?pwd=zpll6laDg59zwfwUSPbTYPZnIVfACS.1')
    audience=models.ManyToManyField(Audience)
    last_modified = models.DateTimeField(auto_now_add = True)
    img = models.ImageField(upload_to = "static/media/")
    #video=models.ManyToManyField(Video)
    #content=models.ForeignKey(Content, on_delete=models.CASCADE, blank=False, null=True)
    def __str__(self):
        return self.title

class Content(models.Model):
    title=models.CharField(max_length=100)
    course=models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    #videos=models.ManyToManyField(Video)

    def __str__(self):
        return self.title
class Video(models.Model):
    caption=models.CharField(max_length=100)
    slug=models.CharField(max_length=100,default="")
    video=models.FileField(upload_to = "video/%y")
    length=models.IntegerField()
    term=models.CharField(max_length = 20,default='3h 20m')
    content=models.ForeignKey(Content, on_delete=models.CASCADE, blank=False, null=True)
    course=models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=True)
    def save(self, *args, **kwargs):
        if self.length >= 60:
            self.term = str(int(self.length/60))+"h "+str(int(self.length%60))+"m"
        else:
            self.term = str(self.length)+"m"
        super(Video, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.caption) + " : "+ str(self.term)

class UserCourse(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)
    course=models.ForeignKey(Course, on_delete=models.CASCADE, blank=False, null=True)
    paid=models.BooleanField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    #checkout=models.ForeignKey(Checkout, on_delete=models.CASCADE, blank=False, null=True)
    def __str__(self):
        return self.user.first_name+" - " +self.course.title