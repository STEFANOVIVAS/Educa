from django import template
from ..models import Subject,Course


register=template.Library()

@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None

@register.filter(name='is_enrolled')
def is_enrolled(user,course):
    return user.courses_joined.filter(title=course).exists()

@register.simple_tag
def total_subjects():
    return Subject.objects.all()
               
@register.simple_tag
def total_courses(subject=None):
    courses=Course.objects.all()
    if subject:
        courses=Course.objects.filter(subject__title=subject)
    return courses
    