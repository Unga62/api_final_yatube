from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.pagination import LimitOffsetPagination

from api.const import DELETE_TEXT, EDIT_TEXT, POST_ID
from api.permissions import BaseIsAuthorOrReadOnly
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer
)
from posts.models import Group, Post, User


class ListCreateViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (BaseIsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied(EDIT_TEXT)
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied(DELETE_TEXT)
        super(PostViewSet, self).perform_destroy(instance)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (BaseIsAuthorOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (BaseIsAuthorOrReadOnly,)

    def post_object(self):
        return get_object_or_404(Post, pk=self.kwargs.get(POST_ID))

    def get_queryset(self):
        return self.post_object().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.post_object())

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied(EDIT_TEXT)
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied(DELETE_TEXT)
        super(CommentViewSet, self).perform_destroy(instance)


class FollowViewSet(ListCreateViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        return user.follower
