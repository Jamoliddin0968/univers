from django.shortcuts import render

from django.views.generic import DetailView
from .models import Page

class PageDetail(DetailView):
    template_name = "skill/page_detail.html"
    model = Page
