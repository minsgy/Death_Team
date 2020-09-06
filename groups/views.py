from django.shortcuts import render
from .models import Group 
# Create your views here.

def group_home(request):
    groups = Group.objects.all() # 모든 그룹 리스트 출력
    return render(request, "groups/main.html",{'groups':groups})