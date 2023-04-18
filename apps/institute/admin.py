from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django.db import models
from .models import Post,Cafedra,Fakultet,Center,Department
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.models import Group,User
admin.site.unregister((Group,User))
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget},
    }

admin.site.register(Post, PostAdmin)
admin.site.register(Cafedra)
admin.site.register(Fakultet)
admin.site.register(Center)
admin.site.register(Department)
