from django.shortcuts import render
from .models import Sakila

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(reqeust):
    return render(reqeust, 'about.html')

def countries(request):
    # 跟Model要資料
    countries = Sakila.countries()
    # print(countries)
    # render()第三個參數，把資料傳給 Template
    return render(request, 'countries.html', {'countries':countries})

