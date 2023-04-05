from django.urls import path
from .views import Home,Department,Faculty,Management,Cafedra,Center

urlpatterns = [
    path("",Home.as_view(),name="home"),
    path('department/',Department.as_view(),name="department"),
    path('faculty/',Faculty.as_view(),name="faculty"),
    path('management/',Management.as_view(),name="management"),
    path('cafedra/',Cafedra.as_view(),name="cafedra"),
    path('center/',Center.as_view(),name="center")
    
]
