from django.urls import path, include
from .views import ArticleDetail, ArticleList

app_name="blog_api"

urlpatterns = [
    # route url for fetching the data of particular article using primary key article (GET request accessible only)
    path('<int:pk>/', ArticleDetail.as_view(), name="detailCreate"),
    # route url for fetching all the article (GET request only) 
    path('', ArticleList.as_view(), name="listCreate"),
]
