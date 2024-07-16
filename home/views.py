from django.shortcuts import render
from .models import Sakila

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(reqeust):
    return render(reqeust, 'about.html')

def categories(request):
     # 跟Model要資料
    categories = Sakila.categories()
    return render(request, 'categories.html', {'categories': categories})

def countries(request):
    # 跟Model要資料
    countries = Sakila.countries()
    # print(countries)
    # render()第三個參數，把資料傳給 Template
    return render(request, 'countries.html', {'countries': countries})

def cities(request):
    id = request.GET.get('id', 1)
    country = request.GET.get('country', '')
    
    # 跟Model要資料
    cities = Sakila.cities(id)
    # print(cities)
    # 將資料傳給templates，render 第三個參數{}
    return render(request, 'cities.html', {'cities':cities,'country':country})