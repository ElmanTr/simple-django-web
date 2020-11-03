from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.ProjectList.as_view(), name='home'),
    path('contact/',views.contact, name='contact'),
    path('about/',views.about, name='about'),
    path('posts/<slug:slug>',views.PostsDetail.as_view(), name='postsdetail'),
    path('preview/<int:pk>',views.PostsPreview.as_view(), name='postspreview'),
    path('posts/',views.PostList.as_view(), name='posts'),
    path('category/<slug:slug>',views.CategoryList.as_view(), name='category'),
    path('author/<slug:username>', views.AuthorList.as_view(), name="author"),
    path('search/', views.searchbar, name='search')
]