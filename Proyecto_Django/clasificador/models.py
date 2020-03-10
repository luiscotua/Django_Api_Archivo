from django.db import models
from django.utils import timezone


# Create your models here.
class Clasificar(models.Model):
    fileid  = models.AutoField(primary_key=True)
    fileName = models.CharField(max_length=20)
    fileUpload = models.FileField(upload_to ='files/')
    dateC = models.DateTimeField('Date Published', auto_now_add=True)
    dateU = models.DateTimeField('Date Update', auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Gestor de Archivos"
    
    def __str__(self):
        return self.fileName