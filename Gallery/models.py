from django.db import models
class Category(models.Model):
    cat=models.CharField(max_length=50)

class myuploadfile(models.Model):
    f_name = models.ForeignKey(Category,on_delete=models.CASCADE)
    myfiles = models.FileField(upload_to="")


