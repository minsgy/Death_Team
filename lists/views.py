from django.shortcuts import render
from . import models


def detail(request):

    """ list views """
    return render(request, "page.html")
