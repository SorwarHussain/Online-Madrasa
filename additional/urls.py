from django.urls import path
from . import views

urlpatterns = [
   path("",views.dashboard_fu,name="dashboard"),  
   path("permission",views.permission_fu,name="permission"), 
   path("my-courses",views.mycourses,name="mycourses"), 
]


 