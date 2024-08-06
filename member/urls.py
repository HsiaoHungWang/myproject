from django.urls import path
from member import views 

app_name='member'
# http://127.0.0.1:8000/member/
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='create'), # http://127.0.0.1:8000/member/register/
    path('mobile/', views.mobile, name='mobile') # http://127.0.0.1:8000/member/mobile/
]