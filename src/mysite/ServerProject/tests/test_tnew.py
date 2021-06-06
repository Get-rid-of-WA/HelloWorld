from django.test import TestCase
from django.urls import reverse

class newServerProjectTest(TestCase):
    def setUp(self):
        url = reverse('tnewServerProject')
        self.response = self.client.get(url)
    
    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_sent_data(self):
        url = reverse('tnewServerProject')
        data = {
            'name': 'fkw',
            'description': '123456',
            'price': 100,
        }
        self.client.post(url, data)
