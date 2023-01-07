from django.urls import path, include
from rest_framework.routers import DefaultRouter
from noticeboard import views
from noticeboard.views import LoginView

router = DefaultRouter()
router.register(r'posts', views.PostViewSet,basename="posts")
# router.register(r'login', views.LoginView,basename="login")

urlpatterns = [
    path('', include(router.urls)),
    path('login', LoginView.as_view())

]
