from django.test import TestCase
from courses.models import Subject, Course, Module, Content
from django.contrib.auth.models import User


class SubjectModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        Subject.objects.create(title='Web developer', slug='web-developer')

    def test_object_name_is_title(self):
        subject = Subject.objects.get(id=1)
        expected_subject_name = f'{subject.title}'
        self.assertEquals(expected_subject_name, str(subject))


class CourseModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            'johnsilver', '756237')
        subject = Subject.objects.create(
            title='Web developer', slug='web-developer')
        Course.objects.create(
            owner=user.profile, subject=subject, title='HTTP method', slug='HTTP-method', overview='')

    def test_object_name_is_title(self):
        course = Course.objects.get(id=1)
        expected_course_name = f'{course.title}'
        self.assertEquals(expected_course_name, str(course))


class ModuleModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            'johnsilver', '756237')
        subject = Subject.objects.create(
            title='Web developer', slug='web-developer')
        course = Course.objects.create(
            owner=user.profile, subject=subject, title='HTTP method', slug='HTTP-method', overview='')
        Module.objects.create(course=course, title='GET Method')
        Module.objects.create(course=course, title='POST Method')
        Module.objects.create(course=course, title='DELETE Method')

    def test_object_name_is_order_comma_title(self):
        module = Module.objects.get(id=1)
        expected_module_name = f'{module.order}. {module.title}'
        self.assertEquals(expected_module_name, str(module))


class OrderFieldModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            'johnsilver', '756237')
        subject = Subject.objects.create(
            title='Web developer', slug='web-developer')
        course_test_1 = Course.objects.create(
            owner=user.profile, subject=subject, title='HTTP method', slug='HTTP-method', overview='')
        course_test_2 = Course.objects.create(
            owner=user.profile, subject=subject, title='DOM Tree', slug='DOM-Tree', overview='')
        Module.objects.create(course=course_test_1, title='GET Method')
        Module.objects.create(course=course_test_2,
                              title='Searching DOM elements')
        Module.objects.create(course=course_test_1, title='DELETE Method')

    def test_object_custom_field_OrderField_generating_order_automatically(self):
        module_one = Module.objects.get(id=1)
        module_two = Module.objects.get(id=2)
        module_three = Module.objects.get(id=3)
        expect_module_order_course_2 = f'{module_two.order}'
        expect_module_order_course_3 = f'{module_three.order}'
        self.assertEquals(expect_module_order_course_2, '0')
        self.assertEquals(expect_module_order_course_3, '1')
