from django.urls import path
from .views import (
   Department,Mb,Oub,Tsnqb,Xab
)
urlpatterns = [
    path('',Department.as_view(),name="departments"),
    path('mb/',Mb.as_view(),name="mb"),
    path('oub/',Oub.as_view(),name="oub"),
    path('tsnqb/',Tsnqb.as_view(),name="tsnqb"),
    path('xab/',Xab.as_view(),name="xab"),
]
