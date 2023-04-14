from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget},
    }

admin.site.register(Post, PostAdmin)
