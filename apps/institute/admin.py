from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.db import models
from mptt.admin import DraggableMPTTAdmin, MPTTModelAdmin

from .models import Cafedra, Category, Center, Department, Fakultet, Page, Post

admin.site.unregister((Group, User))

# --------------------------------------------------------
# from django import forms
# from django.contrib.flatpages.admin import FlatPageAdmin

# from django.contrib.flatpages.models import FlatPage
from django.urls import reverse
from tinymce.widgets import TinyMCE

# admin.site.register(Page, TinyMCEFlatPageAdmin)


# --------------------------------------------------------
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": CKEditorUploadingWidget},
    }


admin.site.register(Post, PostAdmin)
admin.site.register(Cafedra)
admin.site.register(Fakultet)
admin.site.register(Center)
admin.site.register(Department)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "link")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    expand_tree_by_default = True
    # list_display = ('indented_title','is_leaf_node')
