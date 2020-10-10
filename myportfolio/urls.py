"""myportfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from portfolio import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.ProjectList.as_view(), name='home'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('posts/<slug:slug>',views.PostsDetail.as_view(), name='postsdetail'),
    path('posts/',views.PostList.as_view(), name='posts'),
    path('login/',views.login, name='login'),
    path('category/<slug:slug>',views.CategoryList.as_view(), name='category'),
    path('author/<slug:username>', views.AuthorList.as_view(), name="author")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)