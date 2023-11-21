from django.contrib import admin
from .models import *

# Register your models here.
class SignupData(admin.ModelAdmin):
    #ordering=['id']
    list_display=['id','firstname','email']

class notesAdmin(admin.ModelAdmin):
    list_display=['title','option','file','comment']



admin.site.register(signup,SignupData)
admin.site.register(notes,notesAdmin)