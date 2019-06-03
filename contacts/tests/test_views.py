from django.urls import reverse
from .test_base import BaseTest


class ContactTest(BaseTest):

    def test_contacts_page_status_code(self):
        response = self.client.get('/accounts/dashboard')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/dashboard.html')

    def test_should_create_and_redirect(self):
        self.client.login(username="cryce", password="1234qwerq")
        response = self.client.post(
            reverse('contact'), self.data, format="text/html")
        self.assertEqual(response.status_code, 302)

    def test_should_create_and_redirect_when_user_not_logged_in(self):
        response = self.client.post(
            reverse('contact'), self.data, format="text/html")
        self.assertEqual(response.status_code, 302)

    def test_should_create_and_redirect_when_user_logged_in_twice(self):
        self.client.login(username="cryce", password="1234qwerq")
        self.client.post(
            reverse('contact'), self.data, format="text/html")
        response = self.client.post(
            reverse('contact'), self.data, format="text/html")
        self.assertEqual(response.status_code, 302)
