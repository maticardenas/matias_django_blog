from django.urls import include, path
from posts.views import PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"post", PostViewSet, basename="post")

app_name = "posts"

urlpatterns = [path("", include(router.urls))]
