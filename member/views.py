from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    # print(request.headers)

    # 讀出 headers 裡面的某類型的資料
    # print(request.headers.get('Content-Type'))
    # print(request.headers.get('User-Agent'))

    # 讀出 headers 中所有的資料
    # html += '<ul>'
    # for key, value in request.headers.items():
    #     html += f'<li>{key}：{value}</li>'
    # html += '</ul>'

    # user_agent = request.headers.get('User-Agent')
    # print('Mobile' in user_agent)
    # if 'Mobile' in user_agent:
    #     return redirect('/member/mobile/')

    # http method：GET、POST、PUT、DELETE...
    # print(request.method)  # GET

    # 讀取透過GET傳過來的資料 ?key=value
    name = request.GET.get('username') # 讀不到 username 回傳 None
    if name is None:
        name = 'Django'
    html = f'<h2>Hello {name}</h2>'

    return HttpResponse(html)
    # return render(request,'member/index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        print(name)
        print(email)
        
    return render(request, 'member/register.html',)
def mobile(request):
    return HttpResponse('<h2>Mobile 專屬</h2>')