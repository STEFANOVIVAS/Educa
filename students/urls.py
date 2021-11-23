from . import views
from django.urls import path

urlpatterns=[
    path('register/', views.StudentRegistrationView.as_view(),name='student_registration'),
    path('enroll-course/',views.StudentEnrollCourseView.as_view(),name='student_enroll_course'),
    path('courses/', views.student_course_list_view, name='student_course_list' ),
    path('course/<int:course_id>/', views.student_course_detail_view, name='student_course_detail' ),
    path('course/<int:course_id>/<int:module_id>', views.student_course_detail_module, name='student_course_detail_module' ),


]