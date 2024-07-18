from django.shortcuts import render
from .models import Sakila

# Create your views here.
def index(request):
    # 讀取透過 GET 傳過來的 ?id=10 資料
    id = request.GET.get('id', 1)
    country = ''
    if request.method == 'POST':
        # 讀取透過 POST 傳過來的表單資料
        country = request.POST.get('country', '')
    
    return render(request,'home/index.html',{'id':id,'country':country})

def about(reqeust):
    return render(reqeust, 'home/about.html')

def categories(request):
     # 跟Model要資料
    categories = Sakila.categories()
    return render(request, 'home/categories.html', {'categories': categories})

def countries(request):
    # 跟Model要資料
    countries = Sakila.countries()
    # print(countries)
    # render()第三個參數，把資料傳給 Template
    return render(request, 'home/countries.html', {'countries': countries})

def cities(request):
    # print(request.GET)  #key=value&key=value => {'key':['value']}
    # print(request.GET['id'])
    id = request.GET.get('id', 1)
    country = request.GET.get('country', '')
    
    # 跟Model要資料
    cities = Sakila.cities(id)
    # print(cities)
    # 將資料傳給templates，render 第三個參數{}
    return render(request, 'home/cities.html', {'cities':cities,'country':country})