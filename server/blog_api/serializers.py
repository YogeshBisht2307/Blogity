from rest_framework import serializers
from blog.models import Article


# model serializer for Article Model
class ArticleSerializer(serializers.ModelSerializer):
    # meta class for defining the data of Article serializers class
    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'description', 'content', 'status')