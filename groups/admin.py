from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Group)
class RoomAdmin(admin.ModelAdmin):

    """ Group Admin Definition """

    pass
