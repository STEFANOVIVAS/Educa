from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import CourseEnrollForm
from courses.models import Course,Module
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


class StudentCourseDetailView(DetailView):
    model = Course
    template_name = 'students/course/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get course object
        course = self.get_object()
        # get first module
        module=course.modules.all()[0]
        context['module'] = module
        context['content']=module.contents.all()[0]
        return context

def student_module_detail(request,course_id,module_id, content_id):
    course=Course.objects.get(id=course_id)
    module=course.modules.get(id=module_id)
    content=module.contents.get(id=content_id)
    return render(request,'students/course/detail.html', {'content': content,'course':course, 'module':module})
    #refatorar função