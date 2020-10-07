from django.views.generic import ListView , DetailView
from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator
from .models import Data , Category

# views

#def home(request):
#    context = {
#        "project": Data.objects.order_by('-date')[:5],
#    }
#    return render(request, 'portfolio/index.html',context)

class ProjectList(ListView):
    # model = Data
    #paginate_by =
    queryset = Data.objects.order_by('-date')[:5]
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
        return get_object_or_404(Data,slug=slug)

    template_name = 'portfolio/postdetail.html'

def post(request):
    projects_list = Data.objects.all()
    paginator = Paginator(projects_list, 8)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    context = {
        "project": project
    }
    return render(request, 'portfolio/post.html', context)

def contact(request):
    return render(request, 'portfolio/contact.html')

def login(request):
    email = request.GET.get('email')
    return render(request, 'portfolio/login.html', {'email':email})

def base(request):
    return render(request, 'portfolio/base.html')

def category(request,slug):
    category = get_object_or_404(Category,slug=slug)
    projects_list = category.projects.all()
    paginator = Paginator(projects_list, 4)
    page = request.GET.get('page')
    project = paginator.get_page(page)
    context = {
        "category": category,
        "project": project,
    }
    return render(request, 'portfolio/category.html',context)
