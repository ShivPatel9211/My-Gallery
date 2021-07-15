from django.db import models

class myuploadfile(models.Model):
    f_name = models.CharField(max_length=255)
    myfiles = models.FileField(upload_to="")

    def __str__(self):
        return self.f_name

