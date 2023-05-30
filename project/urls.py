"""
URL configuration for project project.


The `urlpatterns` list routes URLs to views. For more information please see:
   https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from syncsocial import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.home, name='home'),
   path('login/', views.login_view, name='login'),
   path('createuser/', views.createuser, name='createuser'),
   path('add-friends/', views.add_friends, name='add_friends'),  # Fixed import
   path('add-free-dates/', views.add_free_dates, name='add_free_dates'),
   path('notifications/', views.notifications, name='notifications'),
   path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Use 'login' as the next_page parameter

]

