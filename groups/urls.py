from django.urls import path
from . import views

urlpatterns = [
    path("groupmain/", views.group_home, name="group_main"),  # 홈페이지 실행 시 로그인 창 출력  
]
