from django.test import TestCase
from django.urls import reverse
from courses.models import Course, Subject, Module
from django.contrib.auth.models import User, Permission


class CourseListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            'johnsilver', '756237')
        subject = Subject.objects.create(
            title='Web developer', slug='web-developer')
        Course.objects.create(
            owner=user.profile, subject=subject, title='HTTP method', slug='HTTP-method', overview='')

    def test_view_url_exists_at_desired_location_courseList(self):
        subject = Subject.objects.get(id=1)
        response = self.client.get(f'/course/subject/{subject.slug}/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name_courseList(self):
        subject = Subject.objects.get(id=1)
        slug = subject.slug
        response = self.client.get(
            reverse('course_list_subject', kwargs={'subject': slug}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template_courseList(self):
        subject = Subject.objects.get(id=1)
        slug = subject.slug
        response = self.client.get(
            reverse('course_list_subject', kwargs={'subject': slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/course/list.html')


class ManageCourseListViewTest(TestCase):

    def setUp(self):

        test_user1 = User.objects.create_user(
            username='johnsilver', password='71RS56237')
        test_user2 = User.objects.create_user(
            username='stefanovivas', password='ABidnk223')

        test_user1.save()
        test_user2.save()

    def test_view_url_exists_at_desired_location_manage_course(self):
        response = self.client.get('/course/dashboard/')
        self.assertEquals(response.status_code, 302)

    def test_redirect_if_not_logged_in_manage_course(self):
        response = self.client.get(reverse('manage_course_list'))
        self.assertRedirects(
            response, '/accounts/login/?next=/course/dashboard/')

    def test_logged_in_but_without_permission_manage_course(self):

        self.client.login(username='johnsilver', password='71RS56237')
        response = self.client.get(reverse('manage_course_list'))
        # Check that we got a response "Forbidden"
        self.assertEqual(response.status_code, 403)

    def test_logged_in_with_permission_manage_course(self):
        user1 = User.objects.get(id=1)

        # creating view permission
        view_permission = Permission.objects.get(
            name__icontains='view course')

        # Applying permission to user
        user1.user_permissions.add(view_permission)

        self.client.login(username='johnsilver', password='71RS56237')
        response = self.client.get(reverse('manage_course_list'))
        
        
        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'johnsilver')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(
            response, 'courses/manage/course/list.html')


class CourseCreateViewTest(TestCase):
    def setUp(self):

        test_user1 = User.objects.create_user(
            username='johnsilver', password='71RS56237')
        test_user2 = User.objects.create_user(
            username='stefanovivas', password='ABidnk223')

        test_user1.save()
        test_user2.save()

    def test_view_url_exists_at_desired_location_course_create(self):
        response = self.client.get('/course/create/')
        self.assertEquals(response.status_code, 302)

    def test_view_url_accessible_by_name_course_create(self):
        response = self.client.get(reverse('course_create'))
        self.assertEquals(response.status_code, 302)

    def test_logged_in_but_without_permission_course_create(self):
        self.client.login(username='johnsilver', password='71RS56237')
        response = self.client.get(reverse('course_create'))

        # Check that we got a response "Forbidden"
        self.assertEqual(response.status_code, 403)

    def test_logged_in_with_permission_course_create(self):
        user1 = User.objects.get(id=1)

        # creating view permission
        view_permission = Permission.objects.get(
            name__icontains='add course')
        
        # Applying permission to user
        user1.user_permissions.add(view_permission)

        self.client.login(username='johnsilver', password='71RS56237')
        response = self.client.get(reverse('course_create'))
        

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'johnsilver')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)


class CourseDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):

        user = User.objects.create_user(
            username='johnsilver', password='756237')

        subject = Subject.objects.create(
            title='Web developer', slug='web-developer')
        Course.objects.create(
            owner=user.profile, subject=subject, title='HTTP method', slug='HTTP-method', overview='')

    def test_view_url_exists_at_desired_location_course_delete(self):
        course = Course.objects.get(id=1)
        response = self.client.get(
            reverse('delete_course', kwargs={'pk': course.pk}))
        self.assertEquals(response.status_code, 302)

    def test_logged_in_but_without_permission_course_delete(self):
        course = Course.objects.get(id=1)
        self.client.login(username='johnsilver', password='756237')
        response = self.client.get(
            reverse('delete_course', kwargs={'pk': course.pk}))
        self.assertEquals(response.status_code, 403)

    def test_logged_in_with_permission_course_delete(self):
        course = Course.objects.get(id=1)
        user = User.objects.get(id=1)
        # Creating view permission
        view_permission = Permission.objects.get(
            name__icontains='delete course')
        user.user_permissions.add(view_permission.id)

        self.client.login(username='johnsilver', password='756237')
        response = self.client.get(
            reverse('delete_course', kwargs={'pk': course.pk}))
        # Verifying if the user is logged in
        self.assertEquals(str(response.context['user']), 'johnsilver')


class CourseDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            'johnsilver', '756237')
        subject = Subject.objects.create(
            title='Web developer', slug='web-developer')
        Course.objects.create(
            owner=user.profile, subject=subject, title='HTTP method', slug='HTTP-method', overview='')

    def test_view_url_accessible_by_name(self):
        course = Course.objects.get(id=1)
        response = self.client.get(
            reverse('course_detail', kwargs={'pk': course.pk}))

        self.assertEquals(response.status_code, 200)


class ModuleContentListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='johnsilver', password='756237')
        test_user.save()

        subject = Subject.objects.create(
            title='Web developer', slug='web-developer')
        course = Course.objects.create(
            owner=test_user.profile, subject=subject, title='HTTP protocol', slug='HTTP-protocol', overview='')
        Module.objects.create(course=course, title='GET method')

    def test_content_list_view_url_accessible_by_name(self):
        login = self.client.login(username='johnsilver', password='756237')
        
        module = Module.objects.get(id=1)
        
        response = self.client.get(
            reverse('module_content_list', kwargs={'module_id': module.id}))

        self.assertEquals(response.status_code, 200)


class ContentCreateUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='johnsilver', password='756237')
        test_user.save()

        subject = Subject.objects.create(
            title='Web developer', slug='web-developer')
        course = Course.objects.create(
            owner=test_user.profile, subject=subject, title='HTTP protocol', slug='HTTP-protocol', overview='')
        Module.objects.create(course=course, title='GET method')

    def test_content_create_view_url_accessible_by_name(self):
        self.client.login(username='johnsilver', password='756237')
        module = Module.objects.get(id=1)

        # Create a text content
        response = self.client.get(
            reverse('module_content_create', kwargs={'module_id': module.id, 'model_name': 'text'}))
        self.assertEquals(response.status_code, 200)
        # Create a video content
        response = self.client.get(
            reverse('module_content_create', kwargs={'module_id': module.id, 'model_name': 'video'}))
        self.assertEquals(response.status_code, 200)
