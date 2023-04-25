"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from ckeditor_uploader import views as ckeditor_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from filebrowser.sites import site

urlpatterns = [
    path("admin/filebrowser/", site.urls),
    path("admin/", admin.site.urls),
    path("", include("apps.institute.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("upload/", ckeditor_views.upload, name="ckeditor_upload"),
    path("browse/", ckeditor_views.browse, name="ckeditor_browse"),
    path("grappelli/", include("grappelli.urls")),  # grappelli URLS
    path("tinymce/", include("tinymce.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
