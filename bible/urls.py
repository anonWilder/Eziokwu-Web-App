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

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', views.home),
    path('all/<str:pk>', views.view_data),
    path('category/<str:pk>', views.subcategories,name='category'),
    path('books/<str:pk>', views.headers,name='list'),
    path('books/<str:pk>/<str:extra>', views.update_headers),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout'),
]
