from django.contrib import admin
from . models import *


admin.site.index_template='memcache_status/admin_index.html'
# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=['title','slug']
    prepopulated_fields={'slug':('title',)}
    
# class ContentInline(admin.StackedInline):
#     model=Content

class ModuleInline(admin.StackedInline):
    model=Module
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['title','subject','created']
    list_filter=['created', 'subject']
    search_fields=['title','overview']
    prepopulated_fields={'slug':('title',)}
    inlines=[ModuleInline]
