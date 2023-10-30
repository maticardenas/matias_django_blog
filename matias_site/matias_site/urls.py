"""matias_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth import views
from django.urls import include, path, re_path

urlpatterns = [
    path("", include("core.urls"), name="core"),
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls"), name="blog"),
    re_path(r"^accounts/login/$", views.LoginView.as_view(), name="login"),
    re_path(r"^accounts/logout/$", views.LogoutView.as_view(), name="logout", kwargs={"next_page": "/"}),
    re_path("^tinymce/", include("tinymce.urls")),
    re_path("^api/posts/", include("posts.urls"), name="posts_api"),
    re_path("^api/questions/", include("questions.urls"), name="questions_api"),

]
