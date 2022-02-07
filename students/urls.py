from . import views
from django.urls import path

urlpatterns=[
    path('register/', views.StudentRegistrationView.as_view(),name='student_registration'),
    path('enroll-course/',views.StudentEnrollCourseView.as_view(),name='student_enroll_course'),
    path('courses/', views.student_course_list_view, name='student_course_list' ),
    path('course/<pk>/',views.StudentCourseDetailView.as_view(),name='student_course_detail'),   
    path('course/<course_id>/<module_id>/<content_id>/', views.student_module_detail, name='student_module_detail'),


]