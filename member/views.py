from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from django.core.files.storage import FileSystemStorage
from .models import Member
from django.contrib.auth.hashers import make_password, check_password
from .forms import MemberForm, UserForm
from datetime import datetime, timedelta

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



    # return HttpResponse('資料庫操作練習')

    # 讀取會員所有資料
    members = Member.objects.all()
    return render(request, 'member/index.html',{'members': members})

def register(request):
    if request.method == 'POST':
       
        # 接收使用者上傳的資料
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        password = request.POST.get('userpassword')
        birth = request.POST.get('userbirth')

         # 接收上傳的檔案
        avatar = request.FILES.get('userphote')
        # # 檔案名稱
        file_name = avatar.name
        # # 檔案大小
        # file_size = avatar.size
        # # 檔案類型
        # file_type = avatar.content_type

        # print(f'檔案名稱：{ file_name }')
        # print(f'檔案大小：{ file_size }')
        # print(f'檔案類型{ file_type }')

        # 將上傳檔案儲存到uploads資料夾
        fs = FileSystemStorage()
        upload_file = fs.save(file_name, avatar)

        
        Member.objects.create(
            member_name = name,
            member_password = make_password(password), 
            member_birth = birth,
            member_email = email,
            member_avatar = upload_file
        )

        return redirect('member:index')


       
        # print(f'upload file:{ upload_file }')
        
    return render(request, 'member/register.html',)

# /edit/?id=5
def edit(request):
    if request.method == 'POST':
        # 接收使用者上傳的資料
        id = request.POST.get('userid')
        name = request.POST.get('username')
        email = request.POST.get('useremail')    
        birth = request.POST.get('userbirth')
         # 接收上傳的檔案
        avatar = request.FILES.get('userphote')
        file_name = avatar.name
        # 將上傳檔案儲存到uploads資料夾
        fs = FileSystemStorage()
        upload_file = fs.save(file_name, avatar)
        # 修改到資料庫
        member = Member.objects.get(member_id=id) 
        member.member_name = name
        member.member_email = email
        member.member_birth = birth
        member.member_avatar = upload_file
        member.save()
        return redirect('member:index')

  

    id  = request.GET.get('id', 1)
    member = Member.objects.get(member_id=id)  
    return render(request, 'member/edit.html',{'member': member})


# /delete/1
def delete(request, id):   
    member = Member.objects.get(member_id=id)  
    member.delete()

    return redirect('member:index')


def mobile(request):
    return HttpResponse('<h2>Mobile 專屬</h2>')

def formdemo(request):
    form = MemberForm()
    userForm = UserForm()
    return render(request, 'member/formdemo.html', locals())

def write(request):
    response = render(request, 'member/write.html', locals())
    title = "cookie demo"
    # 已經登入

    # 將資料寫進cookies
    response.set_cookie('is_login', True)
    # 將資料寫進session
    request.session['name'] = 'Jack'

    # return render(request, 'member/write.html',{'title': title})
    return response


def read(request):
    title = "abcdefg"

    # 讀取 cookie
    is_login = request.COOKIES.get('is_login')    
    print(is_login)

    # 讀取 session
    if 'name' in request.session:
        name = request.session['name']
    else:
        name = 'guest'
    print(name)

    return render(request, 'member/read.html',{'title': title})

def login(request):
    if request.method == 'POST':
        # 接收表單傳過來的資料
        member_name = request.POST.get('member_name')
        member_password = request.POST.get('member_password')
        remember_me = request.POST.get('remember_me')

        # print(member_name)
        # print(member_password)
        # print(remember_me)
        
        message = ''

        # 檢查是否有此帳號
        member = Member.objects.filter(member_name=member_name).first()
        if member:            
            message = '有此帳號'
            # 檢查密碼是否正確
            if check_password(member_password, member.member_password):
                response = HttpResponse('<script>alert("登入成功");location.href="/member/"</script>')
                message = '有此帳號且密碼正確'
                # 表示登入成功，我們要將登入成功的資訊存進cookie或者是session
                if remember_me == 'on':
                    # 保留 cookie 的值一段時間
                    maxAgeTime = timedelta(minutes=1)
                    response.set_cookie('name', member_name, max_age=maxAgeTime)
                    
                else:
                    # 瀏覽器關掉就讓 cookie 的值消失
                    response.set_cookie('name', member_name)
                    
                # 轉到會員首頁
                return response
            else:
                message = '密碼不正確'

        else:
            message = '查無此帳號'

        return render(request, 'member/login.html', {'message': message})


    return render(request, 'member/login.html')

def logout(request):
    # 清除 session 中的資料
    request.session.clear()

    # 清除 cookie 中的資料
    response = HttpResponse('<script>alert("登出成功");location.href="/member/login"</script>')
    response.delete_cookie('name')
    response.delete_cookie('is_login')

    return response


