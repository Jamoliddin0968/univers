from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget


from django.db import models
from .models import Page
class PageAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget},
    }
    
admin.site.register(Page,PageAdmin)