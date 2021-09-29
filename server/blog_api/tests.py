from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Article, Category
from django.contrib.auth.models import User

# Create your tests here.

class ArticleTest(APITestCase):
    def test_view_posts(self):
        # hitting the url of creating a article
        url = reverse('blog_api:listCreate')
        # simulating a brower using client
        response = self.client.get(url, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def create_post(self):
        self.test_category = Category.objects.create(name="django")
        self.testuser1 = User.objects.create_user(
            username = 'test_user1', password = '12345678'
        )
        data = {
            "title":"new",
            "author":1,
            "description":"desc",
            "content":"cont",
        }
        url = reverse("blog_api:listCreate")
        response = self.client.post(url, data, format = 'json')
        self.assertEqual(response.status_code, status.CREATED)

