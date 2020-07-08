from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, status, viewsets
# from rest_framework.parsers import JSONParser

from .models import Article, Author
from .serializers import ArticleSerializer
from django.shortcuts import get_object_or_404

class ArticleDetail(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
class SingleArticleView(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer