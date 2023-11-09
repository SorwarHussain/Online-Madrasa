from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about,name="about"),
    path("question/",views.question,name="question"),
   
    path('article/',views.article,name='article'),
    path("privacy-policy/",views.privacy_policy,name="privacy_policy"),
    path("terms_condition/",views.terms_condition,name="terms_condition"),
]
