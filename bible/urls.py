"""bible URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from bibleapp import views
from django.contrib import admin
from django.urls import path
from bibleapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('video/', views.video,name='video'),
    path('audio/', views.audio,name='audio'),
    path('contact/', views.contact,name='contact'),
    path('all/<str:pk>', views.view_data),
    path('category/<str:pk>', views.subcategories,name='category'),
    path('books/<str:pk>', views.headers,name='list'),
    path('books/<str:pk>/<str:extra>', views.update_headers),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings. STATIC_URL, document_root=settings.STATIC_ROOT)