from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length= 100, null=True, unique = True)
    slug = models.CharField(unique = True, max_length = 120)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Category, self).save(*args, **kwargs)

    class Meta:
        db_table = "blog_categories"
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    name = models.CharField(max_length= 100, unique = True, null = False)
    slug = models.SlugField(max_length= 120)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(SubCategory, self).save(*args, **kwargs)
    

    class Meta:
        db_table = "blog_subCategories"
        verbose_name_plural = "SubCategories"




class Article(models.Model):

    class ArticleObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status = 'published')

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

    objects = models.Manager() #default manage
    artcileobjects = ArticleObject() #custom manager

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Article, self).save(*args, **kwargs)

    class Meta:
        db_table = "blog_articles"
        verbose_name_plural = "Articles"
        ordering = ('-published',)
