from django.urls import path

from .views import (ITILPTK, About, CafedraList, CenterList, CenterDetail, FakultetList, Home, FakultetDetail,
                    Management, PostDetail, PostList, SiteMap, StateSymbol,
                    Vacansy, Vacansycard, CafedraDetail,DepartmentList,DepartmentDetail)

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("post/<int:pk>/", PostDetail.as_view(), name='post_detail'),
    path("posts", PostList.as_view(), name="posts"),
    path('facultet/', FakultetList.as_view(), name="fakultetlar"),
    path('facultet/<int:pk>', FakultetDetail.as_view(), name="fakultet_detail"),
    path('management/', Management.as_view(), name="management"),
    path('cafedra/', CafedraList.as_view(), name="cafedra"),
    path('cafedra/<int:pk>/', CafedraDetail.as_view(), name='cafedra_detail'),
    path('center/', CenterList.as_view(), name="center"),
    path('center/<int:pk>', CenterDetail.as_view(), name="center_detail"),
    path('department/', DepartmentList.as_view(), name="departments"),
    path('department/<int:pk>', DepartmentDetail.as_view(), name="department_detail"),
    path('about/', About.as_view(), name='about'),
    path('state_symbol/', StateSymbol.as_view(), name="state_symbol"),
    path('vacansy/', Vacansy.as_view(), name='vacansy'),
    path('vacansycard/', Vacansycard.as_view(), name='vacansycard'),
    path('sitemap/', SiteMap.as_view(), name='sitemap')
]
