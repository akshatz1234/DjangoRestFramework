from rest_framework import serializers

from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_id', 'name', 'email')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('author_id','title', 'description', 'body', 'id')