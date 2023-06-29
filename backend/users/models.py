from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField('Nome', max_length=110, blank=False)
    email = models.EmailField('Email', max_length=110, blank=False)
    password = models.CharField('Password', max_length=20, blank=False)

    def __str__(self):
        return self.name
        