from django.db import models

# Create your models here.


class Voter(models.Model):
    sl = models.IntegerField()
    name = models.CharField(max_length=200)
    house = models.CharField(max_length=200)
    polled = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.sl + " || " + self.name+" || " + self.house
