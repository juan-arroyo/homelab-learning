# Basic tests for the django-cicd practice project
from django.test import TestCase, Client

class HomeViewTest(TestCase):

    def setUp(self):
        # Create a test client to simulate HTTP requests
        self.client = Client()

    def test_home_returns_200(self):
        # Verify the home page returns HTTP 200 OK
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_contains_expected_text(self):
        # Verify the response contains expected content
        response = self.client.get('/')
        self.assertContains(response, 'Django CI/CD')