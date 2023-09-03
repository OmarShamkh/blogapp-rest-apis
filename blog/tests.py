from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Post

class AdminPostDetailTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.admin = User.objects.create_superuser(username='admin', password='adminpass')
        self.post = Post.objects.create(user=self.user, title='Test Post', content='Test Content')

    def test_create_post_as_admin(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post('/admin/posts/', {'title': 'New Post', 'content': 'New Content'})
        self.assertEqual(response.status_code, 201)

    def test_create_post_as_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post('/admin/posts/', {'title': 'New Post', 'content': 'New Content'})
        self.assertEqual(response.status_code, 403)

    def test_edit_post_as_admin(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.put(f'/admin/posts/{self.post.id}/', {'title': 'Updated Post', 'content': 'Updated Content'})
        self.assertEqual(response.status_code, 200)

    def test_edit_post_as_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.put(f'/admin/posts/{self.post.id}/', {'title': 'Updated Post', 'content': 'Updated Content'})
        self.assertEqual(response.status_code, 403)

    def test_delete_post_as_admin(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.delete(f'/admin/posts/{self.post.id}/')
        self.assertEqual(response.status_code, 200)

    def test_delete_post_as_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(f'/admin/posts/{self.post.id}/')
        self.assertEqual(response.status_code, 403)
