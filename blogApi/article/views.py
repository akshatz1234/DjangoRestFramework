from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from .models import Article, Author
from .serializers import ArticleSerializer
from django.shortcuts import get_object_or_404


class ArticleDetail(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response({"articles": serializer.data})

class ArticleCreate(mixins.CreateModelMixin, generics.GenericAPIView):

    queryset= Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, *args, **kwargs):
       return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ArticleUpdate(generics.GenericAPIView):
    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})

class ArticleDelete(APIView):
    def delete(self, request, pk):
        # Get object with this pk
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({"message": "Article with id `{}` has been deleted.".format(pk)},status=204)