from django.db import models
from core import models as core_models

# Create your models here.


class List(core_models.TimeStempedModel): # 일기 
    now = models.DateTimeField(auto_now_add=True) # 소리
#    weather = models.ImageField()
    content = models.TextField(max_length=200)
#    comment = 
