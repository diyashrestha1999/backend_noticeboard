from django.urls import path, include
from rest_framework.routers import DefaultRouter
from noticeboard import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet,basename="posts")
urlpatterns = [
    path('', include(router.urls)),
]
