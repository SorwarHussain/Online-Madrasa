from django.urls import path
from . import views
urlpatterns = [
   path("general/",views.general,name="general"),
   path("delete-account/",views.delete_account,name="delete_account"),
]