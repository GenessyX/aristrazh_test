from rest_framework import status
from django.test import TestCase, Client
from url_parser.models import Ticket
from rest_framework.test import APIClient, APIRequestFactory

# initialize the APIClient app
client = Client()
factory = APIRequestFactory()
client = APIClient()

class ApiTest(TestCase):
    def setUp(self):
        self.ticket = Ticket.objects.create(
            url="https:/example.com"
        )

    def test_post_valid_ticket(self):
        url = '/tickets/'
        test_url = 'https://example.com'
        data = {'url': test_url}
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_json = response.json()
        self.assertEqual(response_json['url'], test_url)

    def test_post_invalid_ticket(self):
        url = '/tickets/'
        test_url = 'test'
        data = {'url': test_url}
        response = client.post(url, data, format='json')
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
        