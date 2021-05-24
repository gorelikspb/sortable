from django.db import models


class Pack(models.Model):
    date = models.DateField(auto_now=True) #auto just for simplify test data filling
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    distance = models.IntegerField()


    def __str__(self):
        return self.name