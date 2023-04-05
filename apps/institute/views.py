from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Home(TemplateView):
    template_name = "index.html"
    
class Department(TemplateView):
    template_name = "institute/bolimlar.html"

class Faculty(TemplateView):
    template_name = "institute/fakultetlar.html"

class Management(TemplateView):
    template_name = "institute/rahbariat.html"

class Cafedra(TemplateView):
    template_name = "institute/kafedralar.html"
    
class Center(TemplateView):
    template_name = "institute/markazlar.html"