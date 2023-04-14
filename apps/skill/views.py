from django.shortcuts import render

from django.views.generic import TemplateView

class OTMRating(TemplateView):
    template_name = "skill/otmreyting.html"

class Demand(TemplateView):
    template_name = "skill/talablar.html"    
    
