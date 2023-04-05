from django.urls import path
from .views import Bachelor
urlpatterns = [
    path('bachelor/',Bachelor.as_view(),name='bachelor'),
]
