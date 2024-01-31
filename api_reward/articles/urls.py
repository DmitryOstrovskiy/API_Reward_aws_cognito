from django.urls import path

from .views import ListCreateArticles

urlpatterns = [
    path("", ListCreateArticles.as_view(), name="list_create_articles"),
]
