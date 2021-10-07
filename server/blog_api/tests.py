from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import Article, Category
from django.contrib.auth.models import User

# Create your tests here.
# testing the blogAPI and its operation
class ArticleTest(APITestCase):
    def test_view_posts(self):
        # hitting the url of getting  a article, GET method
        # blog_api => name of api application and listCreate => a view which will be invoked when we hit the create article route url.
        url = reverse('blog_api:listCreate')
        # simulating a browser using client
        response = self.client.get(url, format = 'json')
        # checking that client.get() function gives the success code of HTTP_200 which indicate that we recieved the article by hitting the api url
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def create_post(self):
        # create category object of article using api
        self.test_category = Category.objects.create(name="django")
        # creating urser object using api
        self.testuser1 = User.objects.create_user(
            username = 'test_user1', password = '12345678'
        )
        # creating data dictionary which consist of all the data related to article
        data = {
            "title":"new",
            "author":1,
            "description":"desc",
            "content":"cont",
        }
        #hitting the url of creating article, POST method.
        url = reverse("blog_api:listCreate")
        # sending data of article using post request
        response = self.client.post(url, data, format = 'json')
        # checking that api return a CREATED status code or not
        self.assertEqual(response.status_code, status.CREATED)

