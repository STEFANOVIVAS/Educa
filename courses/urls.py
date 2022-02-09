
from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.ManageCourseListView.as_view(),
         name='manage_course_list'),
    path('create/', views.CourseCreateView.as_view(), name='course_create'),
    path('<pk>/edit/', views.CourseUpdateView.as_view(), name='update_course'),
    path('<pk>/delete/', views.CourseDeleteView.as_view(), name='delete_course'),
    path('<pk>/module/', views.CourseModuleUpdateView.as_view(),
         name='course_module_update'),
    path('module/<int:module_id>/content/<model_name>/create/',
         views.ContentCreateUpdateView.as_view(), name='module_content_create'),
    path('module/<int:module_id>/content/<model_name>/<id>/',
         views.ContentCreateUpdateView.as_view(), name='module_content_update'),
    path('content/<int:id>/delete/', views.ContentDeleteView.as_view(),
         name='module_content_delete'),
    path('module/<int:module_id>/', views.ModuleContentListView.as_view(),
         name='module_content_list'),
    path('subject/<slug:subject>/', views.CourseListView.as_view(),
         name='course_list_subject'),
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('search/', views.SearchCourseView.as_view(), name='search_course'),

]
