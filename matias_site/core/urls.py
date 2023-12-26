import core.views as views
from django.urls import path

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
