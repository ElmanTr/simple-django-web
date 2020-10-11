from django.contrib.auth import views
from django.urls import path
from .views import home

app_name = "account"

urlpatterns = [
    path('login/',views.LoginView.as_view(), name='login'),

    path('', home,name='home')

]