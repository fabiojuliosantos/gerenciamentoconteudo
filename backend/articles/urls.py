from django.urls import include, path
from .views import ArticleView

urlpatterns = [
    path('article', ArticleView.as_view())
]

