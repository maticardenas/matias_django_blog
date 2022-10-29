from api.views import PostViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"post", PostViewSet, basename="post")

app_name = "api"

urlpatterns = [path("", include(router.urls))]
