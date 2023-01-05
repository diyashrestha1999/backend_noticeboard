from django.shortcuts import render
from rest_framework import viewsets

from noticeboard.models import Post
from noticeboard.serializer import *


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class= PostSerializer
    # serializer= PostSerializer(queryset)



