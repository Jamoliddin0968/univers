from django.urls import path
from .views import OTMRating,Demand,Dik
urlpatterns = [
    path('otm_rating/',OTMRating.as_view(),name='otm_rating'),
    path('demand/',Demand.as_view(),name='demand'),
    path('dik/',Dik.as_view(),name='dik')
]
