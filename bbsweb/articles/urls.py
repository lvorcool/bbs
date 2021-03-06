from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'article', views.ArticleAPIViewSet)
router.register(r'comment', views.CommentAPIViewSet)

urlpatterns = [
    path('', include(router.urls))
]
