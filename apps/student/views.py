from django.shortcuts import render
from django.views.generic import TemplateView


class Bachelor(TemplateView):
    template_name = "student/Bakalavriyat.html"

class ExamSchedule(TemplateView):
    template_name = "student/imtihon_jadvali.html"
    
class LessonTableBachelor(TemplateView):
    template_name = "student/dars_jadvali_bakalavr.html"
    
class Masters(TemplateView):
    template_name = "student/magistratura.html"
    

class LessonTableMasters(TemplateView):
    template_name = "student/dars_jadvali_magistratura.html"
    
class CorrespondenceEducation(TemplateView):
    template_name = "student/sirtqi_talim.html"