# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Articles, Comments
from .permissions import IsOwnerOrReadOnly
from .serializers import ArticlesSerializer, CommentsSerializer, ArticlesSerializerV2


class ArticleAPIViewSet(viewsets.ModelViewSet):
    """
    使用serializers和viewset
    """
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.version == "v2":
            return ArticlesSerializerV2
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentAPIViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'articles': reverse('article-list', request=request, format=format)
    })
