from apps.institute.models import Category

def get_student_pages(request):
    
    lst = Category.objects.all()
    
    return {
        "categories":lst,
    }
    