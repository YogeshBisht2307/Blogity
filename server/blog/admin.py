from django.contrib import admin
from .models import *


# Register your models here.
# registering model in admin file so that they are visible in the django-admin pannel
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(SubCategory)
