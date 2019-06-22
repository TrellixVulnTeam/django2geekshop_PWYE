

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name = 'возраст')

    activation_key = models.CharField(max_length=128, blank=True)
    # Ключ активации активен с текущего момента и 48 часов
    activation_key_expires = models.DateTimeField(default=(timezone.now() + timezone.timedelta(hours=48)))

    def is_activation_key_expired(self):
        return timezone.now() > self.activation_key_expires
