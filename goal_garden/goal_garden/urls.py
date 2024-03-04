"""
URL configuration for goal_garden project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from myapp import views

admin.autodiscover()

urlpatterns = [
    path("", views.index, name='index'),
    path("admin/", admin.site.urls, name="admin"),
    path('index/', views.index, name='index'),
    path("database/", views.database, name="database"), #to be deleted
    path("403/", views.error_403, name="403_error", kwargs={'exception': Exception('Unauthorized access')}),
    path("404/", views.error_404, name="404_error", kwargs={'exception': Exception('Page not found')}),
    path("500/", views.error_500, name="500_error", kwargs={'exception': Exception('Server error')}),
    path("search/", views.search_profiles, name="search_profiles"),
    path("login/", views.login_view, name='login'),
    path("user/", login_required(views.user), name="user"), #TBR doesn't rl;y change things
    #path("user/", views.user, name="user"), #TBR
]
