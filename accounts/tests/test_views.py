from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User


class UserViewTest(TestCase):

    def setUp(self):
        self.user = {


            'first_name': 'first_name',
            'last_name': 'last_name',
            'username': 'username',
            'email': 'email@email.com',
            'password': 'password2!',
            'password2': 'password2!',
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

    def test_login_page_by_logout_name(self):
        response = self.client.get(reverse('logout'))
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

    def test_should_create_new_user(self):
        response = self.client.post(
            reverse('register'), self.user, format='text.html')

        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(email="email@email.com").first())

    def test_shoul_not_use_taken_username(self):
        self.client.post(
            reverse('register'), self.user, format='text.html')
        self.client.post(reverse('register'), {
            'first_name': 'first_name',
            'last_name': 'last_name',
            'username': 'username',
            ' email': 'email2@email.com',
            'password': 'password2!',
            ' password2': 'password2!'
        }, format='text.html')

        self.assertFalse(User.objects.filter(
            email="email2@email.com").exists())

    def test_shoul_not_use_taken_email(self):
        self.client.post(
            reverse('register'), self.user, format='text.html')
        self.client.post(
            reverse('register'), {

                'first_name': 'first_name',
                'last_name': 'last_name',
                'username': 'username5',
                ' email': 'email@email.com',
                'password': 'password2!',
                ' password2': 'password2!',

            }, format='text.html')

        self.assertFalse(User.objects.filter(username="username1").exists())

    def test_shoul_not_use_unmatching_passwords(self):
        self.client.post(
            reverse('register'), self.user, format='text.html')
        self.client.post(
            reverse('register'), {

                'first_name': 'first_name',
                'last_name': 'last_name',
                'username': 'username5',
                ' email': 'email3@email.com',
                'password': 'password2!',
                ' password2': 'password2!x',

            }, format='text.html')

        self.assertFalse(User.objects.filter(username="username5").exists())

    def test_should_login_successfully(self):
        self.client.post(
            reverse('register'), self.user, format='text.html')
        response = self.client.post(
            reverse('login'), {
                'username': self.user['username'],
                'password': self.user['password'],

            }, format='text.html')

        self.assertEqual(response.status_code, 302)

    def test_not_should_login_wrong_credentials(self):
        self.client.post(
            reverse('register'), self.user, format='text.html')
        response = self.client.post(
            reverse('login'), {
                'username': self.user['username'],
                'password': self.user['email'],

            }, format='text.html')

        self.assertNotEqual(response.status_code, 302)

    def test_should_logout_successfully(self):
        self.client.post(
            reverse('register'), self.user, format='text.html')

        self.client.login(
            username=self.user['username'], password=self.user['password'])
        self.client.post(
            reverse('login'), {
                'username': self.user['username'],
                'password': self.user['password'],

            }, format='text.html')

        response = self.client.post(
            reverse('logout'))

        self.assertEqual(response.status_code, 302)
