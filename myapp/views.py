from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    return HttpResponse('<h2>myapp 首頁</h2>')

def about(request, year=datetime.now().year):
    return HttpResponse(f'<h2>About { year }</h2>')