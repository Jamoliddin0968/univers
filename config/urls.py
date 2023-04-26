"""
asosiy url
"""
from ckeditor_uploader import views as ckeditor_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from filebrowser.sites import site

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("institute.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("upload/", ckeditor_views.upload, name="ckeditor_upload"),
    path("browse/", ckeditor_views.browse, name="ckeditor_browse"),
    path("grappelli/", include("grappelli.urls")),  # grappelli URLS
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
