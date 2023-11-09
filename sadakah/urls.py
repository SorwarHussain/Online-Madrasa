from django.urls import path
from . import views

urlpatterns = [
    path("",views.sadakah_func,name="sadakah"),
]


 