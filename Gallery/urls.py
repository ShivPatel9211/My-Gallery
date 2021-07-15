from django.urls import path
from . import views


# app_name = "fileapp"

urlpatterns = [
    
    path("",views.home,name="home"),
    path("upload",views.upload,name="upload"),
    path("viewPhoto/<int:id>",views.viewPhoto,name="viewPhoto"),
    path("rotateleft/<int:id>",views.rotateleft,name="rotateleft"),
    path("rotateright/<int:id>",views.rotateright,name="rotateright"),
    path("category/<int:id>",views.category,name="category"),

]