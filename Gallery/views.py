from django.shortcuts import render,redirect,HttpResponse
from . models import myuploadfile
# Create your views here.
def upload(request):
    if request.method == "POST" :
        name = request.POST.get("filename")
        myfile = request.FILES.getlist("uploadfoles")
        
        for f in myfile:
            myuploadfile(f_name=name,myfiles=f).save()
        return redirect('home')
    return render(request,'upload.html')
    
def home(request):
    return HttpResponse("ok")