
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # route url for admin application
    path('admin/', admin.site.urls),
    # route url for api application
    path('api/', include("blog_api.urls", namespace = "blog")),
    # route url for blog application
    path('', include("blog.urls",namespace = "blog_api")),
]
