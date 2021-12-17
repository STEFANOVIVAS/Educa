
from django.test import TestCase
from django.urls import reverse
from courses.models import Subject, Course
from django.contrib.auth.models import User


class StudentRegistrationViewTest(TestCase):
    def setUp(self):
        pass

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/students/register/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('student_registration'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('student_registration'))
        self.assertTemplateUsed(response, 'students/student/registration.html')


class StudentEnrollCourseViewTest(TestCase):
    def setUp(self):
        # Create 3 users:
        test_user1 = User.objects.create_user(
            username='johnsilver', password='756237')
        test_user2 = User.objects.create_user(
            username='stefanovivas', password='4E7FBG7')
        test_user3 = User.objects.create_user(
            username='raquelmachado', password='RF04NKFS')

        test_user1.save()
        test_user2.save()
        test_user3.save()

        # Create a Subject
        test_subject = Subject.objects.create(
            title='Web developer', slug='web-developer')
        # Create a course
        Course.objects.create(
            owner=test_user3, subject=test_subject, title='HTTP method', slug='HTTP-method', overview='')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('student_enroll_course'))

        self.assertRedirects(
            response, '/accounts/login/?next=/students/enroll-course/')
