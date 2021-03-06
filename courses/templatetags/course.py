from django import template
from ..models import Subject, Course
from django.contrib.auth.models import User


register = template.Library()


@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None


@register.filter(name='is_enrolled')
def is_enrolled(user, course):
    return user.courses_joined.filter(title=course).exists()


@register.simple_tag
def total_subjects():
    return Subject.objects.all()


@register.simple_tag
def total_courses(subject=None):
    courses = Course.objects.all()
    if subject:
        courses = Course.objects.filter(subject__title=subject)
    return courses

@register.simple_tag
def total_contents(course_obj):
    total_contents=0
    course=Course.objects.get(title=course_obj)
    for module in course.modules.all():
        total_contents=module.contents.count()
    return total_contents


@register.simple_tag
def all_users(email):
    user=User.objects.extra(where=["email=email"])
    if user:
        return True
    else:
        return False