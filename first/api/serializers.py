from rest_framework.serializers import ModelSerializer
from first.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fiels = ['id', 'title', 'content']