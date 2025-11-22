from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Mlibro 

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.book_data = {
            "title": "Test Book",
            "author": "Test Author",
            "isbn": "1234567890",
            "stock": 5
        }

    def test_create_book_valid(self):
        response = self.client.post('/api/libro/', self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_duplicate_isbn(self):
        Mlibro.objects.create(**self.book_data)  # primero lo creo
        response = self.client.post('/api/libro/', self.book_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_books_paginated(self):
        Mlibro.objects.create(**self.book_data)
        response = self.client.get('/api/libro/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)

    def test_filter_by_author(self):
        Mlibro.objects.create(**self.book_data)
        response = self.client.get('/api/libro/?author=Test Author')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_update_book_put(self):
        book = Mlibro.objects.create(**self.book_data)
        update_data = self.book_data.copy()
        update_data['title'] = 'Updated Title'
        response = self.client.put(f'/api/libro/{book.id}/', update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, 'Updated Title')

    def test_update_book_patch(self):
        book = Mlibro.objects.create(**self.book_data)
        response = self.client.patch(f'/api/libro/{book.id}/', {'stock': 10})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.stock, 10)

    def test_delete_book(self):
        book = Mlibro.objects.create(**self.book_data)
        response = self.client.delete(f'/api/libro/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Mlibro.objects.filter(id=book.id).exists())

    def test_create_book_negative_stock(self):
        invalid_data = self.book_data.copy()
        invalid_data['stock'] = -1
        response = self.client.post('/api/libro/', invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# Create your tests here.
