#from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FieldsMixin, FormValidMixin, AuthorAccessMixin, SuperUserAccessMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from portfolio.models import Data
from django.urls import reverse_lazy
from .models import User
from .forms import ProfileForms

# Create your views here.

class ArticleList(LoginRequiredMixin,ListView):
    template_name = "registration/home.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
                return Data.objects.all()
        else:
                return Data.objects.filter(author=self.request.user)

class ArticleCreate(LoginRequiredMixin,FormValidMixin,FieldsMixin,CreateView):
    model = Data
    template_name = "registration/article-create-update.html"

class ArticleUpdate(AuthorAccessMixin,FormValidMixin,FieldsMixin,UpdateView):
    model = Data
    template_name = "registration/article-create-update.html"

class ArticleDelete(SuperUserAccessMixin,DeleteView):
    model = Data
    success_url = reverse_lazy('account:home')
    template_name = "registration/confirm_delete.html"

class Profile(UpdateView):
    model = User
    template_name = "registration/profile.html"
    success_url = reverse_lazy('account:profile')
    form_class = ProfileForms

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs