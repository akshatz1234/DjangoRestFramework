from django.urls import path
from .views import ArticleDetail

app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleDetail.as_view()),
]
