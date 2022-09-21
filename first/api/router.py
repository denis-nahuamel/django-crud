from rest_framework.routers import DefaultRouter
from first.api.views import PostApiViewSet

router_post = DefaultRouter()
router_post.register(prefix='post', basename='post', viewsets=PostApiViewSet)