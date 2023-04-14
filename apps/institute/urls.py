from django.urls import path

from .views import (ITILPTK, About, Cafedra, Center, Dik, Faculty, Home,
                    Management, SiteMap, StateSymbol, Vacansy, Vacansycard,PostDetail)

urlpatterns = [
    path("",Home.as_view(),name="home"),
    path("post/<int:pk>/",PostDetail.as_view(),name='post_detail'),
    path('faculty/',Faculty.as_view(),name="faculty"),
    path('management/',Management.as_view(),name="management"),
    path('cafedra/',Cafedra.as_view(),name="cafedra"),
    path('cafedra/dik/',Dik.as_view(),name='dik'),
    path('cafedra/itilptk/',ITILPTK.as_view(),name='itilptk'),
    path('center/',Center.as_view(),name="center"),
    path('about/',About.as_view(),name='about'),
    path('state_symbol/',StateSymbol.as_view(),name="state_symbol"),  
    path('vacansy/',Vacansy.as_view(),name='vacansy'),
    path('vacansycard/',Vacansycard.as_view(),name='vacansycard'),
    path('sitemap/',SiteMap.as_view(),name='sitemap')
]
