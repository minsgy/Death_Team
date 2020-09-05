from django.shortcuts import render


class Login(request):

    print(request.url)
    return render(request, "login.html")

