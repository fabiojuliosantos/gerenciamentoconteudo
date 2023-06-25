from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField('Username', max_length=50, blank=False)
    name = models.CharField('Nome', max_length=110, blank=False)
    email = models.EmailField('Email', max_length=110, blank=False)
    password = models.CharField('Password', max_length=20, blank=False)

    def __str__(self):
        return self.name
        