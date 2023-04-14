from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Post


class Home(ListView):
    queryset = Post.objects.all().order_by("-id")[:3]
    template_name = "index.html"

class PostDetail(DetailView):
    model=Post 
    template_name = "institute/post_detail.html"

class Faculty(TemplateView):
    template_name = "institute/fakultetlar.html"


class Management(TemplateView):
    template_name = "institute/rahbariat.html"


class Cafedra(TemplateView):
    template_name = "institute/kafedralar.html"
    
class Dik(TemplateView):
    template_name = 'institute/dik.html'

class ITILPTK(TemplateView):
    template_name = 'institute/itilptk.html'
    
class ITITFTE(TemplateView):
    template_name = 'institute/ititfte.html'

class Center(TemplateView):
    template_name = "institute/markazlar.html"


class About(TemplateView):
    template_name = "institute/haqida.html"


class StateSymbol(TemplateView):
    template_name = "institute/davlat_ramzlari.html"
    

class SiteMap(TemplateView):
    template_name = "saytxaritasi.html"
    
class Vacansy(TemplateView):
    template_name = "vacansy.html"
    
class Vacansycard(TemplateView):
    template_name = "vacansycard.html"
