from django.db import models
from core import models as core_models
# Create your models here.
class Comment(core_models.TimeStempedModel):

    hi = models.CharField(max_length = 50)