from django.urls import path
from . import views

urlpatterns = [
    path("<str:str>",views.checkout_fu,name="checkout"),
]


 