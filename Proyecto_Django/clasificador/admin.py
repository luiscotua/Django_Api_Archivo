from django.contrib import admin
from .models import Clasificar

# Register your models here.
class Clasifica (admin.ModelAdmin):

    list_display = ['fileid','fileName','fileUpload','dateC','dateU']
    class Meta:
	     model = Clasificar

admin.site.register(Clasificar, Clasifica)