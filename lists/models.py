from django.db import models
from core import models as core_models

# Create your models here.


class List(core_models.TimeStempedModel):
    now = models.DateTimeField(auto_now_add=True)

