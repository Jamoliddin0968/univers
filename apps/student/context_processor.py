from .models import Page
from apps.skill.models import Page as SkillPage
def get_student_pages(request):
    
    lst = Page.objects.all()
    skills = SkillPage.objects.all()
    return {
        "student_pages":lst,
        'skills_page':skills,
    }
    