from django.urls import path, include
from django.conf import settings

app_name = "main"
urlpatterns = [path("/", login, name="login")]

