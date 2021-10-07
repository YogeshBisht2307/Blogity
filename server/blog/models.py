from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length= 100, null=True, unique = True)
    slug = models.CharField(unique = True, max_length = 120)

    def __str__(self):
        return str(self.name)

    # Overriding the save method of Category model class for storing category slug with the help of slugify method. 
    #  Category name will be slugify into the slug 
    # Example :- web development => web-development

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Category, self).save(*args, **kwargs)

    #meta class for storing the additional data of category model such as database table name and django admin model name.
    class Meta:
        db_table = "blog_categories"
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    name = models.CharField(max_length= 100, unique = True, null = False)
    slug = models.SlugField(max_length= 120)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.name)

    # Overriding the save method of SubCategory model class for storing category slug with the help of slugify method. 
    # SubCategory name will be slugify into the slug 
    # Example :- django development => django-development
    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(SubCategory, self).save(*args, **kwargs)
    

    # meta class for storing the additional data of SubCategory model such as database table name and django admin model name.
    class Meta:
        db_table = "blog_subCategories"
        verbose_name_plural = "SubCategories"




class Article(models.Model):

    # manager class for overriding the (models.objects.get() ) objects part of query so that it overrided ArticleObject will fetch only published article
    class ArticleObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status = 'published')

    # choices options for status column of the article model it will be displayed as dropdown to choose the status of a article.
    options = (
        ('draft', 'Draft'),
        ('published', "Published"),
    )

    title = models.CharField(max_length = 200, null = False, unique = True)
    slug = models.SlugField(max_length= 220)
    description = models.CharField(max_length = 200)
    content = models.TextField()
    image = models.FileField(upload_to= "Upload/Article/")
    published = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.
    CASCADE, related_name = 'blog_posts')
    category = models.ForeignKey(Category, on_delete = models.PROTECT, default = 1)
    sub_category = models.ForeignKey(SubCategory, on_delete  = models.PROTECT)
    status = models.CharField(max_length = 10, choices = options, default = 'published')

    objects = models.Manager() #default manageer

    # 1. Now we can access query for published item as follow using artcileobjects
    # 2. Example => models.artcileobjects.all()
    artcileobjects = ArticleObject() #custom manager

    def __str__(self):
        return str(self.title)


    # Overriding the save method of Article model class for storing category slug with the help of slugify method. 
    # Article name will be slugify into the slug 
    # Example :- creating a crud application using django =>       creating-a-crud-application-using-django
    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Article, self).save(*args, **kwargs)

    # meta class for storing the additional data of SubCategory model such as database table name ,django admin model name and ordering of article.
    class Meta:
        db_table = "blog_articles"
        verbose_name_plural = "Articles"
        ordering = ('-published',)
