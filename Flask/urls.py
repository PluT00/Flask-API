"""Flask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from Users.views import UserViewSet
from Messages.views import ChatViewSet, MessageAPIView
from Posts.views import PostViewSet, CommentAPIView

router = DefaultRouter()
# Users app register.
router.register(r'users', UserViewSet)
# Messages app register.
router.register(r'chats', ChatViewSet, 'chats-list')
#Posts app register.
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/chats/<int:pk>/post_message/', MessageAPIView.as_view()),
    path('api/posts/<int:pk>/post_comment/', CommentAPIView.as_view()),
    path('openapi', get_schema_view(
        title="Flask Social Network",
        description="API for Flask"
    ), name='openapi-schema')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
