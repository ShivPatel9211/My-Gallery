from django.shortcuts import render,redirect,HttpResponse,get_object_or_404 , redirect
from .models import myuploadfile ,Category
from django.core.paginator import Paginator ,EmptyPage , PageNotAnInteger
from django.core.files.base import ContentFile
from PIL import Image 
import numpy as np
# Create your views here.
def upload(request):
    category = Category.objects.all()
    context = {
        'category':category,
    }
    if request.method == "POST" :
        name = request.POST.get("filename")
        myfile = request.FILES.getlist("uploadfiles")
        category=get_object_or_404(Category, cat=name)
        print(category)
        for f in myfile:
            myuploadfile(f_name=category,myfiles=f).save()
        return redirect('home')
    return render(request,'upload.html',context)
    
def home(request):
    category = Category.objects.all()
    photo=myuploadfile.objects.all()
    allphoto = Paginator(photo,8)
    page=request.GET.get("page")
    try:
        photo=allphoto.page(page)
    except PageNotAnInteger:
        photo=allphoto.page(1)
    except EmptyPage:
        photo=allphoto.page(allphoto.num_pages)

    context ={
        'category':category,
        'photo':photo,
    }
    return render(request,'home.html', context)

def viewPhoto(request,id):
    photo = myuploadfile.objects.filter(id =id).first()
    context ={
        'photo':photo,
    }
    return render(request,'view.html',context)

def rotateright(request ,id):
    photo = myuploadfile.objects.get(pk=id)
    image = np.array(Image.open(photo.myfiles.file))
    image = Image.fromarray(np.rot90(image, 3))
    image.save(photo.myfiles.file.name)
    id=id
    return redirect('viewPhoto',id)

def rotateleft(request,id):
    photo = myuploadfile.objects.get(pk=id)
    image = np.array(Image.open(photo.myfiles.file))
    image = Image.fromarray(np.rot90(image))
    image.save(photo.myfiles.file.name)
    id=id
    return redirect('viewPhoto',id)

def category(request,id):
    category =Category.objects.all()
    photo= myuploadfile.objects.filter(f_name=id)
    
    allphoto = Paginator(photo,8)
    page=request.GET.get("page")
    try:
        photo=allphoto.page(page)
    except PageNotAnInteger:
        photo=allphoto.page(1)
    except EmptyPage:
        photo= allphoto.page(allphoto.num_pages)
    context = {
        'photo':photo,
        'category':category,
     }
    return render(request, 'category.html',context)