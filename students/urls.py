from . import views
from django.urls import path

urlpatterns=[
    path('register/', views.StudentRegistrationView.as_view(),name='student_registration'),
    path('enroll-course/',views.StudentEnrollCourseView.as_view(),name='student_enroll_course'),


]