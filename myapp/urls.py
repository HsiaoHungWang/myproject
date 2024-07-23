from django.urls import path
from myapp import views

urlpatterns = [
    # path('比對的路徑','要執行的function')
    # http://127.0.0.1:8000/store/
    path('', views.index),

    # http://127.0.0.1:8000/store/details/uuid
    path('details/<uuid:product_id>', views.details),
    # http://127.0.0.1:8000/store/about/
    path('about/', views.about),
     # http://127.0.0.1:8000/store/about/2000
    path('about/<int:year>', views.about),
     # http://127.0.0.1:8000/store/blog/2024/7/1
    path('blog/<path:publish>', views.blog),
    path('course/<slug:course_name>', views.course)

]