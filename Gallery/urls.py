from django.urls import path
from . import views


# app_name = "fileapp"

urlpatterns = [
    
    path("",views.home,name="home"),
    path("upload",views.upload,name="uploads"),

]