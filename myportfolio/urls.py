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
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from account.views import Login, Registration, activate
from portfolio.views import change_lang
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,100})/$', activate, name='activate'),
    path('comment/', include('comment.urls')),
    re_path(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    path('change_lang/', change_lang, name='change_lang'),
]

urlpatterns += i18n_patterns(
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('', include('portfolio.urls')),
    path('account/',include('account.urls')),
    path('login/', Login.as_view(), name='login'),
    path('registry/', Registration.as_view(), name='registry'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'portfolio.views.page_not_found'