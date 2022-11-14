from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CommentsViewSet,
    GroupsViewSet,
    PostsViewSet,
    FollowViewSet
)

router_v1 = DefaultRouter()

router_v1.register(
    'posts',
    PostsViewSet,
    basename='posts'
)

router_v1.register(
    'groups',
    GroupsViewSet,
    basename='groups'
)

router_v1.register(
    r'posts/(?P<post_id>[1-9]\d*)/comments',
    CommentsViewSet,
    basename='comments'
)

router_v1.register(
    'follow',
    FollowViewSet,
    basename='follow'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
