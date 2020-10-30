from django.db import models


class Signup(models.Model):
    Surname = models.CharField(max_length=20)
    Other_names = models.CharField(max_length=20)
    Username = models.CharField(max_length=10)
    phone_number = models.PositiveIntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=15)

    def __str__(self):
        return self.Username

# Create your models here.
