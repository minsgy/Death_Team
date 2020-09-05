from django.db import models


class Order(models.Model):

    """ Order models """

    book = models.ForeignKey("essays.Essays", on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)

    adress = models.CharField(max_length=150)
    book_count = models.IntegerField()

    price = models.IntegerField()
