from django.shortcuts import render

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"