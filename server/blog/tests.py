from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Article , Category, SubCategory

# Create your tests here.
class Test_Create_Article(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name="web development")
        test_category = SubCategory.objects.create(name="django", category_id = 1)
        test_user = User.objects.create_user(username="test_user1", password = "123456789")
        test_article = Article.artcileobjects.create(category_id = 1, sub_category_id=1, title="Article Title", description="description", content = "content", author_id = 1, status = 'published')


    def test_blog_content(self):
        article = Article.artcileobjects.get(id=1)
        cat= Category.objects.get(id=1)
        author = f'{article.author}'
        description = f'{article.description}'
        title = f'{article.title}'
        content = f'{article.content}'
        status = f'{article.status}'

        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Article Title')
        self.assertEqual(description, 'description')
        self.assertEqual(content, 'content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(article), 'Article Title')
        self.assertEqual(str(cat), 'web development')



