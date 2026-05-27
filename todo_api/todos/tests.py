from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Todo



# Create your tests here.

class TodoApiTestCase(APITestCase):
    def setUp(self):
        self.todo=Todo.objects.create(title="Test Todo", description="Test description")
        
    def test_list_todos(self):
        response=self.client.get('/api/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(len(response.data),1)
        
        
    def test_create_todo(self):
        data={"title":"New Todo", "description":"New description","completed":False}
        response=self.client.post('/api/todos/',data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(),2)
        
    def test_retrieve_todo(self):
        response=self.client.get(f'/api/todos/{self.todo.id}/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Todo")
        
            
        
        