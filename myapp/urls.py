from django.urls import path
from myapp import views

urlpatterns = [
    # path('比對的路徑','要執行的function')
    # http://127.0.0.1:8000/store/
    path('', views.index),
    # http://127.0.0.1:8000/store/about/
    path('about/', views.about),
    path('about/<int:year>', views.about)

]