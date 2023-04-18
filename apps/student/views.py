from django.shortcuts import render
from django.views.generic import TemplateView,DetailView

from .models import Page
class PageDetail(DetailView):
    model = Page
    template_name = "student/page_detail.html"