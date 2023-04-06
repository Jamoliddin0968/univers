from django.urls import path
from .views import Bachelor,ExamSchedule,LessonTableBachelor,Masters
urlpatterns = [
    path('bachelor/',Bachelor.as_view(),name='bachelor'),
    path('examschedule/',ExamSchedule.as_view(),name='examschedule'),
    path('lesson_table_bachelor/',LessonTableBachelor.as_view(),name='lesson_table_bachelor'),
    path('masters/',Masters.as_view(),name='masters'),
]
