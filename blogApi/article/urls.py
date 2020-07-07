from django.urls import path
from .views import ArticleDetail, ArticleCreate, ArticleDelete, ArticleUpdate

app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleDetail.as_view()),
    path('articles/create', ArticleCreate.as_view()),
    path('articles/delete/<int:pk>', ArticleDelete.as_view()),
    path('articles/update/<int:pk>', ArticleUpdate.as_view()),
    
]
