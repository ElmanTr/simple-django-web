from django.views.generic import ListView, DetailView
from account.models import User
from django.shortcuts import render, get_object_or_404
#from django.core.paginator import Paginator
from .models import Data, Category, SlideImage
from account.mixins import AuthorAccessMixin

# views

#def home(request):
#    context = {
#        "project": Data.objects.order_by('-date')[:5],
#    }
#    return render(request, 'portfolio/index.html',context)

class ProjectList(ListView):
    # model = Data
    # paginate_by =
    # context_object_name =
    queryset = Data.objects.published().order_by('-date')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slide'] = SlideImage.objects.all()
        return context

    template_name = 'portfolio/index.html'

def about(request):
    return render(request,'portfolio/about.html')

#def postsdetail(request,slug):
#    context ={
#        "project": get_object_or_404(Data,slug=slug)
#    }
#    return render(request, 'portfolio/postdetail.html', context)

class PostsDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Data,slug=slug,status='p')

    template_name = 'portfolio/postdetail.html'

class PostsPreview(AuthorAccessMixin,DetailView):
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Data,pk=pk)

    template_name = 'portfolio/postdetail.html'

class PostList(ListView):
    paginate_by = 8
    queryset = Data.objects.published()
    template_name = 'portfolio/post.html'

#def post(request):
#    projects_list = Data.objects.all()
#    paginator = Paginator(projects_list, 8)
#    page = request.GET.get('page')
#    project = paginator.get_page(page)
#    context = {
#        "project": project
#    }
#    return render(request, 'portfolio/post.html', context)

def contact(request):
    return render(request, 'portfolio/contact.html')

def base(request):
    return render(request, 'portfolio/base.html')

class CategoryList(ListView):
    paginate_by = 4
    template_name = 'portfolio/category.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.all(), slug=slug)
        return category.projects.published()

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get('slug')
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category.objects.all(), slug=slug)
        return context

#def category(request,slug):
#    category = get_object_or_404(Category,slug=slug)
#    projects_list = category.projects.all()
#    paginator = Paginator(projects_list, 4)
#    page = request.GET.get('page')
#    project = paginator.get_page(page)
#    context = {
#        "category": category,
#        "project": project,
#    }
#    return render(request, 'portfolio/category.html',context)

class AuthorList(ListView):
    paginate_by = 4
    template_name = 'portfolio/author.html'

# لیست مقالات را میگیریم
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User, username=username)
        return author.projects.all()

# مدل category را به کانتکس ها اضافه میکنیم
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
