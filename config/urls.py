"""
asosiy url
"""
from ckeditor_uploader import views as ckeditor_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .utils import set_language

urlpatterns = [
    path("set_language/<str:language>", set_language, name="set-language"),
    path("i18n/", include("django.conf.urls.i18n")),
]
from django.conf.urls.i18n import i18n_patterns

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("", include("institute.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("upload/", ckeditor_views.upload, name="ckeditor_upload"),
    path("browse/", ckeditor_views.browse, name="ckeditor_browse"),
    path("grappelli/", include("grappelli.urls")),  # grappelli URLS
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
