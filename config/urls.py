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
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from ckeditor_uploader import views as ckeditor_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("apps.institute.urls")),
    path('',include("apps.student.urls")),
    path('',include("apps.skill.urls")),
    path('faculties/',include("apps.facultet.urls")),
    path('departments/',include('apps.department.urls')),
     path('ckeditor/', include('ckeditor_uploader.urls')),
    path('upload/', ckeditor_views.upload, name='ckeditor_upload'),
    path('browse/', ckeditor_views.browse, name='ckeditor_browse'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)