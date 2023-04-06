from django.urls import path

from .views import (Bachelor, CorrespondenceEducation, ExamSchedule,
                    LessonTableBachelor, LessonTableMasters, Masters)

urlpatterns = [
    path('bachelor/',Bachelor.as_view(),name='bachelor'),
    path('examschedule/',ExamSchedule.as_view(),name='examschedule'),
    path('lesson_table_bachelor/',LessonTableBachelor.as_view(),name='lesson_table_bachelor'),
    path('masters/',Masters.as_view(),name='masters'),
    path('lesson_table_masters/',LessonTableMasters.as_view(),name='lesson_table_masters'),
    path('correspondence_education',CorrespondenceEducation.as_view(),name='correspondence_education'),
]
