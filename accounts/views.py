from django.shortcuts import render, redirect
from .models import User
from django.contrib import auth
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'join.html', {'error': "아이디 또는 비밀 번호가 다릅니다."})
    else:
        return render(request, 'account/join.html')    
def logout(request):
    auth.logout(request)
    return redirect('index')

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
            # 유저 값을 가져와 아이디/패스워드에 추가한 값을 user에 추가
            auth.login(request, user)
            return redirect('index') # 그룹 선택 화면
        return render(request, 'account/join.html') # 비밀번호 확인 실패 시 다시 돌아감.

    return render(request, 'join.html') # POST 형식 아닐 시

    