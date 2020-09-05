from django.db import models
from core import models as core_models


class Essays(core_models.TimeStempedModel):

    name = models.CharField(max_length=50)
   # start_page = models.ForeignKey("lists.List", on_delete=models.CASCADE)
   # last_page = models.ForeignKey("lists.List", on_delete=models.CASCADE)

