"""briefology URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static # new

from blog import views as blog_views
from lookup import views as lookup_views
from dictionaryanalysis import views as da_views
from users import views as users_views
from dictations import views as dictations_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.index, name='home'),
    path('blog', blog_views.blog, name='blog'),
    path('blog/<slug:slug>', blog_views.post_view, name='blogpost_view'),
    path('lookup', lookup_views.lookup, name='lookup'),
    path('dictionaryanalysis', da_views.dictionaryanalysis, name='dictionaryanalysis'),
    path('analysisresults', da_views.analysisresults, name='analysisresults'),
    path('register', users_views.register, name='register'),
    path('dictations', dictations_views.dictation_list_view, name='dictation_list_view'),
    path('dictations/<slug:slug>', dictations_views.dictation_detail_view, name='dictation_detail_view'),
    url(r'^search/$', dictations_views.search, name='search'),
]


if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)