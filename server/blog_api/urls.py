from django.urls import path, include
from .views import ArticleDetail, ArticleList

app_name="blog_api"

urlpatterns = [
    path('<int:pk>/', ArticleDetail.as_view(), name="detailCreate"),
    path('', ArticleList.as_view(), name="listCreate"),
]
