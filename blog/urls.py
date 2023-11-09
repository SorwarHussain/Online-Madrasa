from django.urls import path
from . import views

urlpatterns = [
    path("",views.post,name="blog_post"),
    path("<str:str>",views.post_details,name="blog_post_details"),
   
   
]
