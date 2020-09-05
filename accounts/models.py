from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """ Custom user Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    # tuple
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    avatar = models.ImageField(blank=True)  # 프로필
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=10,
        blank=True,
        default=GENDER_MALE,  # choices 의 default 값
    )

    age = models.IntegerField()
