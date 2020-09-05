import random
from django.db import models
from core import models as core_models


class Group(core_models.TimeStempedModel):

    """ Groups Model """

    name = models.CharField(max_length=150)
    uni_code = models.IntegerField(random.randint(1, 10000000))
    # Members = models.ManyToManyField("accounts.User", related_name="group", blank=True)

