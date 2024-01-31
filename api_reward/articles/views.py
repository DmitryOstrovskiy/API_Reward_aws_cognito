from rest_framework import generics

from .models import Article
from .serializers import ArticleSerializer


class ListCreateArticles(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
