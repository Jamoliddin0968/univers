from django.urls import path
from .views import (
    Uzatgf,Uzmms,Uzmtn,Mchi,Mxk,Vchipt
)
urlpatterns = [
    path("uzatgf/",Uzatgf.as_view(),name="uzatgf"),
    path("uzmms/",Uzmms.as_view(),name="uzmms"),
    path("uzmtn/",Uzmtn.as_view(),name="uzmtn"),
    path("mchi/",Mchi.as_view(),name="mchi"),
    path("mxk/",Mxk.as_view(),name="mxk"),
    path("vchipt/",Vchipt.as_view(),name="vchipt"),
]
