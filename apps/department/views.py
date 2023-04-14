from django.shortcuts import render
from django.views.generic import TemplateView

class Department(TemplateView):
    template_name = "department/bolimlar.html"
    
class Mb(TemplateView):
    template_name = "department/mb.html"

class Oub(TemplateView):
    template_name = "department/oub.html"

class Tsnqb(TemplateView):
    template_name = "department/tsnqb.html"
    
class Xab(TemplateView):
    template_name = "department/xab.html"
