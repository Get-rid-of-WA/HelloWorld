from django.test import TestCase

from django.urls import reverse, resolve

# Create your tests here.
class ServerProjectTest(TestCase):
    def setUp(self):
        url = reverse('indexServerProject')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)