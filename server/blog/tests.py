from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Article , Category, SubCategory

# Create your tests here.
class Test_Create_Article(TestCase):

    # creating category ,sub category , user and article for testing enviroment.
    @classmethod
    def setUpTestData(cls):
        # create category object
        test_category = Category.objects.create(name="web development")
        # create subcategory object
        test_subcategory = SubCategory.objects.create(name="django", category_id = 1)
        # create user object
        test_user = User.objects.create_user(username="test_user1", password = "123456789")
        # create article object
        test_article = Article.artcileobjects.create(category_id = 1, sub_category_id=1, title="Article Title", description="description", content = "content", author_id = 1, status = 'published')

    # function for performing test operation or checking wether Queries invoked inside setUpTestData are working well or not
    def test_blog_content(self):
        article = Article.artcileobjects.get(id=1)
        cat= Category.objects.get(id=1)

        author = f'{article.author}'
        description = f'{article.description}'
        title = f'{article.title}'
        content = f'{article.content}'
        status = f'{article.status}'

        # checking that object created using setUpTestData are created as per requirements or not
        self.assertEqual(author, 'test_user1') 
        self.assertEqual(title, 'Article Title')
        self.assertEqual(description, 'description')
        self.assertEqual(content, 'content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(article), 'Article Title')
        self.assertEqual(str(cat), 'web development')



