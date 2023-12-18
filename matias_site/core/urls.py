from django.urls import path

import core.views as views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
