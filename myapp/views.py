from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    # return HttpResponse('<h2>讀出所有商品資料</h2>')
    store_title = '商城首頁...'
    now = datetime.now()
    id = '123e4567-e89b-12d3-a456-426655440000'

    # return render(request, 'myapp/index.html', {'title': store_title, 'now': now})
    return render(request, 'myapp/index.html', locals())

def details(reqeust, product_id=''):
    return HttpResponse(f'<h2>讀出商品編號{ product_id }的商品</h2>')


# http://127.0.0.1:8000/store/about/2000
#  2000 會傳給 year 這個參數
def about(request, year=datetime.now().year):
    return HttpResponse(f'<h2>About { year }</h2>')

# publish => 2024/7/23
def blog(request, publish=None):
     return HttpResponse(f'<h2>讀取 { publish } 的文章</h2>')

# course_name => python-web-framework
def course(request, course_name=None):
    return HttpResponse(f'<h2>課程名稱：{ course_name }</h2>')
    