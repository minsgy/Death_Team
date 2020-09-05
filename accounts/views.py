from django.shortcuts import render, redirect
from . import User
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
            return render(request, 'login.html', {'error': "아이디 또는 비밀 번호가 다릅니다."})
    else:
        return render(request, 'login.html')    
def logout(request):
    pass

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
            # 아이디, 
            auth.login(request, user)
            return redirect('index') # 그룹 선택 화면
        return render(request, 'signup.html') # 비밀번호 확인 실패 시 다시 돌아감.

    return render(request, 'signup.html') # POST 형식 아닐 시

    