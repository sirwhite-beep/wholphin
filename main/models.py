from django.db import models


class Comment(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.PositiveIntegerField()
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name



# Create your models here.
