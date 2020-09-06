from django.shortcuts import render, redirect
from django.utils import timezone
from . import models


def detail(request):

    """ list views 일기장 """

    page = models.List()

    page.now = timezone.now()
    page.content = "불라불라"
    return render(request, "list/list.html", {"page": page})


def create(request):

    if request.method == "POST":
        item = models.List()

        item.name = request.POST["title"]  # 제목
        # item.user = request.user  # 작성자
        item.now = request.POST["date"]
        item.content = request.POST["message"]  # 내용
        item.photos = request.POST["photos"]  # 사진
        item.save()

        return redirect("detail")
    return render(request, "create.html", {"item": item})

