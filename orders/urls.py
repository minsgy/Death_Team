from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path("/", views.order, name="order"),
    path("payment/", views.payment, name="payment"),
]
