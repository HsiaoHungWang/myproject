from django.urls import path
from home import views

urlpatterns = [
    # http://127.0.0.1:8000/
    path('', views.index),
    path('countries/', views.countries),  # http://127.0.0.1:8000/countries/
    path('about/', views.about),  # http://127.0.0.1:8000/about/
    path('categories/', views.categories), # http://127.0.0.1:8000/categories/
    path('cities/', views.cities),    # http://127.0.0.1:8000/cities/
]