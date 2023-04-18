from django.urls import path
from .views import PageDetail
urlpatterns = [
    path('<int:pk>/',PageDetail.as_view(),name='skill_page_detail'),
   
]
