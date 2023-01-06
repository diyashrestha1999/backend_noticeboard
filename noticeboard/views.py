from django.shortcuts import render
from rest_framework import viewsets
from noticeboard.models import Post
from rest_framework.permissions import IsAdminUser
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .serializer import PostSerializer
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()

    def list(self, request):
        serializer = PostSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        user = request.user

        post = Post.objects.create(user=user, **data)
        ser = self.get_serializer(post)
        return Response(data=ser.data, status=201)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = PostSerializer(user)
        return Response(serializer.data)

    # def update(self, request, pk=None):
    #     pass
    #
    # def partial_update(self, request, pk=None):
    #     pass
    #
    # def destroy(self, request, pk=None):
    #     pass


