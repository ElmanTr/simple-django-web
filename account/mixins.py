from django.http import Http404
from django.shortcuts import get_object_or_404
from portfolio.models import Data

class FieldsMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_superuser:
            self.fields = [
                "title", "author", "paragraph", "slug", "category", "date", "status"
            ]
        elif request.user.is_author:
            self.fields = [
                "title","paragraph","slug","category","date"
            ]
        else:
            raise Http404("You are not author!")
        return super().dispatch(request,*args,**kwargs)

class FormValidMixin():
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
        return super().form_valid(form)

class AuthorAccessMixin():
    def dispatch(self,request,pk,*args,**kwargs):
        article = get_object_or_404(Data,pk=pk)
        if article.author == request.user and article.status == 'd' or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You can not see this page :(")

class SuperUserAccessMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You are not author of this article !!!")