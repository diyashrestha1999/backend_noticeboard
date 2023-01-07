from django.shortcuts import render
from rest_framework import viewsets
from noticeboard.models import Post
from rest_framework.permissions import IsAdminUser
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .serializer import *
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


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


class LoginView(APIView):

    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']

            user = authenticate(username=username, password=password)

            if user is None:
                return Response({
                    'status': 400,
                    'message': 'user does not exit'
                })
            if not user.check_password(password):
                return Response({
                    'status': 400,
                    'message': 'password is incorrect '
                })
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({
            'message': 'success'
        })
