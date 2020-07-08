from django.urls import path
from .views import *

app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleDetail.as_view()),
    path('articles/update/<int:pk>', SingleArticleView.as_view()),
    path('articles/delete/<int:pk>', ArticleDetail.as_view()),
]
