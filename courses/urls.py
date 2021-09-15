
from django.urls import path, include
from . import views


urlpatterns = [
    path('dashboard/', views.ManageCourseListView.as_view(), name='manage_course_list'),
    path('create/', views.CourseCreateView.as_view(), name='course_create'),
    path('<pk>/edit/', views.CourseUpdateView.as_view(), name='update_course'),
    path('<pk>/delete/', views.CourseDeleteView.as_view(), name='delete_course'),

]
