from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import CourseEnrollForm
from courses.models import Course
from django.contrib.auth.decorators import login_required
from students.forms import CourseEnrollForm
from django.views.generic.detail import DetailView
# Create your views here.


class StudentRegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_course_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password1'])
        login(self.request, user)
        return result


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('student_course_detail', args=[self.course.id])


@login_required
def student_course_list_view(request):
    courses = Course.objects.filter(students__in=[request.user])
    return render(request, 'students/course/list.html', {'courses': courses})


@login_required
def student_course_detail_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    modules = course.modules.all()
    return render(request, 'students/course/detail.html', {'course': course, 'modules': modules})


@login_required
def student_course_detail_module(request, course_id, module_id):
    course = get_object_or_404(Course, id=course_id)
    module = course.modules.get(id=module_id)
    return render(request, 'students/course/detail.html', {'course': course, 'module': module})
