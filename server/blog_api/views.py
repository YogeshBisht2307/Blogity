from rest_framework import generics
from blog.models import Article
from .serializers import ArticleSerializer


class ArticleList(generics.ListCreateAPIView): #get and post request only
    queryset = Article.artcileobjects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveAPIView): #get and delete
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
