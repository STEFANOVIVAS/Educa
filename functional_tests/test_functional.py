from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from courses.models import Subject, Course
from accounts.models import Profile


class TestListCourses(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_main_title_is_displayed_index_page(self):
        '''
        Test if main title is showed for users

        '''
        self.browser.get(self.live_server_url + '/')
        title = self.browser.find_element(
            By.ID, 'title-courses')
        self.assertEquals(title.find_element(
            By.TAG_NAME, 'h3').text, 'Expand your carrer job oportunities with this courses')

    def test_list_all_courses_from_culinary_subject_box(self):
        '''
        Test if user find all courses from culinary box-subject link

        '''
        self.browser.get(self.live_server_url + '/')
        time.sleep(3)
        subject_url = self.live_server_url + \
            reverse('course_list_subject', kwargs={'subject': 'culinary'})
        subject = self.browser.find_element(By.CLASS_NAME, 'culinary')
        self.assertEquals(subject.find_element(
            By.TAG_NAME, 'a').text, 'Culinary')
        # Subject culinary link click
        self.browser.find_element(
            By.XPATH, '//div[@class="col-md-4 subject-box culinary"]//a').click()

        self.assertEquals(self.browser.current_url, subject_url)


class TestEnrollCourses(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        user1 = User.objects.create_user(
            'johnsilver', '756237')

        user2 = User.objects.create_user('stefanovivas', '6dejhb3')

        user1.save()
        user2.save()

        authenticate(
            username='johnsilver', password='756237')
        self.browser.get(self.live_server_url + '/')
        subject = Subject.objects.create(
            title='Software development', slug='software-development')
        Course.objects.create(
            owner=user1, subject=subject, title='Data structures', slug='data-structures', overview='')

    def tearDown(self):
        self.browser.quit()

    def test_user_list_software_development_courses_from_dropdown_menu(self):
        self.browser.get(self.live_server_url + '/')
        self.browser.maximize_window()
        time.sleep(3)
        subject_url = self.live_server_url + \
            reverse('course_list_subject', kwargs={
                    'subject': 'software-development'})
        self.browser.find_element(
            By.XPATH, "//a[@class='nav-link dropdown-toggle']").click()
        time.sleep(2)
        self.browser.find_element(
            By.XPATH, "//ul[@class='dropdown-menu subjects show']//li[1]//a").click()
        self.assertEquals(self.browser.current_url, subject_url)

    def test_user_enroll_course_web_development_from_dropdown_menu(self):
        self.browser.get(self.live_server_url + reverse('course_list_subject', kwargs={
            'subject': 'software-development'}))
        self.browser.find_element(
            By.XPATH, "//div[@class='module']//p[1]/a").click()

        time.sleep(5)
        self.browser.find_element(By.CLASS_NAME, 'button').click()
        time.sleep(5)

    # def test_user_create_course(self):
    #     pass

    # def test_user_access_course_already_enrolled(self):
    #     pass
