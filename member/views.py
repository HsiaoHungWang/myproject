from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Member

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
    # name = request.GET.get('username') # 讀不到 username 回傳 None
    # if name is None:
    #     name = 'Django'    
    # html = f'<h2>Hello {name}</h2>'

    # response = HttpResponse(html)
    # response.status_code = 200
    # [{},{}]
    # response['Content-Type'] = 'application/json'
    # response.encoding = 'utf-8'


    # return HttpResponse(html)
    # return render(request,'member/index.html',{})


    # 資料庫操作 CRUD
    # 新增
    # Member.objects.create(
    #     member_name = 'Jack',
    #     member_password = '12345678',
    #     member_birth = '1998-11-20',
    #     member_email = 'Jack@gmail.com'
    # )

    # # 讀取所有會員資料
    # members = Member.objects.all()
    # print(members)

    # # 讀取單筆資料
    # member = Member.objects.get(member_id=2)    
    # print(member)

    # 修改
    # 先找到要修改的資料
    # member = Member.objects.get(member_id=2)  
    # # 進行修改
    # member.member_name = 'Jack2'
    # member.member_birth = '1998-01-20'
    # # 將修改完的結果更新到資料庫
    # member.save()

    # 刪除
    #  # 先找到要刪除的資料
    # member = Member.objects.get(member_id=2)  
    # # 進行刪除
    # member.delete()



    return HttpResponse('資料庫操作練習')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        # 接收上傳的檔案
        avator = request.FILES.get('userphote')
        # 檔案名稱
        file_name = avator.name
        # 檔案大小
        file_size = avator.size
        # 檔案類型
        file_type = avator.content_type

        print(f'檔案名稱：{ file_name }')
        print(f'檔案大小：{ file_size }')
        print(f'檔案類型{ file_type }')

        # 上傳檔案
        fs = FileSystemStorage()
        upload_file = fs.save(file_name, avator)
        print(f'upload file:{ upload_file }')
        
    return render(request, 'member/register.html',)
def mobile(request):
    return HttpResponse('<h2>Mobile 專屬</h2>')
