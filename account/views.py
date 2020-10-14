from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , CreateView
from portfolio.models import Data

# Create your views here.

class ArticleList(LoginRequiredMixin,ListView):
    template_name = "registration/home.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Data.objects.all()
        else:
            return Data.objects.filter(author=self.request.user)

class ArticleCreate(LoginRequiredMixin,CreateView):
    model = Data
    fields = ["title","author","paragraph","slug","category","date"]
    template_name = "registration/article-create-update.html"