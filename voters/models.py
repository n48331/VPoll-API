from django.db import models

# Create your models here.


class Voter(models.Model):
    sl = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    house = models.CharField(max_length=200)
    polled = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.name + self.house
