from django.urls import reverse
from django.test import TestCase


class UserViewTest(TestCase):

    def setUp(self):
        self.user = {

            " first_name ": "first_name",
            "last_name ": "last_name",
            "username": "username",
            "email": "email",
            "password": "password",
            "password2": "password2"
        }

    def test_register_page_status_code(self):
        response = self.client.get('/accounts/register')
        self.assertEqual(response.status_code, 200)

    def test_register_page_by_name(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_register_page_uses_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_login_page_status_code(self):
        response = self.client.get('/accounts/login')
        self.assertEqual(response.status_code, 200)

    def test_login_page_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_uses_correct_template(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_dashboard_page_status_code(self):
        response = self.client.get('/accounts/dashboard')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_page_by_name(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_page_uses_correct_template(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/dashboard.html')
