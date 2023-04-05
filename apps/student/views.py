from django.shortcuts import render
from django.views.generic import TemplateView


class Bachelor(TemplateView):
    template_name = "student/Bakalavriyat.html"
