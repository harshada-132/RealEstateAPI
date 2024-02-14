# tests.py

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import House

class HouseAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_house(self):
        data = {
            'owner': 'Shilpa Sawrikar',
            'area': '4589 Sq.Ft.',
            'sale_price': '10000000',
            'negotiable': True,
            'location': 'Somwar Peth'  
        }
        response = self.client.post('/houses/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(House.objects.count(), 1)
        self.assertEqual(House.objects.get().owner, 'Shilpa Sawrikar')
        self.assertEqual(House.objects.get().location, 'Somwar Peth')  