from django.shortcuts import render
from django.views.generic import TemplateView

class Mchi(TemplateView):
    template_name = 'facultet/mchi.html'

class Mxk(TemplateView):
    template_name = 'facultet/mxk.html'

class Uzatgf(TemplateView):
    template_name = 'facultet/uzatgf.html'

class Uzmms(TemplateView):
    template_name = 'facultet/uzmms.html'

class Uzmtn(TemplateView):
    template_name = 'facultet/uzmtn.html'

class Vchipt(TemplateView):
    template_name = 'facultet/vchipt.html'

