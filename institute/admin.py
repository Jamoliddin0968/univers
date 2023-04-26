from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.contrib.auth.models import Group
from django.db import models
from mptt.admin import DraggableMPTTAdmin, MPTTModelAdmin

from .models import Cafedra, Category, Center, Department, Fakultet, Page, Post, User

admin.site.unregister((Group,))


class SuperAdminModelAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        if request.user.is_authenticated and request.user.is_full_user:  # show for super user anyway
            return True
        return False


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": CKEditorUploadingWidget},
    }

    def has_module_permission(self, request):
        if request.user.is_authenticated and request.user.is_full_user:
            return False
        return True


admin.site.register(Post, PostAdmin)
admin.site.register(Cafedra, SuperAdminModelAdmin)
admin.site.register(Fakultet, SuperAdminModelAdmin)
admin.site.register(Center, SuperAdminModelAdmin)
admin.site.register(Department, SuperAdminModelAdmin)


@admin.register(Page)
class PageAdmin(SuperAdminModelAdmin):
    list_display = ("title", "link")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    expand_tree_by_default = True

    def has_module_permission(self, request):
        if request.user.is_authenticated and request.user.is_full_user:  # show for super user anyway
            return True

        return False
