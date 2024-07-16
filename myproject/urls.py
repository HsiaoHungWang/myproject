"""
URL configuration for myproject project.

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

from member import views as member_view
from home import views as home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view.index),  # http://127.0.0.1:8000/
    path('countries/', home_view.countries),    # http://127.0.0.1:8000/countries/
    path('about/', home_view.about),  # http://127.0.0.1:8000/about/
    path('categories/', home_view.categories), # http://127.0.0.1:8000/categories/
    path('member/', member_view.index),     # http://127.0.0.1:8000/member/
    path('cities/', home_view.cities),    # http://127.0.0.1:8000/cities/
    path('member/mobile/', member_view.mobile),   # http://127.0.0.1:8000/member/mobile/
    path('member/register/', member_view.register)   # http://127.0.0.1:8000/member/mobile/


]
