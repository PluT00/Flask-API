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
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from Users.views import UserListAPIView, CreateUserAPIView, UserDetailAPIView
from Messages.views import ChatViewSet, MessageAPIView
from Posts.views import PostViewSet, CommentAPIView

router = DefaultRouter()
# Messages app register.
router.register(r'chats', ChatViewSet, 'chats-list')
#Posts app register.
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # API root.
    path('api/', include(router.urls)),
    # JWTAuthentication urls.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Applications urls.
    path('api/users/', UserListAPIView.as_view()),
    path('api/users/<int:pk>/', UserDetailAPIView.as_view()),
    path('api/users/create/', CreateUserAPIView.as_view()),
    path('api/chats/<int:pk>/messages/', MessageAPIView.as_view()),
    path('api/posts/<int:pk>/post_comment/', CommentAPIView.as_view()),
    # SwaggerUI docs urls.
    path('openapi', get_schema_view(
        title="Flask Social Network",
        description="API for Flask"
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
