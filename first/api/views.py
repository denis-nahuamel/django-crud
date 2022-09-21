from rest_framework.viewsets import ModelViewSet
from first.models import Post
from first.api.serializers import PostSerializer
class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()