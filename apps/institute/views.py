from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Post,Cafedra,Fakultet,Center,Department


class Home(ListView):
    queryset = Post.objects.all().order_by("-id")[:3]
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cafedras"] = Cafedra.objects.all()
        context['fakultetlar'] = Fakultet.objects.all()
        return context

class PostDetail(DetailView):
    model=Post 
    template_name = "institute/post_detail.html"

class PostList(ListView):
    model=Post
    template_name = "institute/yangiliklar.html"
    

class FakultetList(ListView):
    model = Fakultet
    template_name = "institute/fakultetlar.html"

class FakultetDetail(DetailView):
    model = Fakultet
    template_name = 'institute/fakultet_detail.html'



class CafedraList(ListView):
    model = Cafedra
    template_name = "institute/kafedralar.html"
    
class CafedraDetail(DetailView):
    queryset = Cafedra.objects.all()
    template_name = 'institute/cafedra_detail.html'
    
class Dik(TemplateView):
    template_name = 'institute/dik.html'

class ITILPTK(TemplateView):
    template_name = 'institute/itilptk.html'
    
class ITITFTE(TemplateView):
    template_name = 'institute/ititfte.html'

class CenterList(ListView):
    template_name = "institute/markazlar.html"
    model = Center
    

class CenterDetail(DetailView):
    template_name = "institute/center_detail.html"
    model = Center


class DepartmentList(ListView):
    template_name = "institute/bolimlar.html"
    model = Department
    

class DepartmentDetail(DetailView):
    template_name = "institute/bolim_detail.html"
    model = Department


# -----------------------------------------------------------------

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

class Management(TemplateView):
    template_name = "institute/rahbariat.html"
