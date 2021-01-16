from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from portfolio.models import Data

class FieldsMixin():
    def dispatch(self,request,*args,**kwargs):
        self.fields = [
            "title_fa", "paragraph_fa", 'title_en', 'paragraph_en', "slug", "category", "date", "is_special", "status",
        ]
        if request.user.is_superuser:
            self.fields.append("author")
        return super().dispatch(request,*args,**kwargs)

class FormValidMixin():
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            if not self.obj.status in ['d','i'] :
                self.obj.status = 'd'
        return super().form_valid(form)

class AuthorAccessMixin():
    def dispatch(self,request,pk,*args,**kwargs):
        article = get_object_or_404(Data, pk=pk)
        if article.author == request.user and article.status == 'd' or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You are not allowed to do this! :(")

class SuperUserAccessMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("You are not allowed to do this !")

class AuthorsUserAccessMixin():
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.is_author:
                return super().dispatch(request, *args, **kwargs)
            else:
                return redirect("account:profile")
        else:
            return redirect("login")