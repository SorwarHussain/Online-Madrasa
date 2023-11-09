from django.urls import path
from . import views

urlpatterns = [
    path("list",views.list,name="courses_list"), 
    path("free-courses",views.free_courses,name="free_courses"),
    path("paid-courses",views.paid_courses,name="paid_courses"), 
    path("instructors",views.instructors,name="instructors"), 
    path("instructors/<str:str>",views.ustaz,name="ustaz"), 
    path("<str:str>",views.course_details,name="course_details"),
    path("<str:str>/dars/<str:str1>",views.course_lecture,name="course_lecture"),
    
    
]


 