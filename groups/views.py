from django.shortcuts import render
from accounts.models import User 
from .models import Group 
# Create your views here.

def group_home(request):
    groups = Group.objects.all() # 모든 그룹 리스트 출력
    return render(request, "groups/main.html",{'groups':groups})

def group_create(request):
    if request.method == 'POST':
        group = Group() #객체생성
        if 'image' in request.FILES: 
            group.image = request.FILES['image'] # new.html의 name="image"
        group.name = request.POST['name'] # new.html의 name="name"
        group.save()
        # redirect 함수는 import 해주어야 사용 가능함.
        # redirect('urls의 path name = 'profile/'+str(post.id), pk)
        # save 한 후 , detail의 주소로 보내는 것. ( pk(post-id)을 통해 감)
        # redirect 는 이동만 하는 거고, render 는 새로 만드는 것.
        return redirect('group_main')
    return render(request, 'groups/makegroup.html')